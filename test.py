import requests
import certifi


def test() -> None:
    proxies: dict[str, str] = {
        "http": "",
        "https": ""
    }

    try:
        requests.get("https://example.com", verify=certifi.where(), proxies=proxies)
        print("Success")
    except requests.exceptions.SSLError as err:
        print(err)
    except Exception as err:
        print(err)

if __name__ == '__main__':
    test()