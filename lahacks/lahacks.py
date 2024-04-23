import reflex as rx
from lahacks.pages.components.recipe_image import output
from lahacks.states.form_state import DynamicFormState
from lahacks.states.field_state import FieldState


def dynamic_form():
    return rx.vstack(
        rx.form(
            rx.vstack(
                rx.foreach(
                    DynamicFormState.form_fields,
                    lambda field: rx.hstack(
                        rx.vstack(rx.heading("Ingredient", size="4"),
                                  rx.text(field[0])),
                        rx.vstack(rx.heading("Weight", size="4"),
                                  rx.text(field[1] + field[2]),),
                    ),
                ),
                rx.hstack(
                    rx.input(
                        placeholder="Ingredient name",
                        name="ingredient",
                        value=FieldState.ingredient,
                        on_change=FieldState.set_ingredient
                    ),
                    rx.input(
                        placeholder="Quantity",
                        name="quantity",
                        # value=f"{FieldState.quantity}",
                        on_change=FieldState.set_quantity
                    ),
                    rx.select(["g", "oz"], name="unit", value=FieldState.unit,
                              on_change=FieldState.set_unit),
                    rx.button("+", on_click=DynamicFormState.add_field(
                        FieldState.ingredient,
                        FieldState.quantity,
                        FieldState.unit
                    ), type="button"),
                    rx.button("Clear", on_click=FieldState.reset_vals,
                              type="button"),
                ),
                rx.text("Press the + button to add your ingredient."),
                rx.spacer(),
                rx.hstack(
                    rx.button(DynamicFormState.buttonText, type="submit",
                              disabled=DynamicFormState.cantSubmit),
                    rx.button(
                        "Reset", on_click=DynamicFormState.handle_reset, type="button"),
                    rx.cond(
                        DynamicFormState.submitted,
                        rx.text("Recipe generating!"),
                    ),
                ),
                rx.cond(
                    DynamicFormState.ai_response != "",
                    rx.box(rx.text("View your ", size="4", as_="span"), rx.link(
                        "generated recipe!",
                        href="/output/",
                        underline="always",
                        size="4",
                        as_="span"
                    )),
                ),
                height="100%"
            ),
            on_mount=DynamicFormState.handle_reset,
            on_submit=DynamicFormState.handle_submit,
            reset_on_submit=True,
            height="100%"
        ),
        height="100%"
    )


def index() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading("Chef.ai", marginX="auto", paddingY=10),
            rx.box(
                dynamic_form(),
                border_width=1,
                border_color="gray-300",
                border_radius=10,
                height="80%",
                padding=20,
            ),
            height="100%",
            padding=20,
        ),
        height="100vh",
    )


app = rx.App()
app.add_page(index)
app.add_page(output)
