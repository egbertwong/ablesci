import os
import datetime as dt
import json
from ablesci import ablesci
from serverchan_sdk import sc_send


def main() -> None:
    cookie = os.getenv("ABLESCI_COOKIE", "").strip()
    if not cookie:
        raise RuntimeError("环境变量 ABLESCI_COOKIE 未设置")
    sendkey = os.getenv("SERVERCHAN_SENDKEY", "").strip()

    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Cookie": cookie,
        "User-Agent": (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/112.0.0.0 Safari/537.36"
        ),
        "Referer": "https://www.ablesci.com/",
        "X-Requested-With": "XMLHttpRequest",
    }

    code, body = ablesci(headers)
    now = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    title = f"科研通签到 {'成功' if code == 200 else '失败'} · {now}"
    desp = json.dumps(body, ensure_ascii=False, indent=2)

    print(title)
    print(desp)

    # 只有设置了 SendKey 才推送
    if sendkey:
        resp = sc_send(sendkey, title, desp, {"tags": "科研通|签到提醒"})
        print("ServerChan 返回：", resp)
    else:
        print("未设置 SERVERCHAN_SENDKEY，跳过推送")


if __name__ == "__main__":
    main()
