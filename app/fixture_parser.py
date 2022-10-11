import argparse, csv, json
from pathlib import Path


def get_fixture_field(obj, id, model):
    id_value = obj[id]
    obj.pop(id, None)
    return {
        "model": model,
        "pk": id_value,
        "fields": obj
    }


def main(csv_file, model, json_file, id):
    investors_file = csv.DictReader(open(csv_file, 'r', encoding='utf-8'))
    fixture = [get_fixture_field(x, id, model) for x in investors_file]
    with open(json_file, 'w') as file:
        json.dump(fixture, file)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Parse plain csv file to json fixture')
    parser.add_argument('csv_file', type=str, help='csv file to convert')
    parser.add_argument('model', type=str, help='django model to apply')
    parser.add_argument('-json_file', type=str, help='destination json file (default: same file name as csv)')
    parser.add_argument('-id', type=str, help='id / primary key of row (default: id)', default='id')
    args = parser.parse_args()

    model = f'{args.model}.{args.model}'
    json_file = args.json_file or "." + args.csv_file.split('.')[-2].replace('\\', '/') + ".json"

    main(args.csv_file, model, json_file, args.id)

