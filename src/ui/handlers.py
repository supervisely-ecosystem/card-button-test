from time import sleep

import supervisely as sly
from supervisely.app import StateJson

from src.ui.card1 import button1, selector1, card1
from src.ui.card2 import button2, selector2, card2
from src.ui.card3 import button3, selector3, card3
from src.ui.card4 import button4, selector4, card4

# from src.ui.utils import wrap_button_click

# disable/enable selector3, unlock/lock card4
# button3_callback = wrap_button_click(button3, card4, [selector3])

# disable/enable selector2, unlock/lock card3
# call button3_callback after card2 unlock
# button2_callback = wrap_button_click(button2, card3, [selector2], button3_callback)

# disable/enable selector1, unlock/lock card2
# call button2_callback after card2 unlock
# button1_callback = wrap_button_click(button1, card2, [selector1], button2_callback)

c3_id = card3.widget_id


@selector3.value_changed
def s3_change_value(new_value):
    sly.logger.info(f"Selector3 new value: {new_value}")
    sly.logger.info(f"Card3 State in SELECTOR handler: {StateJson()[c3_id]}")


@button1.click
def b1_click():
    button1.disable()
    selector1.disable()
    card2.unlock()


@button2.click
def b2_click():
    selector3.set_value("string2")  # trigger @selector3.value_changed
    button2.disable()
    selector2.disable()

    # if you have too heavy code part in between set_value() and lock()
    # and your PC is slow enough, you may not find the error

    # sleep(5)  # heavy code mode; if uncomment probleb will disappear
    card3.unlock()

    # comment upper code and uncomment code below to fix issue

    # button2.disable()
    # selector2.disable()
    # card3.unlock()
    # selector3.set_value("string2")  # trigger @selector3.value_changed

    sly.logger.info(f"Card3 State in BUTTON2 handler: {StateJson()[c3_id]}")


@button3.click
def b3_click():
    button3.disable()
    selector3.disable()
    card4.unlock()
