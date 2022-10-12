import requests
import argparse


def create_bills():
    response = requests.post("http://localhost:8000/api/bills/create-all/")
    print(response.json())


def create_cashcall(investor_id):
    response = requests.post(
        f"http://localhost:8000/api/cashcalls/create/{investor_id}")
    print(response.json())


def update_cashcall(cashcall_id, status):
    response = requests.put(
        f"http://localhost:8000/api/cashcalls/{cashcall_id}/status", json={"invoice_status": status})
    print(response.json())


def main():
    response = requests.post(
        "http://localhost:8000/api/", json={"test": "asdf"})
    print(response.json())


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Basic client for the API')
    parser.add_argument('action', type=str,
                        help='action to execute (available: create-bills, create-cashcall, update-cashcall, e2e)')
    parser.add_argument('-investor_id', type=str,
                        help='(create-cashcall) id of investor to create cashcalls for')
    parser.add_argument('-cashcall_id', type=str,
                        help='(update-cashcall) id of cashcall to edit')
    parser.add_argument('-status', type=str,
                        help='(update-cashcall) new status of cashcall')
    args = parser.parse_args()

    if args.action == 'create-bills':
        create_bills()

    elif args.action == 'create-cashcall':
        if not args.investor_id:
            raise Exception(f'-investor_id must be specified for this action')
        create_cashcall(args.investor_id)

    elif args.action == 'update-cashcall':
        if not args.cashcall_id:
            raise Exception(f'-cashcall_id must be specified for this action')
        if not args.status:
            raise Exception(f'-status must be specified for this action')
        update_cashcall(args.cashcall_id, args.status)

    elif args.action == 'e2e':
        """
        Tests all required functions with some default data
        """
        create_bills()
        create_cashcall(1)
        create_cashcall(2)
        create_cashcall(3)
        update_cashcall(1, 'sent')
        update_cashcall(1, 'should_fail')

    else:
        main()
