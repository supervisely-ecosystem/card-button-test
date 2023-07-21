from src.ui.card1 import button1, selector1, card1
from src.ui.card2 import button2, selector2, card2
from src.ui.card3 import button3, selector3, card3
from src.ui.utils import wrap_button_click


button2_callback = wrap_button_click(button2, card3, [selector2])
button1_callback = wrap_button_click(button1, card2, [selector1], button2_callback)


@button1.click
def b1_click():
    button1_callback()


@button2.click
def b2_click():
    button2_callback()