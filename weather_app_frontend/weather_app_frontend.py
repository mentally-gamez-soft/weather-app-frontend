"""The main Dashboard App."""

from rxconfig import config

import reflex as rx

from weather_app_frontend.styles import BACKGROUND_COLOR, FONT_FAMILY, THEME, STYLESHEETS

from weather_app_frontend.pages.tools import tools
from weather_app_frontend.pages.team import team
from weather_app_frontend.pages.index import index

# Create app instance and add index page.
app = rx.App(
    theme=THEME,
    stylesheets=STYLESHEETS,
)

app.add_page(index, route="/")
app.add_page(tools, route="/tools")
app.add_page(team, route="/team")
