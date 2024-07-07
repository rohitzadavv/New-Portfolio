import os
import reflex as rx
from MyPortfolio.style import style
from MyPortfolio.utilities.utility import create_menu_item, create_header_button
from MyPortfolio.utilities.yaml_reader import read_yaml

configuration = read_yaml(os.getcwd() + "/configuration.yaml")


def render_header():
    return rx.hstack(
        rx.heading(configuration["header"]["title"], size="5"),
        rx.spacer(),
        rx.tablet_and_desktop(
            rx.hstack(
                create_header_button("Home", "/"),
                create_header_button("About", "#about"),
                create_header_button("Projects", "#projects"),
                create_header_button("Publications", "#Publications"),
                create_header_button("Contact", "#contact"),
                spacing="5"
            )
        ),
        rx.mobile_only(
            rx.menu.root(
                rx.menu.trigger(
                    rx.icon(
                        tag="menu",
                        stroke_width=2,
                        size=20,
                        filter="brightness(0) invert(1)"
                    )
                ),
                rx.menu.content(
                    create_menu_item("Home", "/"),
                    create_menu_item("About", "#about_mobile"),
                    create_menu_item("Projects", "#projects_mobile"),
                    create_menu_item("Publications", "#Publications_mobile"),
                    create_menu_item("Contact", "#contact_mobile"),
                    style=style.get("app")
                ),
                align="center"
            )
        ),
        align="center",
        style=style.get("header")
    )


