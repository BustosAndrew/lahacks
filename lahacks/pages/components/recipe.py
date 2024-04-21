# recipe.py

import reflex as rx


class Recipe(rx.Component):
    def __init__(self):
        super().__init__()
        self.state = {"recipe": ""}

    def render(self):
        return rx.box(
            rx.heading(
                {"for_": "recipe"},
                "Recipe:",
            ),
            rx.input(
                {
                    "id": "recipe",
                    "type_": "text",
                    "value": self.state["recipe"],
                    "on_input": lambda e: self.set_state({"recipe": e.target.value}),
                }
            ),
        )



