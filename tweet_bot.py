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

# デバッグ: APIキーの最初の数文字を表示（セキュリティのため一部のみ）
print("🔍 認証情報チェック:")
print(f"API_KEY: {API_KEY[:8]}..." if API_KEY and len(API_KEY) > 8 else f"API_KEY: {API_KEY}")
print(f"API_SECRET: {API_SECRET[:8]}..." if API_SECRET and len(API_SECRET) > 8 else f"API_SECRET: {API_SECRET}")
print(f"ACCESS_TOKEN: {ACCESS_TOKEN[:15]}..." if ACCESS_TOKEN and len(ACCESS_TOKEN) > 15 else f"ACCESS_TOKEN: {ACCESS_TOKEN}")
print(f"ACCESS_TOKEN_SECRET: {ACCESS_TOKEN_SECRET[:8]}..." if ACCESS_TOKEN_SECRET and len(ACCESS_TOKEN_SECRET) > 8 else f"ACCESS_TOKEN_SECRET: {ACCESS_TOKEN_SECRET}")
print(f"BEARER_TOKEN: {BEARER_TOKEN[:8]}..." if BEARER_TOKEN and len(BEARER_TOKEN) > 8 else f"BEARER_TOKEN: {BEARER_TOKEN}")

# 重要: ACCESS_TOKENの検証
if ACCESS_TOKEN and not ACCESS_TOKEN.startswith("195157417084189"):
    print("🚨 警告: ACCESS_TOKENが正しくありません！")
    print("💡 正しいACCESS_TOKENは '1951574170841890817-' で始まるはずです")

if ACCESS_TOKEN_SECRET and ACCESS_TOKEN_SECRET == ACCESS_TOKEN:
    print("🚨 警告: ACCESS_TOKENとACCESS_TOKEN_SECRETが同じ値です！")
    print("💡 これらは異なる値である必要があります")

# Tweepy クライアントの初期化（v2 API用）
try:
    client = tweepy.Client(
        bearer_token=BEARER_TOKEN,
        consumer_key=API_KEY,
        consumer_secret=API_SECRET,
        access_token=ACCESS_TOKEN,
        access_token_secret=ACCESS_TOKEN_SECRET,
        wait_on_rate_limit=True
    )
    print("✅ Twitter APIクライアント初期化成功")
    
    # API接続テスト
    try:
        me = client.get_me()
        print(f"📱 認証済みユーザー: @{me.data.username}")
    except Exception as auth_test_error:
        print(f"⚠️ 認証テストエラー: {auth_test_error}")
        
except Exception as client_error:
    print(f"❌ クライアント初期化エラー: {client_error}")
    exit(1)

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
