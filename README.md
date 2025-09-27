# Twitter Bot - Cloud Deployment

このTwitter botをクラウドにデプロイする手順です。

## 前提条件

- Docker がインストールされていること
- Twitter API キーが取得済みであること
- `.env` ファイルが設定済みであること

## クイックスタート

### ローカルでテスト
```powershell
# ビルド
.\build.ps1

# ローカル実行
.\deploy.ps1 -Platform local
```

### 本番デプロイ

#### Google Cloud Platform
```powershell
# GCP CLIインストール後
.\deploy-gcp.ps1 -ProjectId your-project-id
```

#### AWS
```powershell
# ECRにプッシュ
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin YOUR_ECR_URI
docker tag tweet-bot:latest YOUR_ECR_URI/tweet-bot:latest
docker push YOUR_ECR_URI/tweet-bot:latest

# ECSタスク定義の更新
aws ecs register-task-definition --cli-input-json file://aws-task-definition.json
```

#### Azure
```powershell
# Azure CLIインストール後
az login
.\deploy-azure.ps1
```

## ファイル説明

- `build.ps1` - Dockerイメージビルドスクリプト
- `deploy.ps1` - 統合デプロイスクリプト
- `Dockerfile` - Dockerイメージ設定
- `docker-compose.yml` - ローカル実行用
- `requirements.txt` - Python依存関係
- `aws-task-definition.json` - AWS ECS設定
- `deploy-gcp.ps1` - Google Cloud Run用
- `deploy-azure.ps1` - Azure Container Instances用

## 環境変数

以下の環境変数を設定してください：

- `TWITTER_API_KEY`
- `TWITTER_API_SECRET`
- `TWITTER_ACCESS_TOKEN`
- `TWITTER_ACCESS_TOKEN_SECRET`
- `TWITTER_BEARER_TOKEN`

## スケジュール実行

各クラウドプラットフォームでのスケジュール実行：

### AWS
- CloudWatch Events + ECS タスク

### GCP
- Cloud Scheduler + Cloud Run

### Azure
- Logic Apps または Azure Functions

## トラブルシューティング

### よくある問題
1. **API認証エラー**: `.env`ファイルのキーを確認
2. **重複ツイートエラー**: 時間間隔を空けるか、ツイート内容を変更
3. **Docker build失敗**: `requirements.txt`と`tweet_bot.py`の存在確認

### ログ確認
```powershell
# ローカル
docker-compose logs -f

# クラウド
# 各プラットフォームのログビューワーを使用
```