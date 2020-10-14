import json
import requests
import time
import psutil


def main():
    address_server = "http://localhost:8000/"
    while True:
        time.sleep(9)
        data = {
            'data': str(psutil.cpu_percent(interval=1))
        }
        r = requests.post(
            url=address_server,
            data=data,
        )
        respons = json.loads(r.text)
        print(respons['data'])


if __name__ == '__main__':
    main()