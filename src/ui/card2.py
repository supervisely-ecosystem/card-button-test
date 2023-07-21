from supervisely.app.widgets import Button, Container, Card, SelectString


button2 = Button("Select")
selector2 = SelectString(["string1", "string2"], ["string1", "string2"])
card2 = Card(
    "Card #2",
    content=Container([selector2, button2]),
)

card2.lock()
