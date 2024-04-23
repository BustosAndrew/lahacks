import reflex as rx
from lahacks.states.form_state import DynamicFormState


@rx.page(route="/output/")
def output():
    return rx.center(
        rx.vstack(
            rx.link(rx.button("Go Back", _hover={"cursor": "pointer"},), href="/",
                    ),
            rx.cond(
                DynamicFormState.imageLink == "",
                rx.text("Generating Image..."),
                rx.image(
                    src=DynamicFormState.imageLink,
                    alt="Recipe Image",
                    width="100%",
                    height="100%",
                )),
            rx.heading("Generated Recipe"),
            rx.markdown(DynamicFormState.ai_response),
            height="100%",
        ),
        height="100vh",
        padding=20,
        paddingY=30,
    )
