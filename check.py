import requests
from bs4 import BeautifulSoup
import os

# Slack Webhook URL（後で設定）
SLACK_WEBHOOK = os.environ.get("SLACK_WEBHOOK")

# チェックするメールアドレス
TARGET = "info@men-esthe.jp"

url = "https://m.kuku.lu/recv.php"

res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")

text = soup.get_text()

requests.post(SLACK_WEBHOOK, json={
    "text": "テスト通知"
})
