import supervisely as sly

from supervisely.app.widgets import Container

import src.globals as g
import src.ui.dataset as dataset
import src.ui.handlers
import src.ui.card1 as c1
import src.ui.card2 as c2
import src.ui.card3 as c3

# import src.ui.settings as settings
# import src.ui.output as output

layout = Container(widgets=[dataset.card, c1.card1, c2.card2, c3.card3])

# * If the app uses static dir, it should be passed as a parameter.
# * If not needed the app can be initialized without static_dir parameter.
# * app = sly.Application(layout=layout)
app = sly.Application(layout=layout)
