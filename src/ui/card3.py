from supervisely.app.widgets import Button, Container, Card, SelectString


button3 = Button("Select")
selector3 = SelectString(["string1", "string2"], ["string1", "string2"])
card3 = Card(
    "Card #3",
    content=Container([selector3, button3]),
)

card3.lock()
