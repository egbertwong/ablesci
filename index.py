import os
import datetime as dt

import pytz
from ablesci import ablesci
from serverchan_sdk import sc_send


def main() -> None:
    cookie = os.getenv("ABLESCI_COOKIE", "").strip()
    sendkey = os.getenv("SERVERCHAN_SENDKEY", "").strip()
    if not cookie:
        raise RuntimeError("环境变量 ABLESCI_COOKIE 未设置")

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

    status_code, body = ablesci(headers)  # ← 新 ablesci 返回 (code, json)
    if not isinstance(body, dict):
        body = {"code": -1, "msg": "接口返回异常，无法解析 JSON"}

    msg = body.get("msg", "未返回 msg")
    flag = "成功" if body.get("code") == 0 else "失败"

    # ————— 组织推送内容 —————
    now = dt.datetime.now(pytz.timezone("Asia/Shanghai")).strftime("%Y-%m-%d %H:%M:%S")
    title = f"科研通签到{flag} · {now}"
    desp = msg

    print("签到返回：", body)

    if sendkey:
        resp = sc_send(sendkey, title, desp, {"tags": "科研通|签到提醒"})
        print("ServerChan 返回：", resp)
    else:
        print("未设置 SERVERCHAN_SENDKEY，跳过推送")


if __name__ == "__main__":
    main()
