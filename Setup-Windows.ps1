$ErrorActionPreference = "Stop"

Write-Host "Hamrick Knowledge Vault setup" -ForegroundColor Cyan

if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
    Write-Host "Git is not installed. Install Git for Windows, then run this script again." -ForegroundColor Yellow
    exit 1
}

$vaultPath = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $vaultPath

if (-not (Test-Path ".git")) {
    git init
    git branch -M main
}

git add .
git commit -m "Initialize Obsidian knowledge vault" 2>$null
if ($LASTEXITCODE -ne 0) {
    Write-Host "No new commit was created, or Git identity is not configured." -ForegroundColor Yellow
    Write-Host 'Configure it with: git config --global user.name "Your Name"'
    Write-Host 'and: git config --global user.email "you@example.com"'
}

Write-Host ""
Write-Host "Next, create a PRIVATE empty GitHub repository named hamrick-knowledge-vault." -ForegroundColor Green
Write-Host "Then run:"
Write-Host "git remote add origin https://github.com/Hamrix/hamrick-knowledge-vault.git"
Write-Host "git push -u origin main"
Write-Host ""
Write-Host "Open this folder as an Obsidian vault:"
Write-Host $vaultPath
