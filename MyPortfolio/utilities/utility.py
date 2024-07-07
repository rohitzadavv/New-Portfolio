import reflex as rx
from ..style import style


def create_menu_item(title: str, ref: str):
    return rx.menu.item(
        rx.link(
            title,
            href=ref,
            color="white",
            width="100%"
        ),
        style=style.get("app")
    )


def create_header_button(title: str, ref: str):
    return rx.link(
        title,
        weight="bold",
        color="white",
        href=ref
    )


def create_badge(title):
    return rx.text(
        title,
        bg="#505A6A",
        border_radius="5px",
        weight="bold",
        font_size=["12px", "12px", "14px", "14px", "14px"],
        transition="all 300ms ease",
        wrap="wrap",
        padding=[
            "0.15rem 0.35rem",
            "0.15rem 0.35rem",
            "0.15rem 1rem",
            "0.15rem 1rem",
            "0.15rem 1rem"
        ]
    )

def create_badge_mobile(title):
    return rx.text(
        title,
        bg="#505A6A",
        border_radius="5px",
        weight="bold",
        size='3',
        wrap="wrap",
        padding="0.15rem 0.5rem"
    )


def create_breadcrumb_item(path: str, title: str, url: str):
    return rx.chakra.breadcrumb_item(
        rx.chakra.hstack(
            rx.chakra.image(
                src=path,
                html_width="20px",
                html_height="20px",
                _dark={"filter": "brightness(0) invert(1)"},
            ),
            rx.chakra.breadcrumb_link(
                title,
                href=url,
                _dark={"color": "rgba(255, 255, 255, 0.7)"},
                font_size="sm"
            )
        )
    )


def create_stach_image(path: str):
    return rx.image(
        src=path,
        width=["29px", "32px", "36px", "40px", "44px"],
        height="auto",
        transition="all 300ms ease"
    )

def create_stach_image_mobile(path: str):
    return rx.image(
        src=path,
        width="40px",
        height="auto"
    )


def create_xs_heading(title: str):
    return rx.heading(
        title,
        size="2"
    )


def project_image_desktop(path: str):
    return rx.image(
        src=path,
        width=["200px", "250px", "350px", "400px", "400px"],
        height="auto",
        box_shadow="xl",
        border_radius="15px 15px",
        transition="all 300ms ease",
        display=["none", "flex", "flex", "flex", "flex"],
    )


def project_image_mobile(path: str):
    return rx.image(
        src=path,
        width="340px",
        height="auto",
        box_shadow="xl",
        border_radius="15px 15px",
        transition="all 300ms ease"
    )


def create_text_with_left_image(text: str, icon_path: str):
    return rx.hstack(
        rx.image(
            src=icon_path,
            width="28px",
            height="28px",
            filter="brightness(0) invert(1)"
        ),
        rx.text(text)
    )
