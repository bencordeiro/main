import time
import shutil
import sys

# ASCII Art for the train
TRAIN_ART = [
    r"      ====        ________                ___________ ",
    r"  _D _|  |_______/        \__I_I_____===__|_________| ",
    r"   |(_)---  |   H\________/ |   |        =|___ ___|   ",
    r"   /     |  |   H  |  |     |   |         ||_| |_||   ",
    r"  |      |  |   H  |__--------------------| [___] |   ",
    r"  | ________|___H__/__|_____/[][]~\_______|       |   ",
    r"  |/ |   |-----------I_____I [][] []  D   |=======|__ ",
    r"__/ =| o |=-~~\  /~~\  /~~\  /~~\ ____Y___________|__ ",
    r" |/-=|___|=O=====O=====O=====O   |_____/\___/        ",
    r"  \_/      \__/  \__/  \__/  \__/      \_/            ",
]

def get_terminal_width():
    return shutil.get_terminal_size().columns

def animate_train():
    width = get_terminal_width()
    train_length = len(TRAIN_ART[0])
    
    # The train moves from right to left.
    # Start with the train completely off-screen to the right
    # End when the train is completely off-screen to the left
    
    # Total distance: screen width + train length
    total_steps = width + train_length + 1
    
    try:
        for step in range(total_steps):
            # Clear screen (ANSI escape code)
            sys.stdout.write("\033[2J\033[H")
            
            # Calculate position
            # If step < width, the nose is moving into the screen from right
            # If step > width, the tail is moving off the screen to the left
            
            start_col = width - step
            
            output_lines = []
            for row in TRAIN_ART:
                if start_col >= 0:
                    # Train is entering or in the middle
                    # Print spaces then the part of the train that fits
                    spaces = " " * start_col
                    visible_len = width - start_col
                    line = spaces + row[:visible_len]
                else:
                    # Train is leaving the left side
                    # We need to slice the beginning of the train string
                    offset = abs(start_col)
                    line = row[offset:offset + width]
                
                output_lines.append(line)
            
            # Print the frame (centering vertically a bit if desired, but top is fine for SL feel)
            sys.stdout.write("\n" * 5) # Add some top padding
            for line in output_lines:
                sys.stdout.write(line + "\n")
            
            sys.stdout.flush()
            time.sleep(0.05) # Adjust speed here

    except KeyboardInterrupt:
        # Handle Ctrl+C gracefully (or strictly disallow it like the real SL if we were evil, but let's be nice)
        sys.stdout.write("\nChoo choo interrupted!\n")

if __name__ == "__main__":
    animate_train()
