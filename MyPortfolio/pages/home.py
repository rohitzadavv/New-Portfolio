import os
import reflex as rx

from ..style import style, wave
from ..utilities.utility import create_badge, create_breadcrumb_item, create_stach_image, create_xs_heading, project_image_desktop, project_image_mobile, create_text_with_left_image, create_badge_mobile, create_stach_image_mobile
from ..utilities.yaml_reader import read_yaml

configuration = read_yaml(os.getcwd() + "/configuration.yaml")


page_configuration = configuration["content_page"]
card_titles: list = page_configuration["card_titles"]
workout_project = configuration["projects"][0]
covid_project = configuration["projects"][1]
location_contact = configuration["contact_block"][0]
mail_contact = configuration["contact_block"][1]

images_paths: list = ["/java.png", "/python.png",
                      "/spring-boot.png", "/postgresql.png", "/mongodb.png", "/docker.png"]


def about_me_block_mobile():
    return rx.mobile_only(
        rx.container(
            rx.vstack(
                rx.heading(
                    page_configuration["about_me"],
                    size="5",
                    font_weight="900",
                    style=style.get("title")
                ),
                rx.heading(
                    page_configuration["short_description"],
                    size="5",
                    text_align="center"
                ),
                rx.image(
                    src="/pc_desk.jpg",
                    width="90vw",
                    height="auto",
                    box_shadow="xl",
                    border_radius="15px 15px"
                ),
                rx.text(
                    page_configuration["medium_description"],
                    size="3",
                    text_align="justify",
                    max_w="90vw"
                ),
                spacing="3",
                align_items="center",
                justify_content="center"
            ),
            margin_top="11rem",
            padding=["0 1.5rem"]
        ),
        id="about_mobile"
    )


def about_me_block_desktop():
    return rx.tablet_and_desktop(
        rx.hstack(
            rx.image(
                src="/pc_desk.jpg",
                width=["200px", "250px", "350px", "380px", "380px"],
                height="auto",
                box_shadow="xl",
                border_radius="15px 15px",
                transition="all 300ms ease"
            ),
            rx.box(
                rx.vstack(
                    rx.heading(
                        page_configuration["about_me"],
                        font_size=["1rem", "1.25rem",
                                   "1.25rem", "1.5rem", "1.5rem"],
                        font_weight="900",
                        style=style.get("title"),
                        transition="all 300ms ease"
                    ),
                    rx.heading(
                        page_configuration["short_description"],
                        font_size=["1rem", "1rem",
                                   "1.25rem", "1.25rem", "1.25rem"],
                    ),
                    rx.text(
                        page_configuration["medium_description"],
                        font_size=["0.75rem", "1rem",
                                   "1rem", "1rem", "1rem"],
                    ),
                    justify_content="left",
                    align_items="start"
                ),
                max_width="400px"
            ),
            margin_top="13rem",
            spacing="6",
            padding=["0 1.5rem"],
            wrap="wrap",
            transition="all 300ms ease",
            justify="center"
        ),
        id="about"
    )


def tech_stack_mobile():
    return rx.mobile_only(
        rx.vstack(
            rx.heading(
                page_configuration["tech_stack"],
                size="5"
            ),
            rx.hstack(
                *[create_stach_image_mobile(images_paths[i])
                  for i in range(3)],
                spacing='8',
                width="100%"
            ),
            rx.hstack(
                *[create_stach_image_mobile(images_paths[i])
                  for i in range(3, 6)],
                spacing='8',
                width="100%"
            ),
            spacing="6",
            margin_top="10rem",
            padding="1rem 0",
            align="center",
            justify="center"
        )
    )


def tech_stack_block():
    return rx.tablet_and_desktop(
        rx.hstack(
            rx.heading(
                page_configuration["tech_stack"],
                size="5",
                transition="all 300ms ease"
            ),
            rx.divider(
                orientation="vertical",
                height="2rem",
                width="2px",
                border_color="rgba(255, 255, 255, 0.7)",
                display=["none", "none", "flex", "flex", "flex"],
            ),
            rx.hstack(
                rx.foreach(images_paths, create_stach_image),
                spacing="8",
                justify="center",
                align="center"
            ),
            spacing="5",
            margin_top="10rem",
            padding=["0 1.5rem"],
            align="center",
            justify="center",
            wrap="wrap"
        )
    )


def breadcrumb_block():
    return rx.chakra.breadcrumb(
        create_breadcrumb_item(
            "/github.png", "GitHub", "https://github.com/Davydhh"),
        create_breadcrumb_item(
            "/linkedin.png", "Linkedin", "https://www.linkedin.com/in/davide-cazzetta-3a86a9198")
    )


def card_block_mobile():
    return rx.mobile_only(
        rx.vstack(
            *[create_badge_mobile(card_title) for card_title in card_titles],
            spacing="5",
            margin_top="1rem",
            margin_bottom="1rem",
            align="center"
        )
    )


def card_block_desktop():
    return rx.tablet_and_desktop(
        rx.hstack(
            *[create_badge(card_title.upper()) for card_title in card_titles],
            spacing="4",
            margin_top="0.5rem",
            margin_bottom="0.5rem",
            padding=["0 1rem"]
        )
    )


def landing_block():
    return rx.hstack(
        rx.heading(
            page_configuration["hello"],
            font_size=["40px", "40px", "45px", "50px", "50px"],
            transition="all 300ms ease",
            font_weight="900",
            background_image="linear-gradient(to right, #e1e1e1, #757575)",
            background_clip="text",
            color="transparent",
            display="inline-block",
            padding="0.5rem"
        ),
        rx.heading(
            "👋🏼",
            font_size=["35px", "40px", "45px", "50px", "50px"],
            style=wave
        ),
        spacing="4",
        align="center"
    )


def projects_block_desktop():
    return rx.tablet_and_desktop(
        rx.vstack(
            rx.vstack(
                rx.heading(
                    page_configuration["projects"],
                    font_size=["1rem", "1.25rem",
                               "1.25rem", "1.5rem", "1.5rem"],
                    font_weight="900",
                    style=style.get("title")
                ),
                rx.heading(
                    page_configuration["projects_introduction"],
                    font_size=["1rem", "1rem",
                               "1.25rem", "1.25rem", "1.25rem"]
                ),
                rx.text(
                    "(And others under development...)",
                    color="gray",
                    size="1"
                ),
                spacing="5",
                align="start",
                justify="start"
            ),
            rx.vstack(
                *[project_block_desktop(project["name"], project["description"], project["technologies"],
                                        project["github"], project["live_demo"], project["image_path"], project["period"], image_left=project["image_left"]) for project in configuration["projects"]],
                spacing="9",
                align="center",
                justify="center"
            ),
            margin_top="13rem",
            padding=["0 1.5rem"],
            spacing="7",
            align="start",
            justify="center"
        ),
        id="projects"
    )


def project_block_desktop(title: str, description: str, stack: list, github_link: str, demo_link: str, image_path: str, period: str, image_left: bool = True):
    if image_left:
        return rx.hstack(
            project_image_desktop(image_path),
            project_description_desktop(
                title, description, stack, github_link, demo_link, period),
            spacing="9",
            align="center",
            justify="center"
        )
    else:
        return rx.hstack(
            project_description_desktop(
                title, description, stack, github_link, demo_link, period),
            project_image_desktop(image_path),
            spacing="9",
            align="center",
            justify="center"
        )


def projects_block_mobile():
    return rx.mobile_only(
        rx.vstack(
            rx.vstack(
                rx.heading(
                    page_configuration["projects"],
                    size="5",
                    font_weight="900",
                    style=style.get("title")
                ),
                rx.heading(
                    page_configuration["projects_introduction"],
                    size="5",
                    text_align="justify"
                ),
                rx.text(
                    "(And others under development...)",
                    color="gray",
                    size="1"
                ),
                spacing="3",
                align="center",
                justify="start"
            ),
            rx.vstack(
                *[project_block_mobile(project["name"], project["description"], project["technologies"],
                                       project["github"], project["live_demo"], project["image_path"], project["period"]) for project in configuration["projects"]],
                spacing="9",
                justify="center"
            ),
            margin_top="11rem",
            padding=["0 1.5rem"],
            spacing="7",
            align="center",
            justify="center"
        ),
        id="projects_mobile"
    )


def project_block_mobile(title: str, description: str, stack: list, github_link: str, demo_link: str, image_path: str, period: str):
    return rx.vstack(
        rx.heading(
            title,
            size="3"
        ),
        rx.heading(
            period,
            size="2",
            color="gray"
        ),
        project_image_mobile(image_path),
        rx.text(
            description,
            size="3",
            text_align="justify",
            white_space="pre-wrap"
        ),
        rx.hstack(
            rx.foreach(stack, create_xs_heading),
            spacing="4"
        ),
        rx.cond(
            github_link != "" or demo_link != "",
            rx.hstack(
                rx.cond(
                    github_link != "",
                    rx.link(
                        rx.image(
                            src="/github.png",
                            width="24px",
                            filter="brightness(0) invert(1)"
                        ),
                        href=github_link
                    )
                ),
                rx.cond(
                    demo_link != "",
                    rx.link(
                        rx.button(
                            "Live Demo",
                            rx.icon(
                                tag="external_link",
                                width="20px"
                            ),
                            color="white",
                            variant="ghost"
                        ),
                        href=demo_link
                    )
                ),
                spacing="3"
            )
        ),
        max_width="90vw",
        spacing="5",
        align="center"
    )


def project_description_desktop(title: str, description: str, stack: list, github_link: str, demo_link: str, period: str):
    return rx.vstack(
        rx.vstack(
            rx.heading(
                title,
                size="3"
            ),
            rx.heading(
                period,
                size="2",
                color="gray"
            ),
            spacing="3",
            align="center"
        ),
        rx.text(
            description,
            size="3",
            text_align="center",
            white_space="pre-wrap"
        ),
        rx.hstack(
            *[create_xs_heading(s) for s in stack],
            spacing="4"
        ),
        rx.cond(
            github_link != '' or demo_link != '',
            rx.hstack(
                rx.cond(
                    github_link != '',
                    rx.link(
                        rx.image(
                            src="/github.png",
                            width=["20px", "22px",
                                   "24px", "24px", "24px"],
                            filter="brightness(0) invert(1)",
                            transition="all 300ms ease"
                        ),
                        href=github_link
                    )
                ),
                rx.cond(
                    demo_link != '',
                    rx.link(
                        rx.button(
                            "Live Demo",
                            rx.icon(
                                tag="external_link",
                                padding_left="0.5rem",
                                width=["20px", "22px",
                                       "24px", "24px", "24px"],
                                transition="all 300ms ease"
                            ),
                            _dark={"color": "white"},
                            _light={"color": "black"},
                            variant="ghost"
                        ),
                        href=demo_link
                    )
                ),
                spacing="4"
            )
        ),
        max_width="400px",
        spacing="5",
        justify="center",
        align="center",
    )


def contact_block_desktop():
    return rx.tablet_and_desktop(
        rx.vstack(
            rx.vstack(
                rx.heading(
                    page_configuration["contact"],
                    font_size=["1rem", "1.25rem",
                               "1.25rem", "1.5rem", "1.5rem"],
                    font_weight="900",
                    style=style.get("title")
                ),
                rx.heading(
                    page_configuration["contact_description"],
                    font_size=["1rem", "1rem",
                               "1.25rem", "1.25rem", "1.25rem"]
                ),
                spacing="4"
            ),
            rx.hstack(
                create_text_with_left_image(
                    location_contact["link"], location_contact["image_path"]),
                create_text_with_left_image(
                    mail_contact["link"], mail_contact["image_path"]),
                spacing="7"
            ),
            margin_top="13rem",
            padding=["0 1.5rem"],
            spacing="6",
            align="center"
        ),
        id="contact"
    )


def contact_block_mobile():
    return rx.mobile_only(
        rx.vstack(
            rx.vstack(
                rx.heading(
                    page_configuration["contact"],
                    size="5",
                    font_weight="900",
                    style=style.get("title")
                ),
                rx.heading(
                    page_configuration["contact_description"],
                    size="5"
                ),
                spacing="5",
                align="center"
            ),
            rx.vstack(
                create_text_with_left_image(
                    location_contact["link"], location_contact["image_path"]),
                create_text_with_left_image(
                    mail_contact["link"], mail_contact["image_path"]),
                spacing="5",
                align="center"
            ),
            margin_top="13rem",
            padding=["0 1.5rem"],
            spacing="7",
            align="center"
        ),
        id="contact_mobile"
    )


def publication_desktop():
    return rx.tablet_and_desktop(
        rx.vstack(
            rx.vstack(
                rx.heading(
                    page_configuration["publications"],
                    font_size=["1rem", "1.25rem",
                               "1.25rem", "1.5rem", "1.5rem"],
                    font_weight="900",
                    style=style.get("title"),
                    transition="all 300ms ease"
                ),
                rx.heading(
                    configuration["publication"]["title"],
                    font_size=["1rem", "1.25rem",
                               "1.5rem", "1.5rem", "1.5rem"]
                ),
                rx.text(
                    rx.text.strong("Abstract: "),
                    configuration["publication"]["abstract"],
                    font_size=["0.75rem", "1rem",
                               "1rem", "1rem", "1rem"],
                    transition="all 300ms ease",
                    text_align="justify",
                    width=["90%", "90%", "80%", "70%", "70%"],
                    max_width="800px"
                ),
                rx.link(
                    rx.button(
                        "Go to the paper",
                        variant="surface",
                        size='3',
                        radius="large",
                    ),
                    href="https://doi.ieeecomputersociety.org/10.1109/SITIS61268.2023.00017"
                ),
                spacing="5",
                align="center",
                justify="center"
            ),
            justify="center",
            align="center",
            margin_top="13rem",
            id="publications"
        )
    )


def publication_mobile():
    return rx.mobile_only(
        rx.vstack(
            rx.heading(
                page_configuration["publications"],
                size="5",
                font_weight="900",
                style=style.get("title")
            ),
            rx.heading(
                configuration["publication"]["title"],
                text_align="center"
            ),
            rx.text(
                rx.text.strong("Abstract: "),
                configuration["publication"]["abstract"],
                size='3',
                text_align="justify"
            ),
            rx.link(
                rx.button(
                    "Go to the paper",
                    variant="surface",
                    size='3',
                    radius="large",
                    width="100%"
                ),
                href="https://doi.ieeecomputersociety.org/10.1109/SITIS61268.2023.00017"
            ),
            margin_top="13rem",
            padding=["0 1.5rem"],
            spacing="5",
            align="center",
            id="publications_mobile"
        )
    )


def render_page():
    return rx.vstack(
        landing_block(),
        card_block_desktop(),
        card_block_mobile(),
        breadcrumb_block(),
        tech_stack_block(),
        tech_stack_mobile(),
        about_me_block_desktop(),
        about_me_block_mobile(),
        projects_block_desktop(),
        projects_block_mobile(),
        publication_desktop(),
        publication_mobile(),
        contact_block_desktop(),
        contact_block_mobile(),
        style=style.get("content")
    )
