# Rename AVA to AVA globally
# This script replaces all occurrences of AVA with AVA across the project

$ErrorActionPreference = "Continue"

# Define replacement patterns
$replacements = @(
    @{Pattern = 'AVA'; Replacement = 'AVA'; CaseSensitive = $true},
    @{Pattern = 'AVA'; Replacement = 'AVA'; CaseSensitive = $true},
    @{Pattern = 'ava'; Replacement = 'ava'; CaseSensitive = $true}
)

# File extensions to process
$extensions = @('*.md', '*.py', '*.yml', '*.yaml', '*.json', '*.txt', '*.sh', '*.ps1', '*.js', '*.html', '*.css', '*.env', '*.example', '.gitignore', '.dockerignore')

# Directories to exclude
$excludeDirs = @('.git', '__pycache__', 'node_modules', 'venv', '.venv', 'data', 'logs')

Write-Host "Starting global rename: AVA -> AVA" -ForegroundColor Cyan
Write-Host ""

# Get all files recursively, excluding certain directories
$files = Get-ChildItem -Path . -Recurse -File | Where-Object {
    $file = $_
    $exclude = $false
    foreach ($dir in $excludeDirs) {
        if ($file.FullName -like "*\$dir\*") {
            $exclude = $true
            break
        }
    }
    
    if (-not $exclude) {
        $matchExt = $false
        foreach ($ext in $extensions) {
            if ($file.Name -like $ext -or $file.Name -eq '.gitignore' -or $file.Name -eq '.dockerignore') {
                $matchExt = $true
                break
            }
        }
        $matchExt
    } else {
        $false
    }
}

$totalFiles = $files.Count
$processedFiles = 0
$modifiedFiles = 0

Write-Host "Found $totalFiles files to process..." -ForegroundColor Yellow
Write-Host ""

foreach ($file in $files) {
    $processedFiles++
    $relativePath = $file.FullName.Replace((Get-Location).Path + '\', '')
    
    try {
        # Read file content
        $content = Get-Content -Path $file.FullName -Raw -ErrorAction Stop
        
        if ($null -eq $content) {
            continue
        }
        
        $originalContent = $content
        $modified = $false
        
        # Apply each replacement pattern
        foreach ($repl in $replacements) {
            if ($repl.CaseSensitive) {
                $newContent = $content -creplace $repl.Pattern, $repl.Replacement
            } else {
                $newContent = $content -replace $repl.Pattern, $repl.Replacement
            }
            
            if ($newContent -ne $content) {
                $content = $newContent
                $modified = $true
            }
        }
        
        # Write back if modified
        if ($modified) {
            Set-Content -Path $file.FullName -Value $content -NoNewline -ErrorAction Stop
            $modifiedFiles++
            Write-Host "[$processedFiles/$totalFiles] Modified: $relativePath" -ForegroundColor Green
        } else {
            Write-Host "[$processedFiles/$totalFiles] Skipped: $relativePath" -ForegroundColor Gray
        }
    }
    catch {
        Write-Host "[$processedFiles/$totalFiles] Error processing $relativePath : $_" -ForegroundColor Red
    }
}

Write-Host ""
Write-Host "================================================" -ForegroundColor Cyan
Write-Host "Rename complete!" -ForegroundColor Green
Write-Host "Processed: $processedFiles files" -ForegroundColor Yellow
Write-Host "Modified: $modifiedFiles files" -ForegroundColor Green
Write-Host "================================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Next steps:" -ForegroundColor Cyan
Write-Host "1. Rename the root directory from 'ava' to 'ava'" -ForegroundColor White
Write-Host "2. Rename docs/ava.jpg to docs/ava.jpg" -ForegroundColor White
Write-Host "3. Update any git remote URLs if needed" -ForegroundColor White
Write-Host "4. Review and test the changes" -ForegroundColor White
