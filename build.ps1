# ビルドスクリプト for Windows PowerShell
param(
    [string]$ImageName = "tweet-bot",
    [string]$Tag = "latest"
)

Write-Host "=== Twitter Bot Build Script ===" -ForegroundColor Green
Write-Host "Building Docker image: $ImageName:$Tag" -ForegroundColor Yellow

# Dockerfileが存在することを確認
if (-not (Test-Path "Dockerfile")) {
    Write-Error "Dockerfile not found in current directory"
    exit 1
}

# requirements.txtが存在することを確認
if (-not (Test-Path "requirements.txt")) {
    Write-Error "requirements.txt not found in current directory"
    exit 1
}

# tweet_bot.pyが存在することを確認
if (-not (Test-Path "tweet_bot.py")) {
    Write-Error "tweet_bot.py not found in current directory"
    exit 1
}

# .envファイルの確認（警告のみ）
if (-not (Test-Path ".env")) {
    Write-Warning ".env file not found. Make sure to set environment variables in your cloud platform."
}

try {
    # Dockerイメージをビルド
    Write-Host "Starting Docker build..." -ForegroundColor Blue
    docker build -t "${ImageName}:${Tag}" .
    
    if ($LASTEXITCODE -eq 0) {
        Write-Host "✅ Build successful!" -ForegroundColor Green
        Write-Host "Image created: ${ImageName}:${Tag}" -ForegroundColor Green
        
        # イメージ情報を表示
        Write-Host "`n=== Image Information ===" -ForegroundColor Yellow
        docker images | Select-String $ImageName
        
        Write-Host "`n=== Next Steps ===" -ForegroundColor Cyan
        Write-Host "Local run: docker run --env-file .env ${ImageName}:${Tag}"
        Write-Host "Push to registry: docker push your-registry/${ImageName}:${Tag}"
    } else {
        Write-Error "❌ Build failed with exit code $LASTEXITCODE"
        exit 1
    }
}
catch {
    Write-Error "❌ Build failed: $_"
    exit 1
}