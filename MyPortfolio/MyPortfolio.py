from rxconfig import config

import reflex as rx
from .components import header, footer
from MyPortfolio.pages import home, about
from .style import style


@rx.page(route="/", title="Davide.dev")
def home_page() -> rx.Component:
    return rx.vstack(
        header.render_header(),
        home.render_page(),
        footer.Footer(),
        style=style.get("main")
    )


app = rx.App(
    style=style.get("app"),
    theme=rx.theme(
        appearance="dark",
        accent_color="gray"
    )
)