from supervisely.app.widgets import Button, Container, Card, SelectString


button4 = Button("Select")
selector4 = SelectString(["string1", "string2"], ["string1", "string2"])
card4 = Card(
    "Card #4",
    content=Container([selector4, button4]),
)

card4.lock()
