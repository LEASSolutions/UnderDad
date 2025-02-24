from underdad.settings import *
from underdad.settings.local import *

# Test codehilite with pygments

WIKI_MARKDOWN_KWARGS = {
    "extensions": [
        "codehilite",
        "footnotes",
        "attr_list",
        "headerid",
        "extra",
    ]
}
