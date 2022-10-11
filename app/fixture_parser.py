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
    csv_path = Path(csv_file)
    csv_file = open(csv_path, 'r', encoding='utf-8')
    csv_dict = csv.DictReader(csv_file)
    fixture = [get_fixture_field(x, id, model) for x in csv_dict]

    json_path = Path(json_file)
    json_path.write_text(json.dumps(fixture))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Parse plain csv file to json fixture')
    parser.add_argument('app', type=str, help='will look for csv inside fixture folder of this drf app (name also used for model & output json file)')
    parser.add_argument('-id', type=str, help='id / primary key of row (default: id)', default='id')
    args = parser.parse_args()

    app = args.app
    model = f'{app}.{app}'
    csv_file = f'{app}/fixtures/{app}.csv'
    json_file = f'{app}/fixtures/{app}.json'

    main(csv_file, model, json_file, args.id)

