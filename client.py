import requests
import argparse


def create_bills():
    response = requests.post("http://localhost:8000/api/bills/create-all/")
    print(response.json())


def create_cashcall(investor_id):
    response = requests.post(
        f"http://localhost:8000/api/cashcalls/create/{investor_id}")
    print(response.json())


def main():
    response = requests.post(
        "http://localhost:8000/api/", json={"test": "asdf"})
    print(response.json())


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Basic client for the API')
    parser.add_argument('action', type=str,
                        help='action to execute (example: create-bills)')
    parser.add_argument('-investor_id', type=str,
                        help='id of investor to create cashcall')
    args = parser.parse_args()

    if args.action == 'create-bills':
        create_bills()
    elif args.action == 'create-cashcall':
        if not args.investor_id:
            raise Exception(f'investor_id must be specified for this action')
        create_cashcall(args.investor_id)
    else:
        main()
