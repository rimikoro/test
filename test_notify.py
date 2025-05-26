import requests
import os

WEBHOOK_URL = os.environ["DISCORD_WEBHOOK_URL"]
livedoor_URL = "https://weather.tsukumijima.net/api/forecast/city/130010" # 東京を選択
weather = requests.get(livedoor_URL).json() # 天気を取得してjsonに整形する

# 最大の降水確率を算出
probability = max([int(probabilitys[:-1]) for probabilitys in weather['forecasts'][0]['chanceOfRain'].values() if not probabilitys == "--%"])
message = f"今日の最大降水確率は{probability}%です"

# Discordにメッセージを送信
requests.post(WEBHOOK_URL, json={"content": message})
