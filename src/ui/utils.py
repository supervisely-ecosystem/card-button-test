from typing import Callable, Dict, Any, List, Optional
from supervisely.app import DataJson
from supervisely.app.widgets import Button, Widget, Card


button_clicked = {}


def update_custom_params(
    btn: Button,
    params_dct: Dict[str, Any],
) -> None:
    btn_state = btn.get_json_data()
    for key in params_dct.keys():
        if key not in btn_state:
            raise AttributeError(f"Parameter {key} doesn't exists.")
        else:
            DataJson()[btn.widget_id][key] = params_dct[key]
    DataJson().send_changes()


def update_custom_button_params(
    btn: Button,
    params_dct: Dict[str, Any],
) -> None:
    params = params_dct.copy()
    if "icon" in params and params["icon"] is not None:
        new_icon = (
            f'<i class="{params["icon"]}" style="margin-right: {btn._icon_gap}px"></i>'
        )
        params["icon"] = new_icon
    update_custom_params(btn, params)


def disable_enable(widgets: List[Widget], disable: bool = True):
    for w in widgets:
        if disable:
            w.disable()
        else:
            w.enable()


def unlock_lock(cards: List[Card], unlock: bool = True):
    for w in cards:
        if unlock:
            w.unlock()
        else:
            w.lock()


def wrap_button_click(
    btn: Button,
    card_to_unlock: Card,
    widgets_to_disable: List[Widget],
    callback: Optional[Callable] = None,
) -> Callable[[Optional[bool]], None]:
    global button_clicked

    select_params = {"icon": None, "plain": False, "text": "Select"}
    reselect_params = {"icon": "zmdi zmdi-refresh", "plain": True, "text": "Reselect"}
    bid = btn.widget_id
    button_clicked[bid] = False

    def button_click(btn_clicked_value: Optional[bool] = None):
        if btn_clicked_value is not None:
            button_clicked[bid] = btn_clicked_value
        else:
            button_clicked[bid] = not button_clicked[bid]

        if button_clicked[bid]:
            update_custom_button_params(btn, reselect_params)
        else:
            update_custom_button_params(btn, select_params)

        unlock_lock(
            [card_to_unlock],
            unlock=button_clicked[bid],
        )
        disable_enable(
            widgets_to_disable,
            disable=button_clicked[bid],
        )
        if callback is not None and not button_clicked[bid]:
            callback(False)

    return button_click
