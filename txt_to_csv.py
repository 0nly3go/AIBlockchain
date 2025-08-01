import csv
import json

# Update these filenames as needed
input_txt = 'transactions.txt'
output_csv = 'transactions.csv'

def jsonlines_to_csv(input_txt, output_csv):
    """
    Converts a JSON-lines (one JSON object per line) text file to CSV format.
    """
    with open(input_txt, 'r', encoding='utf-8') as infile:
        lines = [line.strip() for line in infile if line.strip()]
        data = [json.loads(line) for line in lines]
    if not data:
        print('No data found in input file.')
        return
    # Get all unique keys for header (in case some lines have missing fields)
    all_keys = set()
    for item in data:
        all_keys.update(item.keys())
    fieldnames = sorted(all_keys)
    with open(output_csv, 'w', newline='', encoding='utf-8') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        for item in data:
            writer.writerow(item)

if __name__ == '__main__':
    jsonlines_to_csv(input_txt, output_csv)
    print(f'Converted {input_txt} to {output_csv}')
