import reflex as rx
from lahacks.pages.components.recipe_image import output
from lahacks.states.form_state import DynamicFormState
from lahacks.states.field_state import FieldState
from lahacks.styles.styles import button_style


def dynamic_form():
    return rx.vstack(
        rx.form(
            rx.vstack(
                rx.foreach(
                    DynamicFormState.form_fields,
                    lambda field: rx.box(rx.vstack(
                        rx.vstack(rx.heading("Ingredient", size="4"),
                                  rx.text(field[0], style={"overflow-wrap": "break-word", "word-wrap": "break-word"})),
                        rx.heading("Amount", size="4"),
                        rx.text(field[1] + " " + field[2]),
                    ), border_width=1, border_color="gray-300", border_radius=10, padding=10, width="100%"),
                ),
                rx.hstack(
                    rx.input(
                        placeholder="Ingredient name",
                        name="ingredient",
                        value=FieldState.ingredient,
                        on_change=FieldState.set_ingredient
                    ),
                    rx.input(
                        placeholder="Amount",
                        name="amount",
                        on_change=FieldState.set_quantity,
                        value=FieldState.quantity
                    ),
                    rx.select(["no unit", "grams", "oz", "fl oz", "gallon(s)", "piece(s)", "slice(s)", "can(s)", "jar(s)", "bottle(s)", "jug(s)", "bag(s)"], name="unit", placeholder="Units (optional)",
                              on_change=FieldState.set_unit, value=FieldState.unit),
                    rx.button("+", on_click=DynamicFormState.add_field(
                        FieldState.ingredient,
                        FieldState.quantity,
                        FieldState.unit,
                    ), type="button", style=button_style),
                    rx.button("Clear", on_click=FieldState.reset_vals,
                              type="button", style=button_style),
                ),
                rx.checkbox("Use only these ingredients?", size="3",
                            on_change=DynamicFormState.set_only_ingredients, checked=DynamicFormState.onlyIngredients, name="onlyIngredients"),
                rx.input.root(rx.input(
                    placeholder="Enter your cookware (optional)",
                    name="cookware",
                    on_change=FieldState.set_cookware,
                    value=FieldState.cookware,
                ), width="100%"),
                rx.text("Press the + button to add your ingredient."),
                rx.spacer(),
                rx.hstack(
                    rx.button(DynamicFormState.buttonText, type="submit",
                              disabled=DynamicFormState.cantSubmit, style=button_style),
                    rx.button(
                        "Reset", on_click=DynamicFormState.handle_reset, type="button", style=button_style),
                    rx.cond(
                        DynamicFormState.buttonText == "Generating...",
                        rx.html('''<dotlottie-player src="https://lottie.host/d395e1a4-28dc-4e60-bffd-8a8ed8844318/qvoNVQ79Bc.json" background="transparent" speed="1" style="width: 50px; height: 40px;" loop autoplay></dotlottie-player>'''),
                    ),
                    align="center",
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
                height="100%",
            ),
            on_mount=DynamicFormState.handle_reset,
            on_submit=DynamicFormState.handle_submit,
            reset_on_submit=True,
            height="100%",
        ),
        height="100%",
    )


def index() -> rx.Component:
    return rx.center(
        rx.script(src="https://unpkg.com/@dotlottie/player-component@latest/dist/dotlottie-player.mjs",
                  custom_attrs={"type": "module"}),
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
        ),
        height="100vh",
        paddingX=10,
    )


app = rx.App()
app.add_page(index)
app.add_page(output)
