import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import Scanner, PinDirect
from kmk.modules.encoder import EncoderHandler

keyboard = KMKKeyboard()

# Define direct pins for 6 switches
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

# Optional rotary encoder support
encoder_handler = EncoderHandler()
encoder_handler.encoder_pins = [(board.GP2, board.GP1)]  # A, B
encoder_handler.map = [((KC.VOLD, KC.VOLU),)]
keyboard.modules.append(encoder_handler)

# Keymap: Ctrl+Shift+Alt+1 through 6
keyboard.keymap = [
    [
        KC.LCTRL(KC.LSHIFT(KC.LALT(KC._1))),  # Button 1
        KC.LCTRL(KC.LSHIFT(KC.LALT(KC._2))),  # Button 2
        KC.LCTRL(KC.LSHIFT(KC.LALT(KC._3))),  # Button 3
        KC.LCTRL(KC.LSHIFT(KC.LALT(KC._4))),  # Button 4
        KC.LCTRL(KC.LSHIFT(KC.LALT(KC._5))),  # Button 5
        KC.LCTRL(KC.LSHIFT(KC.LALT(KC._6))),  # Button 6
    ]
]

if __name__ == '__main__':
    keyboard.go()
