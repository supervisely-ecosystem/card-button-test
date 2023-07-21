from supervisely.app.widgets import Button, Container, Card, SelectString


button1 = Button("Select")
selector1 = SelectString(["string1", "string2"], ["string1", "string2"])
card1 = Card(
    "Card #1",
    content=Container([selector1, button1]),
)
