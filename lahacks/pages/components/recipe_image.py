import reflex as rx
from lahacks.states.form_state import DynamicFormState


@rx.page(route="/output/[res]")
def output():
    return rx.center(
        # rx.image(
        #     src="/img/meal1.jpg",
        #     alt="Recipe Image",
        #     width="300px",
        #     height="200px",
        # )
        rx.vstack(
            rx.heading("Generated Recipe"),
            rx.markdown(DynamicFormState.ai_response),
            height="100%",
        ),
        height="100vh",
        padding=20,
        paddingY=30,
    )
