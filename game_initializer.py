from desmume.emulator import DeSmuME
from desmume.controls import keymask, Keys
import time

a_key = keymask(Keys.KEY_A)
b_key = keymask(Keys.KEY_B)


def run_game():
    emu = DeSmuME()
    emu.open('platinum.nds')

    # Create the window for the emulator
    window = emu.create_sdl_window()

    # Run the game at 60fps
    start_time = time.monotonic()
    frame_num = 0
    while not window.has_quit():
        window.process_input()  # Controls are the default DeSmuME controls, see below.
        emu.cycle()
        window.draw()

        if frame_num % 2:
            emu.input.keypad_add_key(a_key)
        else:
            emu.input.keypad_rm_key(a_key)

        frame_num += 1
        time.sleep((1 / 60.0) - ((time.monotonic() - start_time) % (1 / 60)))


if __name__ == "__main__":
    run_game()
