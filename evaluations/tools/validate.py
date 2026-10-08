#!/usr/bin/env python3
"""Validate this pack and prepare blank run files. Never calls or scores a model."""
import argparse
from collections import Counter
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
CATEGORIES = (
    'script_conversion', 'apostrophes', 'mixed_ru_uz', 'business_dialogue',
    'instruction_adherence', 'name_number_preservation', 'grounded_abstention',
    'structured_reasoning',
)
IDS = [f'uz-eval-{i:03d}' for i in range(1, 25)]
FIELDS = {'id', 'category', 'language', 'input', 'expected_or_rubric', 'notes'}
LANGUAGES = {'uz-Latn', 'uz-Cyrl', 'uz-Latn+ru-Cyrl', 'en+uz-Latn', 'uz-Latn+uz-Cyrl'}
OUTCOMES = {'pass', 'fail', 'needs_review', 'ungraded'}
CHECKS = {'pass', 'fail', 'needs_review'}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, f'duplicate JSON key: {key}')
        result[key] = value
    return result


def invalid_constant(value):
    raise ValueError(f'non-standard JSON constant: {value}')


def read_jsonl(path):
    raw = Path(path).read_bytes()
    text = raw.decode('utf-8')
    require(not text.startswith('\ufeff'), 'UTF-8 BOM is not permitted')
    rows = []
    for n, line in enumerate(text.splitlines(), 1):
        require(bool(line.strip()), f'blank line at line {n}')
        try:
            row = json.loads(line, object_pairs_hook=unique_object, parse_constant=invalid_constant)
        except ValueError as exc:
            raise ValueError(f'line {n}: {exc}') from exc
        require(isinstance(row, dict), f'line {n}: record must be an object')
        rows.append(row)
    require(bool(rows), 'file is empty')
    return rows, hashlib.sha256(raw).hexdigest()


def validate_pack(path):
    rows, digest = read_jsonl(path)
    require(len(rows) == 24, 'pack must contain exactly 24 records')
    require([r.get('id') for r in rows] == IDS, 'IDs must be unique and ordered uz-eval-001 through uz-eval-024')
    require(Counter(r.get('category') for r in rows) == Counter({c: 3 for c in CATEGORIES}), 'each of the eight categories must have exactly three cases')
    for row in rows:
        ident = row['id']
        require(set(row) == FIELDS, f'{ident}: top-level fields differ from schema')
        for key in ('id', 'category', 'language', 'input', 'notes'):
            require(isinstance(row[key], str) and bool(row[key].strip()), f'{ident}: {key} must be a nonempty string')
        require(row['language'] in LANGUAGES, f'{ident}: unsupported language notation')
        grade = row['expected_or_rubric']
        require(isinstance(grade, dict), f'{ident}: grading specification must be an object')
        kind = grade.get('type')
        if kind == 'exact_text':
            require(set(grade) == {'type','normalization','expected'}, f'{ident}: incorrect exact_text fields')
            require(isinstance(grade['expected'], str) and bool(grade['expected']), f'{ident}: expected must be a nonempty string')
            require(grade['normalization'] in {'nfc_trim','apostrophe_equivalent'}, f'{ident}: unsupported text normalization')
        elif kind == 'json':
            require(set(grade) == {'type','string_normalization','extra_keys','expected'}, f'{ident}: incorrect json fields')
            require(isinstance(grade['expected'], (dict,list)), f'{ident}: expected JSON must be an object or array')
            require(grade['extra_keys'] is False, f'{ident}: extra_keys must be false')
            require(grade['string_normalization'] in {'nfc','apostrophe_equivalent'}, f'{ident}: unsupported JSON string normalization')
        elif kind == 'checklist':
            require(set(grade) == {'type','reference_answer','checks'}, f'{ident}: incorrect checklist fields')
            require(isinstance(grade['reference_answer'], str) and bool(grade['reference_answer'].strip()), f'{ident}: missing reference answer')
            checks = grade['checks']
            require(isinstance(checks, list) and len(checks) >= 2, f'{ident}: checklist needs at least two checks')
            for n, check in enumerate(checks, 1):
                require(isinstance(check, dict) and set(check) == {'id','criterion'}, f'{ident}: incorrect check fields')
                require(check['id'] == f'C{n}', f'{ident}: check IDs must be sequential')
                require(isinstance(check['criterion'], str) and bool(check['criterion'].strip()), f'{ident}: empty criterion')
        else:
            raise ValueError(f'{ident}: unknown grading type {kind!r}')
    return rows, digest


def init_run(directory, rows, digest):
    directory = Path(directory)
    paths = [directory/'metadata.json', directory/'responses.jsonl']
    require(not any(p.exists() for p in paths), 'refusing to overwrite existing metadata.json or responses.jsonl')
    directory.mkdir(parents=True, exist_ok=True)
    metadata = {
        'pack_version':'0.1.0', 'corpus_sha256':digest,
        'template_created_at_utc':datetime.now(timezone.utc).isoformat(),
        'run_started_at_utc':None, 'run_finished_at_utc':None,
        'repository_commit':None, 'provider_or_local_runner':None,
        'model_id':None, 'model_version_or_snapshot':None, 'interface_and_version':None,
        'system_instruction':None, 'provider_defaults_or_hidden_instructions':'unknown',
        'temperature':None, 'top_p':None, 'max_output_tokens':None, 'seed':None,
        'other_generation_settings':{}, 'tools_enabled':False, 'fresh_context_per_case':True,
        'local_weight_revision':None, 'local_quantization':None,
        'local_runtime_version':None, 'local_chat_template':None,
        'planned_attempts_per_case':1, 'reviewers':[], 'notes':None,
    }
    responses = [{'case_id':r['id'], 'attempt':1, 'status':'not_run',
        'collected_at_utc':None, 'raw_output':None, 'error':None,
        'truncated':None, 'grading':None} for r in rows]
    # Exclusive creation is intentional; never silently replace research records.
    with paths[0].open('x', encoding='utf-8') as handle:
        json.dump(metadata, handle, ensure_ascii=False, indent=2)
        handle.write('\n')
    with paths[1].open('x', encoding='utf-8') as handle:
        for row in responses:
            handle.write(json.dumps(row, ensure_ascii=False) + '\n')
    return paths


def check_responses(path, cases):
    rows, _ = read_jsonl(path)
    require(len(rows) == 24, 'response file must contain all 24 cases, including not_run/error placeholders')
    ids = [r.get('case_id') for r in rows]
    require(len(set(ids)) == 24 and set(ids) == set(IDS), 'response case IDs are missing, duplicated, or unknown')
    case_map = {r['id']:r for r in cases}
    fields = {'case_id','attempt','status','collected_at_utc','raw_output','error','truncated','grading'}
    for row in rows:
        ident = row['case_id']
        require(set(row) == fields, f'{ident}: response fields differ from template')
        require(type(row['attempt']) is int and row['attempt'] >= 1, f'{ident}: attempt must be a positive integer')
        require(row['status'] in {'not_run','completed','error'}, f'{ident}: invalid response status')
        require(row['collected_at_utc'] is None or isinstance(row['collected_at_utc'], str), f'{ident}: collection time must be a string or null')
        require(row['truncated'] is None or type(row['truncated']) is bool, f'{ident}: truncated must be boolean or null')
        if row['status'] == 'completed':
            require(isinstance(row['raw_output'], str), f'{ident}: completed output must be a string, including an empty string if returned')
            require(row['error'] is None, f'{ident}: completed response cannot have an infrastructure error')
        else:
            require(row['raw_output'] is None, f'{ident}: output must be null unless completed')
            require(row['grading'] is None, f'{ident}: only completed responses can be graded')
            if row['status'] == 'error':
                require(isinstance(row['error'], str) and bool(row['error'].strip()), f'{ident}: error description is required')
            else:
                require(row['error'] is None, f'{ident}: not_run case cannot have an error')
        grade = row['grading']
        if grade is not None:
            require(isinstance(grade, dict) and set(grade) == {'outcome','reviewer','checks','notes'}, f'{ident}: invalid grading fields')
            require(grade['outcome'] in OUTCOMES, f'{ident}: invalid grading outcome')
            require(isinstance(grade['reviewer'], str) and bool(grade['reviewer'].strip()), f'{ident}: reviewer must be recorded')
            require(isinstance(grade['notes'], str), f'{ident}: grading notes must be a string')
            require(isinstance(grade['checks'], dict), f'{ident}: checks must be an object')
            spec = case_map[ident]['expected_or_rubric']
            wanted = {c['id'] for c in spec['checks']} if spec['type']=='checklist' else {'comparison'}
            require(set(grade['checks']) == wanted, f'{ident}: checks must match this case specification')
            require(all(v in CHECKS for v in grade['checks'].values()), f'{ident}: invalid check outcome')
            if grade['outcome'] == 'pass':
                require(all(v == 'pass' for v in grade['checks'].values()), f'{ident}: pass outcome requires every check to pass')
            elif grade['outcome'] == 'fail':
                require('fail' in grade['checks'].values(), f'{ident}: fail outcome requires a failed check')
            elif grade['outcome'] == 'needs_review':
                require('needs_review' in grade['checks'].values(), f'{ident}: needs_review outcome requires an unresolved check')
    return Counter(r['status'] for r in rows)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--prompts', type=Path, default=ROOT/'prompts.jsonl')
    subs = parser.add_subparsers(dest='command', required=True)
    subs.add_parser('validate')
    subs.add_parser('init-run').add_argument('directory', type=Path)
    subs.add_parser('check-responses').add_argument('path', type=Path)
    args = parser.parse_args()
    try:
        rows, digest = validate_pack(args.prompts)
        if args.command == 'validate':
            print(f'Valid: 24 cases; 8 categories with 3 cases each. SHA-256: {digest}')
            print('No model has been called or scored by this command.')
        elif args.command == 'init-run':
            paths = init_run(args.directory, rows, digest)
            print(f'Created blank metadata and 24 not_run records in {paths[0].parent}')
            print('No model has been called or scored.')
        else:
            counts = check_responses(args.path, rows)
            print('Response structure valid. Status counts: '+json.dumps(dict(counts), sort_keys=True))
            print('Answer correctness has not been checked by this command.')
    except (ValueError, OSError, TypeError, KeyError) as exc:
        print(f'Validation error: {exc}', file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
