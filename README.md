# Twitter Bot

シンプルなTwitterボットです。

## セットアップ

1. **依存関係のインストール**
```bash
pip install -r requirements.txt
```

2. **環境変数の設定**
`.env`ファイルに以下の内容を記入してください：
```
TWITTER_API_KEY=your_api_key_here
TWITTER_API_SECRET=your_api_secret_here
TWITTER_ACCESS_TOKEN=your_access_token_here
TWITTER_ACCESS_TOKEN_SECRET=your_access_token_secret_here
TWITTER_BEARER_TOKEN=your_bearer_token_here
```

## 実行

```bash
python tweet_bot.py
```

## ファイル構成

- `tweet_bot.py` - メインプログラム
- `.env` - API認証情報（非公開）
- `.gitignore` - Git除外設定
- `requirements.txt` - 依存パッケージ一覧

## 注意事項

- `.env`ファイルは公開リポジトリにはアップロードされません
- Twitter API v2を使用しています
- 重複ツイートエラーを避けるため、毎回異なる内容を投稿します