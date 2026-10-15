"""A synthetic classroom exercise; not orders, stock or hardware test records."""
import csv
import json
import re
from collections import Counter
from pathlib import Path


def summarize(rows):
    ids = [r['sample_id'] for r in rows]
    if len(set(ids)) != len(ids):
        raise ValueError('Duplicate sample_id: resolve the record grain first.')
    quantities = [r['stock_quantity'].strip() for r in rows]
    outcomes = [r['test_outcome'].strip().lower() for r in rows]
    if any(x not in ('', 'pass', 'fail') for x in outcomes):
        raise ValueError('Use a recorded pass/fail outcome or leave it missing.')
    observed = [x for x in outcomes if x]
    return {
        'scope': 'fictional teaching fixture only',
        'listing_rows': len(rows),
        'rows_by_family': dict(Counter(r['model_family'] for r in rows)),
        'title_word_faulty_rows': sum(bool(re.search(r'\bfaulty\b', r['item_title'], re.I)) for r in rows),
        'seller_declared_faulty_rows': sum(r['declared_condition'].strip().lower() == 'faulty' for r in rows),
        'stock_quantity_total': sum(int(x) for x in quantities) if quantities and all(x != '' for x in quantities) else None,
        'recorded_test_outcomes': len(observed),
        'missing_test_outcomes': len(rows) - len(observed),
        'failure_fraction_among_recorded_tests': observed.count('fail') / len(observed) if observed else None,
    }


if __name__ == '__main__':
    with Path(__file__).with_name('synthetic-listings.csv').open(encoding='utf8', newline='') as source:
        records = list(csv.DictReader(source))
    print(json.dumps(summarize(records), indent=2))
