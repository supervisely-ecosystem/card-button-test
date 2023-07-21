import os

import supervisely as sly
from supervisely.app.widgets import (
    Card,
    DatasetThumbnail,
)

import src.globals as g

dataset_thumbnail = DatasetThumbnail()


if g.STATE.selected_dataset and g.STATE.selected_project:
    # If the app was loaded from a dataset.
    sly.logger.debug("App was loaded from a dataset.")

    # Creating a dataset thumbnail to show.
    dataset_thumbnail.set(
        g.api.project.get_info_by_id(g.STATE.selected_project),
        g.api.dataset.get_info_by_id(g.STATE.selected_dataset),
    )
    dataset_thumbnail.show()


# Input card with all widgets.
card = Card(
    "1️⃣ Input dataset",
    "Images from the selected dataset will be loaded.",
    content=dataset_thumbnail,
    collapsable=False,
)
