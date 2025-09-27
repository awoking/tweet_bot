# Azure Container Instances デプロイスクリプト
param(
    [string]$ResourceGroup = "twitter-bot-rg",
    [string]$ContainerName = "twitter-bot",
    [string]$Location = "eastus"
)

Write-Host "=== Azure Container Instances Deploy Script ===" -ForegroundColor Green

# Azure CLIの確認
if (-not (Get-Command az -ErrorAction SilentlyContinue)) {
    Write-Error "Azure CLI not found. Please install Azure CLI."
    exit 1
}

try {
    # ログイン確認
    Write-Host "Checking Azure login..." -ForegroundColor Blue
    az account show

    # リソースグループの作成
    Write-Host "Creating resource group: $ResourceGroup" -ForegroundColor Blue
    az group create --name $ResourceGroup --location $Location

    # Container Registryの作成（オプション）
    $registryName = "${ContainerName}registry" -replace "[^a-zA-Z0-9]", ""
    Write-Host "Creating Azure Container Registry: $registryName" -ForegroundColor Blue
    az acr create --resource-group $ResourceGroup --name $registryName --sku Basic --admin-enabled true

    # イメージをビルドしてプッシュ
    Write-Host "Building and pushing image..." -ForegroundColor Blue
    az acr build --registry $registryName --image "${ContainerName}:latest" .

    # Container Instancesにデプロイ
    Write-Host "Deploying to Azure Container Instances..." -ForegroundColor Blue
    az container create `
        --resource-group $ResourceGroup `
        --name $ContainerName `
        --image "${registryName}.azurecr.io/${ContainerName}:latest" `
        --registry-login-server "${registryName}.azurecr.io" `
        --registry-username $registryName `
        --registry-password (az acr credential show --name $registryName --query "passwords[0].value" -o tsv) `
        --environment-variables "TWITTER_API_KEY=$env:TWITTER_API_KEY" "TWITTER_API_SECRET=$env:TWITTER_API_SECRET" "TWITTER_ACCESS_TOKEN=$env:TWITTER_ACCESS_TOKEN" "TWITTER_ACCESS_TOKEN_SECRET=$env:TWITTER_ACCESS_TOKEN_SECRET" "TWITTER_BEARER_TOKEN=$env:TWITTER_BEARER_TOKEN" `
        --restart-policy OnFailure

    Write-Host "✅ Deployment successful!" -ForegroundColor Green
}
catch {
    Write-Error "❌ Deployment failed: $_"
    exit 1
}