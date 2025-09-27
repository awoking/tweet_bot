import os

print("=== 環境変数テスト ===")
required_vars = [
    "TWITTER_API_KEY",
    "TWITTER_API_SECRET", 
    "TWITTER_ACCESS_TOKEN",
    "TWITTER_ACCESS_TOKEN_SECRET",
    "TWITTER_BEARER_TOKEN"
]

all_set = True
for var in required_vars:
    value = os.getenv(var)
    if value:
        # 最初の5文字だけ表示（セキュリティのため）
        masked_value = value[:5] + "*" * (len(value) - 5)
        print(f"✅ {var}: {masked_value}")
    else:
        print(f"❌ {var}: 未設定")
        all_set = False

if all_set:
    print("\n🎉 すべての環境変数が設定されています！")
else:
    print("\n⚠️ 一部の環境変数が未設定です")