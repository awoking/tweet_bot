import tweepy 
import os
from datetime import datetime

# 環境変数から認証情報を取得（クラウド環境用）
API_KEY = os.getenv("TWITTER_API_KEY")
API_SECRET = os.getenv("TWITTER_API_SECRET")
ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")

# 認証情報の確認
if not all([API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET]):
    print("❌ 環境変数設定エラー")
    print("� 設定状況:")
    print(f"TWITTER_API_KEY: {'✅' if API_KEY else '❌'}")
    print(f"TWITTER_API_SECRET: {'✅' if API_SECRET else '❌'}")
    print(f"TWITTER_ACCESS_TOKEN: {'✅' if ACCESS_TOKEN else '❌'}")
    print(f"TWITTER_ACCESS_TOKEN_SECRET: {'✅' if ACCESS_TOKEN_SECRET else '❌'}")
    print(f"TWITTER_BEARER_TOKEN: {'✅' if BEARER_TOKEN else '❌'}")
    exit(1)

print("✅ 環境変数設定OK - Twitter Bot起動中...")

# Tweepy クライアントの初期化
client = tweepy.Client(
    consumer_key=API_KEY,
    consumer_secret=API_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET,
    bearer_token=BEARER_TOKEN
)

# 現在時刻を含む一意のツイートを作成
current_time = datetime.now().strftime("%Y年%m月%d日 %H:%M:%S")
tweet_text = f"こんにちは！現在時刻: {current_time} #PythonBot"

# ツイート投稿
try:
    response = client.create_tweet(text=tweet_text)
    print("🎉 ツイート投稿成功!")
    print(f"📝 内容: {tweet_text}")
    print(f"🔗 ツイートID: {response.data['id']}")
except Exception as e:
    print(f"❌ ツイート投稿エラー: {e}")
    if "duplicate" in str(e).lower():
        print("💡 重複エラー: 同じ内容のツイートが既に存在します")
