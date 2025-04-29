import os
from ablesci import ablesci

def main() -> None:
    cookie = os.getenv("ABLESCI_COOKIE")
    if not cookie:
        raise RuntimeError("环境变量 ABLESCI_COOKIE 未设置")
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cookie": cookie,          # 直接塞进请求头
        "DNT": "1",
        "Referer": "https://www.ablesci.com/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/112.0.0.0 Safari/537.36"
        ),
        "X-Requested-With": "XMLHttpRequest",
    }
    ablesci(headers=headers)

if __name__ == "__main__":
    main()
