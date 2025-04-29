import requests


def ablesci(headers):
    """返回 (status_code, json/None)。"""
    url = "https://www.ablesci.com/user/sign"
    resp = requests.get(url, headers=headers, timeout=15)
    try:
        data = resp.json()
    except ValueError:
        data = None
    return resp.status_code, data
