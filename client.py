import requests


def main():
    response = requests.get("http://localhost:8000/api/", json={"test":"asdf"})
    print(response.json())

if __name__ == "__main__":
    main()