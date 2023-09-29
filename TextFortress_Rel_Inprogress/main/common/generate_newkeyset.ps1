#Run this for the first time to generate the keys. 
$filePath = "C:\Users\HOME\Documents\GitHub\cody-lab\encryption\ProjectX\common\Decrypt_keys.txt"

# Check if the file already exists
if (Test-Path $filePath) {
    # Prompt the user to confirm whether they want to overwrite the file
    $overwrite = Read-Host "The file $filePath already exists. Do you want to overwrite it? (Y/N)"
    $overwrite = $overwrite.ToUpper()
    if ($overwrite -eq 'Y') {
        Write-Host "Overwriting will be deleting the existing set of decryption keys. This is an irreversible process"
        $overwrite_confirm= Read-Host "Do you want to proceed? (Y/N)"
        if ($overwrite_confirm -eq 'N') {
            Write-Host "Operation cancelled. The existing file has not been overwritten."
            exit
        }
    }
    if ($overwrite -eq 'N') {
        Write-Host "Operation cancelled. The existing file has not been overwritten."
        exit
    }
}
# To write the sequences to the file, overwriting it if necessary
Set-Content -Path $filePath -Value $sequence -Force

# Generate and write 8-character alpha-numeric sequences to the file
for ($i = 1; $i -le 7; $i++) {
    # Generate a random sequence containing letters and numbers
    $sequence = Get-Random -InputObject (48..57 + 65..90 + 97..122) -Count 8 | ForEach-Object {[char]$_}
    
    # Convert the sequence array to a single string
    $sequence = -join $sequence

    # Append the sequence to the file with a new line
    Add-Content -Path $filePath -Value $sequence
}

# Output a message to indicate the process is complete
Write-Host "8 sets of 8-bit encryption keys have been generated and saved to $filePath."
