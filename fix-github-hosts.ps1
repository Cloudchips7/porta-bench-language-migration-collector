$ErrorActionPreference = "Stop"

$principal = New-Object Security.Principal.WindowsPrincipal([Security.Principal.WindowsIdentity]::GetCurrent())
$isAdmin = $principal.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
if (-not $isAdmin) {
    Write-Host "Please run this script in an Administrator PowerShell window." -ForegroundColor Yellow
    exit 1
}

$repoRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$logDir = Join-Path $repoRoot "logs"
if (-not (Test-Path $logDir)) {
    New-Item -ItemType Directory -Path $logDir | Out-Null
}

$hostsPath = "C:\Windows\System32\drivers\etc\hosts"
$timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
$backupPath = Join-Path $logDir "hosts_backup_$timestamp.txt"
Copy-Item -LiteralPath $hostsPath -Destination $backupPath -Force

$item = Get-Item -LiteralPath $hostsPath
if ($item.IsReadOnly) {
    attrib -r $hostsPath
}

$githubDomains = @(
    "api.github.com",
    "education.github.com",
    "resources.github.com",
    "uploads.github.com",
    "archiveprogram.github.com",
    "raw.github.com",
    "githubusercontent.com",
    "raw.githubusercontent.com",
    "camo.githubusercontent.com",
    "cloud.githubusercontent.com",
    "avatars.githubusercontent.com",
    "avatars0.githubusercontent.com",
    "avatars1.githubusercontent.com",
    "avatars2.githubusercontent.com",
    "avatars3.githubusercontent.com",
    "user-images.githubusercontent.com",
    "objects.githubusercontent.com",
    "private-user-images.githubusercontent.com",
    "github.com",
    "pages.github.com",
    "gist.github.com",
    "githubapp.com",
    "github.githubassets.com",
    "support-assets.githubassets.com",
    "github.io",
    "www.github.io"
)

$pattern = '^127\.0\.0\.1\s+(' + (($githubDomains | ForEach-Object { [regex]::Escape($_) }) -join '|') + ')$'
$content = Get-Content -LiteralPath $hostsPath
$updated = foreach ($line in $content) {
    $trimmed = $line.Trim()
    if ($trimmed -match $pattern) {
        "# DISABLED_BY_CODEX $line"
    } else {
        $line
    }
}

Set-Content -LiteralPath $hostsPath -Value $updated -Encoding ASCII
ipconfig /flushdns | Out-Host

Write-Host ""
Write-Host "GitHub-related hosts overrides have been disabled." -ForegroundColor Green
Write-Host "Backup file: $backupPath"
Write-Host ""
Write-Host "Recommended next checks:"
Write-Host "  1. Resolve-DnsName github.com"
Write-Host "  2. git clone https://github.com/octocat/Hello-World.git"
Write-Host "  3. rerun: python `"需求文档/download_repo.py`" --stage enrich --subtype py2_py3"
