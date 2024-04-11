import reflex as rx

from weather_app_frontend.navigation import navbar
from weather_app_frontend.template import template
from weather_app_frontend.weather_data import (
    weather_forecast,
    weather_forecast_2,
)


def card(*children, **props):
    return rx.card(
        *children,
        box_shadow=(
            "rgba(0, 0, 0, 0.1) 0px 4px 6px -1px, rgba(0, 0, 0, 0.06) 0px 2px"
            " 4px -1px;"
        ),
        **props,
    )


def weather_header_card() -> rx.Component:
    return rx.hstack(
        rx.box(
            rx.text("City: "),
            rx.text(weather_forecast[0]["day"]["location"]["name"]),
            text_align="left",
        ),
        rx.box(
            rx.text(weather_forecast[0]["day"]["temperature"]["real"]),
            rx.text("C"),
            text_align="center",
        ),
        rx.box(
            rx.text(weather_forecast[0]["day"]["weather"]["icon"]),
            text_align="right",
        ),
    )


def weather_header_card2() -> rx.Component:
    return rx.hstack(
        rx.box(
            rx.avatar(src="/city.png"),
            rx.text(weather_forecast_2["day"]["location"]["name"]),
            text_align="left",
            width="33%",
        ),
        rx.box(
            rx.avatar(src="/temperature.png"),
            rx.text(
                "{} C".format(weather_forecast_2["day"]["temperature"]["real"])
            ),
            text_align="left",
            width="33%",
        ),
        rx.box(
            rx.text(weather_forecast_2["day"]["weather"]["icon"]),
            rx.text(weather_forecast_2["day"]["weather"]["description"]),
            text_align="left",
            width="33%",
        ),
        # spacing="2",
        # padding="1em",
        width="100%",
    )


def weather_footer_card() -> rx.Component:
    return rx.hstack(  # rx.vstack(
        # rx.hstack(
        rx.box(
            rx.text("Temp feel: "),
            rx.text(weather_forecast[0]["day"]["temperature"]["feel"]),
            text_align="left",
            width="33%",
        ),
        rx.box(
            rx.text("Humidity: "),
            rx.text(weather_forecast[0]["day"]["temperature"]["humidity"]),
            text_align="left",
            width="33%",
        ),
        # ),
        # rx.hstack(
        rx.box(
            rx.text("Wind Speed: "),
            rx.text(weather_forecast[0]["day"]["wind"]["speed"]),
            text_align="left",
            width="33%",
        ),
        # spacing="2",
        # padding="1em",
        width="100%",
        # ),
    )


def weather_footer_card2() -> rx.Component:
    return rx.hstack(  # rx.vstack(
        # rx.hstack(
        rx.box(
            rx.avatar(src="/temp_feel.png"),
            rx.text(weather_forecast_2["day"]["temperature"]["feel"]),
            text_align="left",
            width="33%",
        ),
        rx.box(
            rx.avatar(src="/humidity.png"),
            rx.text(weather_forecast_2["day"]["temperature"]["humidity"]),
            text_align="left",
            width="33%",
        ),
        rx.box(
            rx.avatar(src="/wind.png"),
            rx.text(weather_forecast_2["day"]["wind"]["speed"]),
            text_align="left",
            width="33%",
        ),
        # spacing="3",
        # padding="1em",
        width="100%",
        # ),
    )


def sun_day_info() -> rx.Component:
    return rx.hstack(
        rx.box(
            rx.text("Rise"),
            rx.avatar(src="/sunrise.png"),
            rx.text(
                weather_forecast_2["week"][0]["ephemeride"]["sun"]["rise"]
            ),
            width="50%",
            text_align="left",
        ),
        rx.box(
            rx.text("Set"),
            rx.avatar(src="/sunset.png"),
            rx.text(weather_forecast_2["week"][0]["ephemeride"]["sun"]["set"]),
            width="50%",
            text_align="left",
        ),
        # spacing="9",
        # padding="1em",
        width="100%",
    )


def moon_day_info() -> rx.Component:
    return rx.hstack(
        rx.box(
            rx.text("Rise"),
            rx.avatar(src="/moonrise6.png"),
            rx.text(
                weather_forecast_2["week"][0]["ephemeride"]["moon"]["rise"]
            ),
            text_align="left",
            width="33%",
        ),
        rx.box(
            rx.text("Set"),
            rx.avatar(src="/moonset.png"),
            rx.text(
                weather_forecast_2["week"][0]["ephemeride"]["moon"]["set"]
            ),
            text_align="center",
            width="33%",
        ),
        rx.box(
            rx.text(
                weather_forecast_2["week"][0]["ephemeride"]["moon"]["phase"]
            ),
            rx.text(
                weather_forecast_2["week"][0]["ephemeride"]["moon"]["light"]
            ),
            text_align="right",
            width="33%",
        ),
        # spacing="5",
        # padding="1em",
        width="100%",
    )


def weather_body_card() -> rx.Component:
    return rx.hstack(
        rx.text(
            weather_forecast[0]["day"]["weather"]["description"],
            text_align="center",
        ),
        width="100%",
        text_align="center",
    )


def weather_card2() -> rx.Component:
    return card(
        rx.vstack(
            weather_header_card2(),
            # rx.divider(),
            # weather_body_card(),
            rx.divider(),
            weather_footer_card2(),
            rx.divider(),
            sun_day_info(),
            rx.divider(),
            moon_day_info(),
        )
    )


def weather_card(title: str, temperature: str, icon: str) -> rx.Component:
    # color = "var(--red-9)" if delta[0] == "-" else "var(--green-9)"
    # arrow = "decrease" if delta[0] == "-" else "increase"
    return card(
        rx.hstack(
            rx.vstack(
                rx.text(title),
                rx.text(temperature),
                rx.text(icon),
                rx.text("Hello"),
                rx.text("world"),
                rx.text("heu !!!"),
                # rx.chakra.stat(
                #     rx.hstack(
                #         rx.chakra.stat_number(stat, color=color),
                #         rx.chakra.stat_help_text(
                #             rx.chakra.stat_arrow(type_=arrow), delta[1:]
                #         ),
                #     ),
                # ),
            ),
        ),
    )


def weather_grid():
    return rx.hstack(
        rx.chakra.grid(
            # *[
            #     rx.chakra.grid_item(weather_card(forecast["day"]["location"]["name"], forecast["day"]["temperature"]["real"], forecast["day"]["weather"]["icon"]), col_span=1, row_span=1)
            #     for forecast in weather_forecast
            # ],
            rx.chakra.grid_item(weather_card2(), col_span=1, row_span=1),
            # rx.chakra.grid_item(
            #     weather_card2(), col_span=1, row_span=1
            # ),
            # rx.chakra.grid_item(
            #     weather_card2(), col_span=1, row_span=1
            # ),
            template_columns="repeat(1, 1fr)",
            width="25%",
            gap=3,
            row_gap=9,
        ),
        rx.chakra.grid(
            # *[
            #     rx.chakra.grid_item(weather_card(forecast["day"]["location"]["name"], forecast["day"]["temperature"]["real"], forecast["day"]["weather"]["icon"]), col_span=1, row_span=1)
            #     for forecast in weather_forecast
            # ],
            rx.chakra.grid_item(weather_card2(), col_span=1, row_span=1),
            template_columns="repeat(1, 1fr)",
            width="70%",
            gap=3,
            row_gap=3,
        ),
        width="100%",
    )


@template
def weather() -> rx.Component:
    return rx.box(
        navbar(heading="Weather Forecasts"),
        rx.box(
            weather_grid(),
            margin_top="calc(50px + 2em)",
            padding="2em",
        ),
        padding_left="250px",
    )
