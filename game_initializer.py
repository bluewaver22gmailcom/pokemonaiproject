from desmume.emulator import DeSmuME
from desmume.controls import keymask, Keys
import time

a_key = keymask(Keys.KEY_A)
b_key = keymask(Keys.KEY_B)

target_fps = 60

def run_game():
    emu = DeSmuME()
    emu.open('platinum.nds')

    # Create the window for the emulator
    window = emu.create_sdl_window()

    # Run the game at 60fps
    frame_interval = 1.0 / target_fps
    while not window.has_quit():
        # Record the start time of the current frame
        start_time = time.time()

        window.process_input()  # Controls are the default DeSmuME controls, see below.
        emu.cycle()
        window.draw()

        # Calculate the time taken to process the frame
        elapsed_time = time.time() - start_time

        # If the processing time is less than the frame interval,
        # sleep for the remaining time to achieve the target fps
        if elapsed_time < frame_interval:
            time.sleep(frame_interval - elapsed_time)


if __name__ == "__main__":
    run_game()
