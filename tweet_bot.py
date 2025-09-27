import tweepy 
import os
from dotenv import load_dotenv
from datetime import datetime

# .envファイルを読み込み
load_dotenv()

# 環境変数から認証情報を取得
API_KEY = os.getenv("TWITTER_API_KEY")
API_SECRET = os.getenv("TWITTER_API_SECRET")
ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")

# 認証情報の確認
if not all([API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET]):
    print("エラー: .envファイルにAPIキーが正しく設定されていません")
    print("以下の環境変数を確認してください:")
    print("- TWITTER_API_KEY")
    print("- TWITTER_API_SECRET") 
    print("- TWITTER_ACCESS_TOKEN")
    print("- TWITTER_ACCESS_TOKEN_SECRET")
    exit(1)

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
    print("ツイートが正常に投稿されました！")
    print(f"ツイート内容: {tweet_text}")
    print(f"ツイートID: {response.data['id']}")
except Exception as e:
    print(f"エラーが発生しました: {e}")
