import csv
import io


def validate_csv(content, required_cols, max_rows=10000):
    reader = csv.DictReader(io.StringIO(content))
    missing = set(required_cols) - set(reader.fieldnames or [])
    if missing:
        return {'ok': False, 'errors': ['missing columns: ' + str(missing)]}
    errors, count = [], 0
    for i, row in enumerate(reader):
        count += 1
        if count > max_rows:
            errors.append('row ' + str(i + 1) + ': exceeds max_rows')
            break
    return {'ok': len(errors) == 0, 'rows': count, 'errors': errors}
