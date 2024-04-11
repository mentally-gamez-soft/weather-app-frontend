"""The main Dashboard App."""

import reflex as rx

from rxconfig import config
from weather_app_frontend.pages.index import index
from weather_app_frontend.pages.team import team
from weather_app_frontend.pages.tools import tools
from weather_app_frontend.pages.weather_page import weather
from weather_app_frontend.styles import (
    BACKGROUND_COLOR,
    FONT_FAMILY,
    STYLESHEETS,
    THEME,
)

# Create app instance and add index page.
app = rx.App(
    theme=THEME,
    stylesheets=STYLESHEETS,
)

app.add_page(index, route="/")
app.add_page(tools, route="/tools")
app.add_page(team, route="/team")
app.add_page(weather, route="/weather")
