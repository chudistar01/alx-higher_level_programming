#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status"""
import request
import sys


if __name__ == "__main__":
    url = sys.arg[1]

    r = requests.get(url)
    print(r.headers.get("X-Request-Id"))
