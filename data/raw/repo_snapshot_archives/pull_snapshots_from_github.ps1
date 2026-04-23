param(
    [switch]$All,
    [string]$Subtype = "",
    [string]$InstanceId = "",
    [int]$Limit = 0,
    [switch]$Force,
    [switch]$BuildList,
    [switch]$GitPull,
    [switch]$UseClashProxy = $true
)

$ErrorActionPreference = "Stop"

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$projectRoot = Resolve-Path (Join-Path $scriptDir "..\..\..")
Set-Location $projectRoot

if ($UseClashProxy) {
    $env:http_proxy = "http://127.0.0.1:7897"
    $env:https_proxy = "http://127.0.0.1:7897"
    $env:HTTP_PROXY = "http://127.0.0.1:7897"
    $env:HTTPS_PROXY = "http://127.0.0.1:7897"
}

if ($GitPull) {
    Write-Host "Running git pull origin main..." -ForegroundColor Cyan
    git pull origin main
}

$pythonScript = Join-Path $scriptDir "pull_snapshots_from_github.py"
$argsList = @($pythonScript)

if ($BuildList) {
    $argsList += "--build-list"
} else {
    if ($All) {
        $argsList += "--all"
    }
    if ($Subtype) {
        $argsList += "--subtype"
        $argsList += $Subtype
    }
    if ($InstanceId) {
        $argsList += "--instance-id"
        $argsList += $InstanceId
    }
    if ($Limit -gt 0) {
        $argsList += "--limit"
        $argsList += "$Limit"
    }
    if ($Force) {
        $argsList += "--force"
    }
    if (-not $All -and -not $Subtype -and -not $InstanceId) {
        Write-Host "No selector provided, defaulting to --all" -ForegroundColor Yellow
        $argsList += "--all"
    }
}

python @argsList
