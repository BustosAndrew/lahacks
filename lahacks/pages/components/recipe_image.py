import reflex as rx
from lahacks.states.form_state import DynamicFormState
from lahacks.styles.styles import button_style


def notification():
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button("View Recipe Image", style=button_style)),
        rx.dialog.content(
            rx.dialog.title("Generated Recipe Image"),
            rx.image(
                src=DynamicFormState.imageLink,
                alt="Recipe Image",
                width="100%",
                height="100%",
                border_radius=10,
            ),
            rx.dialog.close(
                rx.button("Close",
                          style=button_style),
                margin_top=20,
            ),
        ),
    )


@rx.page(route="/output/")
def output():
    return rx.center(
        rx.script(src="https://unpkg.com/@dotlottie/player-component@latest/dist/dotlottie-player.mjs",
                  custom_attrs={"type": "module"}),
        rx.vstack(
            rx.link(rx.button("Go Back", _hover={"cursor": "pointer"}, style=button_style), href="/",
                    ),
            rx.cond(
                DynamicFormState.imageLink == "",
                rx.box(rx.text("Cooking something up..."), rx.html(
                    '''<dotlottie-player src="https://lottie.host/f3bf595a-c177-4b15-bd92-7b77c9c1cb7f/5rP9GZJohZ.json" background="transparent" speed="1" style="width: 300px; height: 300px;" loop autoplay></dotlottie-player>'''),
                ),
                notification()
            ),
            rx.heading("Generated Recipe"),
            rx.markdown(DynamicFormState.ai_response),
            height="100%",
        ),
        height="100vh",
        padding=20,
        paddingY=30,
    )
