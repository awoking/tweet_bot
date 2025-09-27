import tweepy 
import os
from datetime import datetime

# 環境変数から認証情報を取得（クラウド環境用）
BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")

# Bearer Token の確認
if not BEARER_TOKEN:
    print("❌ TWITTER_BEARER_TOKEN が設定されていません")
    exit(1)

print("✅ Bearer Token設定OK - Twitter Bot起動中...")
print(f"🔍 BEARER_TOKEN: {BEARER_TOKEN[:20]}...")

# Bearer Token のみでクライアント初期化（読み取り専用）
try:
    client = tweepy.Client(bearer_token=BEARER_TOKEN)
    print("✅ Twitter APIクライアント初期化成功（Bearer Token）")
    
    # API接続テスト
    try:
        # 自分の情報取得（これは読み取り専用なのでBearer Tokenで可能）
        user = client.get_user(username="Twitter")  # Twitterの公式アカウント情報を取得してテスト
        print(f"📱 API接続テスト成功: {user.data.name}")
    except Exception as test_error:
        print(f"⚠️ API接続テストエラー: {test_error}")
        
except Exception as client_error:
    print(f"❌ クライアント初期化エラー: {client_error}")
    exit(1)

print("📝 注意: Bearer Tokenのみではツイート投稿はできません")
print("💡 ツイート投稿にはOAuth 1.0a認証（API Key/Secret + Access Token/Secret）が必要です")