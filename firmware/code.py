import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import Scanner, PinDirect
from kmk.modules.encoder import EncoderHandler

keyboard = KMKKeyboard()

# Define pins for 6 buttons (direct input)
keyboard.matrix = Scanner(
    [PinDirect(pin) for pin in (
        board.GP26,
        board.GP27,
        board.GP28,
        board.GP29,
        board.GP6,
        board.GP7,
    )]
)

# Rotary encoder setup (volume control)
encoder_handler = EncoderHandler()
encoder_handler.encoder_pins = [(board.GP2, board.GP1)]
encoder_handler.map = [((KC.VOLD, KC.VOLU),)]
keyboard.modules.append(encoder_handler)

# Keymap: just send digits 1-6
keyboard.keymap = [
    [
        KC._1,  # Button 1 sends '1'
        KC._2,  # Button 2 sends '2'
        KC._3,  # Button 3 sends '3'
        KC._4,  # Button 4 sends '4'
        KC._5,  # Button 5 sends '5'
        KC._6,  # Button 6 sends '6'
    ]
]

if __name__ == '__main__':
    keyboard.go()
