import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.keys import KC
from kmk.modules.split import Split, SplitType
from kmk.modules.encoder import EncoderHandler

keyboard = KMKKeyboard()

keyboard.col_pins = (
    board.P0_05,  
    board.P1_15, 
    board.P1_14,  
    board.P1_13,  
    board.P1_12,  
    board.P0_11,  
)

keyboard.row_pins = (
    board.P0_02,  
    board.P0_03,  
    board.P0_28,  
    board.P0_29,  
    board.P0_04,  
)

keyboard.diode_orientation = DiodeOrientation.ROW2COL

keyboard.modules.append(
    Split(
        split_type=SplitType.BLE,
        split_side=None,
    )
)

encoder = EncoderHandler()
encoder.pins = (
    (board.P0_06, board.P0_07, None),
)
encoder.map = [
    (KC.VOLD, KC.VOLU),
]
keyboard.modules.append(encoder)

keyboard.keymap = [
    [
        # ───── LEFT HALF ─────        ───── RIGHT HALF ─────
        KC.NO, KC.Q, KC.W, KC.E, KC.R, KC.T,    KC.Y, KC.U, KC.I, KC.O, KC.P, KC.NO,
        KC.NO, KC.A, KC.S, KC.D, KC.F, KC.G,    KC.H, KC.J, KC.K, KC.L, KC.SCLN, KC.NO,
        KC.NO, KC.Z, KC.X, KC.C, KC.V, KC.B,    KC.N, KC.M, KC.COMM, KC.DOT, KC.SLSH, KC.NO,
        KC.NO, KC.LCTL, KC.LALT, KC.LGUI, KC.SPC, KC.BSPC,
               KC.ENT, KC.SPC, KC.RGUI, KC.RALT, KC.RCTL, KC.NO,
        KC.TAB, KC.ESC, KC.NO, KC.NO, KC.NO, KC.NO,
               KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO,
    ]
]

keyboard.go()
