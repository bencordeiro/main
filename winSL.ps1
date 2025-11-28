$train = @(
    "      ====        ________                ___________ ",
    "  _D _|  |_______/        \__I_I_____===__|_________| ",
    "   |(_)---  |   H\________/ |   |        =|___ ___|   ",
    "   /     |  |   H  |  |     |   |         ||_| |_||   ",
    "  |      |  |   H  |__--------------------| [___] |   ",
    "  | ________|___H__/__|_____/[][]~\_______|       |   ",
    "  |/ |   |-----------I_____I [][] []  D   |=======|__ ",
    "__/ =| o |=-~~\  /~~\  /~~\  /~~\ ____Y___________|__ ",
    " |/-=|___|=O=====O=====O=====O   |_____/~\___/        ",
    "  \_/      \__/  \__/  \__/  \__/      \_/            "
)

$width = $Host.UI.RawUI.WindowSize.Width
$trainWidth = $train[0].Length
$startPos = $width - 1
$endPos = -($trainWidth)

# Hide cursor
$originalCursor = $Host.UI.RawUI.CursorSize
try {
    $Host.UI.RawUI.CursorSize = 0
} catch {}

Clear-Host

for ($i = $startPos; $i -ge $endPos; $i--) {
    $frame = ""
    foreach ($line in $train) {
        if ($i -gt 0) {
            # Train is entering or in middle
            $padding = " " * $i
            $visibleLine = $line
            # If line goes off screen to the right (shouldn't happen with this logic usually but good for safety)
            if (($i + $visibleLine.Length) -gt $width) {
                 $visibleLine = $visibleLine.Substring(0, ($width - $i))
            }
            $frame += "$padding$visibleLine`n"
        } else {
            # Train is exiting left
            $cut = [math]::Abs($i)
            if ($cut -lt $line.Length) {
                $visibleLine = $line.Substring($cut)
                $frame += "$visibleLine`n"
            } else {
                $frame += "`n"
            }
        }
    }
    
    # Move cursor to top left and write frame
    [Console]::SetCursorPosition(0, 0)
    Write-Host $frame -NoNewline
    Start-Sleep -Milliseconds 50
}

Clear-Host
# Restore cursor (approximate, exact restoration varies)
try {
    $Host.UI.RawUI.CursorSize = $originalCursor
} catch {
    $Host.UI.RawUI.CursorSize = 25
}
