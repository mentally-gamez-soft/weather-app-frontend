import reflex as rx

from weather_app_frontend.navigation import navbar
from weather_app_frontend.template import template

@template
def tools() -> rx.Component:
    return rx.box(
            navbar(heading="Tools"),
            rx.box(
                rx.text("placeholder"),
                margin_top="calc(50px + 2em)",
                padding="2em",
            ),
            padding_left="250px",
        )
