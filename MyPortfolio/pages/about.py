import os
import reflex as rx
from ..style import style
from ..utilities.yaml_reader import read_yaml

configuration = read_yaml(os.getcwd() + "/configuration.yaml")


class About(rx.chakra.Vstack):
    def __init__(self):
        super().__init__(style=style.get("about"))

        self.children = [
            self.block_desktop()
        ]

    def block_desktop(self):
        return rx.tablet_and_desktop(
            rx.chakra.vstack(
                rx.chakra.heading(
                    configuration["content_page"]["about_me"],
                    size="3xl",
                    transition="all 300ms ease",
                    font_weight="900",
                    _dark={
                        "background": "linear-gradient(to right, #e1e1e1, #757575)",
                        "background_clip": "text"
                    }
                ),
                rx.chakra.hstack(
                    rx.chakra.image(
                        src="/me.jpg",
                        width=["180px", "200px", "220px", "250px", "250px"],
                        height="auto",
                        box_shadow="xl",
                        border_radius="10px 10px",
                        transition="all 300ms ease"
                    ),
                    rx.chakra.vstack(
                        rx.chakra.tabs(
                            rx.chakra.tab_list(
                                rx.chakra.tab(
                                    "MY STORY",
                                    _selected={"_dark": {"color": "white"}, "_light": {
                                        "color": "black"}},
                                    color="gray",
                                    mr="10"),
                                rx.chakra.tab("EXPERIENCE",
                                       _selected={"_dark": {"color": "white"}, "_light": {
                                           "color": "black"}},
                                       color="gray",
                                       mr="10"),
                                rx.chakra.tab("EDUCATION",
                                       _selected={"_dark": {"color": "white"}, "_light": {
                                           "color": "black"}},
                                       color="gray")
                            ),
                            rx.chakra.tab_panels(
                                rx.chakra.tab_panel(
                                    rx.chakra.text(configuration["about_page"]["my_story"]),
                                    max_w="600px"
                                ),
                                rx.chakra.tab_panel(
                                    rx.chakra.text("Experience"),
                                    max_w="600px"
                                ),
                                rx.chakra.tab_panel(
                                    rx.chakra.text("Education"),
                                    max_w="600px"
                                )
                            ),
                            variant="unstyled",
                            size="lg"
                        ),
                        spacing="2.5rem",
                    ),
                    spacing="2.5rem",
                    align_items="stretch"
                ),
                spacing="3rem",
                justify_content="center",
                margin_left="1.5rem",
                margin_right="1.5rem"
            )
        )
