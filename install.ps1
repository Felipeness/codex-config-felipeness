param(
    [switch]$Force
)

$ErrorActionPreference = 'Stop'
$RootDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$Installer = Join-Path $RootDir 'scripts/install.py'
$InstallerArgs = @()
if ($Force) {
    $InstallerArgs += '--force'
}
$InstallerArgs += $args
& py -3.11 $Installer @InstallerArgs
if ($LASTEXITCODE -ne 0) {
    exit $LASTEXITCODE
}
