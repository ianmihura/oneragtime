import requests, argparse


def create_all():
    response = requests.post("http://localhost:8000/api/bills/create-all/")
    print(response.json())


def main():
    response = requests.post("http://localhost:8000/api/bills/create-all/", json={"test":"asdf"})
    print(response.json())


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Basic client for the API')
    parser.add_argument('command', type=str, help='command to execute (example: create-all)')
    args = parser.parse_args()

    if args.command == 'create-all':
        create_all()
    else:
        main()