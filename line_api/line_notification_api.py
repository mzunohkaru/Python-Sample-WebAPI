from dotenv import load_dotenv
import os
import requests


load_dotenv()

# LINE_NOTIFY_TOKEN = os.getenv("LINE_API_KEY")
LINE_NOTIFY_TOKEN = "API KEY"

URL = "https://notify-api.line.me/api/notify"


def notify_message(message: str):
    headers = {
        "Authorization": f"Bearer {LINE_NOTIFY_TOKEN}",
        # フォームデータがURLエンコードされた形式で送信されることを設定
        # この形式は、HTMLフォームがデータをサーバーに送信する際に一般的に使用されるもの
        # キーと値のペアが&で区切られ、スペースは+または%20でエンコードされる
        "Content-Type": "application/x-www-form-urlencoded",
        # フォームデータが複数の部分（パート）に分割されて送信されることを設定
        # この形式は、テキストデータだけでなくファイルや大量のデータを送信する場合に使用されるもの
        # "Content-Type": "multipart/form-data",
    }

    data = {"message": message}

    res = requests.post(URL, headers=headers, data=data)
    print(res.status_code)


message = "Line API---"

if __name__ == "__main__":
    notify_message(message)
