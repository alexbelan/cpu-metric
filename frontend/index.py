import json
import requests
import time
import psutil
import stun


def main():
    address_server = "http://localhost:8000/"
    ip = stun.get_ip_info()[1]
    while True:
        time.sleep(9)
        data = {
            'ip': str(ip),
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