import tweepy 
import os
from dotenv import load_dotenv
from datetime import datetime
import random

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
    exit(1)

# Tweepy クライアントの初期化
client = tweepy.Client(
    consumer_key=API_KEY,
    consumer_secret=API_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET,
    bearer_token=BEARER_TOKEN
)

# ランダムなツイートメッセージのリスト
messages = [
    "今日も一日お疲れさまでした！",
    "プログラミング楽しい！",
    "Python最高！",
    "今日の作業完了！",
    "コーディング中です〜",
    "新機能を開発中！",
    "デバッグ作業頑張ってます",
    "今日も学習継続中"
]

# ランダムなメッセージと時刻を組み合わせ
current_time = datetime.now().strftime("%H:%M")
random_message = random.choice(messages)
tweet_text = f"{random_message} ({current_time}) #PythonBot"

# ツイート投稿
try:
    response = client.create_tweet(text=tweet_text)
    print("ツイートが正常に投稿されました！")
    print(f"ツイート内容: {tweet_text}")
    print(f"ツイートID: {response.data['id']}")
except Exception as e:
    print(f"エラーが発生しました: {e}")
    if "duplicate" in str(e).lower():
        print("重複エラーの場合は、しばらく待ってから再実行してください。")