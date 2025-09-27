import tweepy 
import os
import ephem
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

# 日本（東京）の日の出・日没時刻を計算する関数
def get_sun_times():
    """東京の日の出・日没時刻を取得する"""
    try:
        # 東京の緯度・経度
        tokyo = ephem.Observer()
        tokyo.lat = '35.6762'  # 東京の緯度
        tokyo.lon = '139.6503' # 東京の経度
        tokyo.elevation = 0
        
        # 日本時間で今日の日付を取得
        from datetime import timedelta
        japan_now = datetime.utcnow() + timedelta(hours=9)
        tokyo.date = japan_now.strftime('%Y/%m/%d 00:00:00')
        
        # 太陽オブジェクト
        sun = ephem.Sun()
        
        # 今日の日の出・日没を計算
        sunrise_utc = tokyo.next_rising(sun)
        sunset_utc = tokyo.next_setting(sun)
        
        # UTC+9（日本時間）に変換
        sunrise_jst = sunrise_utc.datetime() + timedelta(hours=9)
        sunset_jst = sunset_utc.datetime() + timedelta(hours=9)
        
        return sunrise_jst.strftime("%H:%M"), sunset_jst.strftime("%H:%M")
    
    except Exception as e:
        print(f"⚠️ 日の出・日没計算エラー: {e}")
        # 9月末の東京の大体の時刻
        return "05:50", "17:30"
    
    except Exception as e:
        print(f"⚠️ 日の出・日没計算エラー: {e}")
        return "06:30", "18:00"  # デフォルト値

# 日本時間を取得する関数
def get_japan_time():
    """日本時間（UTC+9）を取得する"""
    from datetime import timedelta
    utc_now = datetime.utcnow()
    japan_time = utc_now + timedelta(hours=9)
    return japan_time

# 日の出・日没時刻を取得
sunrise_time, sunset_time = get_sun_times()

# 日本時間でシェルログ風ツイートメッセージを作成
japan_now = get_japan_time()
date_str = japan_now.strftime("%Y-%m-%d")
time_str = japan_now.strftime("%H:%M:%S")
day_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"][japan_now.weekday()]

# シェルプロンプト風のメッセージ
tweet_text = f"""$ Hello,world! {date_str} {time_str} JST

sunrise: {sunrise_time}"""

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
