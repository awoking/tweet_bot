# 統合デプロイスクリプト
param(
    [Parameter(Mandatory=$true)]
    [ValidateSet("local", "aws", "gcp", "azure")]
    [string]$Platform,
    
    [string]$ImageName = "tweet-bot",
    [string]$Tag = "latest"
)

Write-Host "=== Universal Deploy Script ===" -ForegroundColor Green
Write-Host "Platform: $Platform" -ForegroundColor Yellow

# 共通の前処理
function Test-Prerequisites {
    if (-not (Test-Path "tweet_bot.py")) {
        Write-Error "tweet_bot.py not found"
        return $false
    }
    
    if (-not (Test-Path ".env")) {
        Write-Warning ".env file not found. Environment variables must be set in the cloud platform."
    }
    
    if (-not (Get-Command docker -ErrorAction SilentlyContinue)) {
        Write-Error "Docker not found. Please install Docker."
        return $false
    }
    
    return $true
}

# 共通ビルド処理
function Build-Image {
    Write-Host "Building Docker image..." -ForegroundColor Blue
    docker build -t "${ImageName}:${Tag}" .
    
    if ($LASTEXITCODE -ne 0) {
        Write-Error "Docker build failed"
        return $false
    }
    
    Write-Host "✅ Image built successfully" -ForegroundColor Green
    return $true
}

# メイン処理
if (-not (Test-Prerequisites)) {
    exit 1
}

if (-not (Build-Image)) {
    exit 1
}

switch ($Platform) {
    "local" {
        Write-Host "Running locally with docker-compose..." -ForegroundColor Blue
        docker-compose up -d
        Write-Host "✅ Local deployment successful!" -ForegroundColor Green
        Write-Host "Check status: docker-compose ps" -ForegroundColor Cyan
        Write-Host "View logs: docker-compose logs -f" -ForegroundColor Cyan
    }
    
    "aws" {
        Write-Host "For AWS deployment, please:" -ForegroundColor Yellow
        Write-Host "1. Push image to ECR" -ForegroundColor White
        Write-Host "2. Update aws-task-definition.json with your values" -ForegroundColor White
        Write-Host "3. Create ECS service" -ForegroundColor White
    }
    
    "gcp" {
        Write-Host "For GCP deployment, run:" -ForegroundColor Yellow
        Write-Host "./deploy-gcp.ps1 -ProjectId YOUR_PROJECT_ID" -ForegroundColor White
    }
    
    "azure" {
        Write-Host "For Azure deployment, run:" -ForegroundColor Yellow
        Write-Host "./deploy-azure.ps1 -ResourceGroup YOUR_RG" -ForegroundColor White
    }
}