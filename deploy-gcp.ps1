# Google Cloud Run デプロイスクリプト
param(
    [string]$ProjectId = "your-gcp-project-id",
    [string]$ServiceName = "twitter-bot",
    [string]$Region = "us-central1"
)

Write-Host "=== Google Cloud Run Deploy Script ===" -ForegroundColor Green

# gcloudコマンドの確認
if (-not (Get-Command gcloud -ErrorAction SilentlyContinue)) {
    Write-Error "Google Cloud SDK not found. Please install gcloud CLI."
    exit 1
}

try {
    # プロジェクトを設定
    Write-Host "Setting project: $ProjectId" -ForegroundColor Blue
    gcloud config set project $ProjectId

    # Container Registryにイメージをプッシュ
    Write-Host "Building and pushing to Container Registry..." -ForegroundColor Blue
    $imageUri = "gcr.io/${ProjectId}/${ServiceName}:latest"
    
    docker build -t $imageUri .
    docker push $imageUri

    # Cloud Runにデプロイ
    Write-Host "Deploying to Cloud Run..." -ForegroundColor Blue
    gcloud run deploy $ServiceName `
        --image $imageUri `
        --platform managed `
        --region $Region `
        --allow-unauthenticated `
        --set-env-vars "TWITTER_API_KEY=$env:TWITTER_API_KEY,TWITTER_API_SECRET=$env:TWITTER_API_SECRET,TWITTER_ACCESS_TOKEN=$env:TWITTER_ACCESS_TOKEN,TWITTER_ACCESS_TOKEN_SECRET=$env:TWITTER_ACCESS_TOKEN_SECRET,TWITTER_BEARER_TOKEN=$env:TWITTER_BEARER_TOKEN"

    Write-Host "✅ Deployment successful!" -ForegroundColor Green
}
catch {
    Write-Error "❌ Deployment failed: $_"
    exit 1
}