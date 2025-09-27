# Twitter Bot - Cloud Deploy

自動ツイート投稿用のシンプルなTwitterボットです。

## クラウドデプロイ
私はcloudflare コンピューティングにデプロイしました。

1. とりあえず私のリポジトリを登録してください。
2. デプロイコマンドは適当に 
```bash 
pip install -r requirements.txt 
```
3. ビルドコマンドも適当に
```bash 
python3 tweet_bot.py
```
4. そしたら多分一回目はAPI鍵が無いから失敗します。
5. 設定にいって変数とシークレットのとこで自分のAPI鍵を入れてください。
6. たぶんできるはず。

### 環境変数設定
デプロイ先のプラットフォームで以下の環境変数を設定してください：

```
TWITTER_API_KEY=your_api_key_here
TWITTER_API_SECRET=your_api_secret_here
TWITTER_ACCESS_TOKEN=your_access_token_here
TWITTER_ACCESS_TOKEN_SECRET=your_access_token_secret_here
TWITTER_BEARER_TOKEN=your_bearer_token_here
```

## ローカル開発

```bash
git clone https://github.com/awoking/tweet_bot.git
cd tweet_bot
pip install -r requirements.txt

# 環境変数を設定してから実行
python tweet_bot.py
```

## ファイル構成

- `tweet_bot.py` - メインプログラム
- `requirements.txt` - 依存パッケージ

## Twitter API設定

1. [Twitter Developer Portal](https://developer.twitter.com/)
2. アプリケーション作成
3. API Keys and Tokens から認証情報取得
4. 環境変数として設定

以上