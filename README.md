# Twitter Bot - Cloud Deploy

自動ツイート投稿用のシンプルなTwitterボットです。

## クラウドデプロイ

### 環境変数設定
デプロイ先のプラットフォームで以下の環境変数を設定してください：

```
TWITTER_API_KEY=your_api_key_here
TWITTER_API_SECRET=your_api_secret_here
TWITTER_ACCESS_TOKEN=your_access_token_here
TWITTER_ACCESS_TOKEN_SECRET=your_access_token_secret_here
TWITTER_BEARER_TOKEN=your_bearer_token_here
```

### 対応プラットフォーム

#### Cloudflare Pages
1. プロジェクト → Settings → Environment variables
2. 上記5つの環境変数を追加
3. Production環境で実行

#### Heroku
```bash
heroku config:set TWITTER_API_KEY=your_key
heroku config:set TWITTER_API_SECRET=your_secret
# ... 他の変数も同様
```

#### Vercel
```bash
vercel env add TWITTER_API_KEY
# プロンプトで値を入力
```

#### Railway/Render
環境変数タブで上記変数を設定

## ローカル開発

```bash
git clone https://github.com/awoking/tweet_bot.git
cd tweet_bot
pip install -r requirements.txt

# 環境変数を設定してから実行
python tweet_bot.py
```

## 特徴

- ✅ 軽量設計（依存関係最小限）
- ✅ クラウドネイティブ（環境変数で設定）
- ✅ 重複ツイート防止（タイムスタンプ付き）
- ✅ エラーハンドリング付き
- ✅ Python 3.11+ 対応

## ファイル構成

- `tweet_bot.py` - メインプログラム
- `requirements.txt` - 依存パッケージ
- `wrangler.toml` - Cloudflare設定（オプション）

## Twitter API設定

1. [Twitter Developer Portal](https://developer.twitter.com/)
2. アプリケーション作成
3. API Keys and Tokens から認証情報取得
4. 環境変数として設定