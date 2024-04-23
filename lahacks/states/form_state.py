import reflex as rx
from lahacks.states.field_state import FieldState
from lahacks.api.gemini import generate_recipe, generate_prompt
from lahacks.pages.text2img import text2img
import os

file_path = "assets/meal1.png"


class DynamicFormState(rx.State):
    form_data: dict = {}
    form_fields: list[list[str]] = []
    ai_response: str = ""
    submitted: bool = False
    cantSubmit: bool = True
    buttonText: str = "Submit"
    imageLink: str = ""

    def add_field(self, ingredient: str, quantity: int, unit: str):
        if not ingredient:
            return

        self.form_fields.append([ingredient, str(quantity), unit])
        self.cantSubmit = False

    def handle_submit(self, form_data: dict):
        self.submitted = True
        self.cantSubmit = True
        self.buttonText = "Generating..."
        yield
        if not self.form_fields:
            self.submitted = False
            self.cantSubmit = False
            self.buttonText = "Submit"
            return
        self.ai_response = ""
        self.form_data = form_data

        chunks = generate_recipe({
            "ingredients": ", ".join([
                f"{field[1]}{field[2]} {field[0]}"
                for field in self.form_fields
            ]),
        })

        for chunk in chunks:
            self.ai_response += chunk.text
            yield

        if self.ai_response:
            self.form_fields = []
            self.submitted = False
            self.buttonText = "Submit"
            yield
            recipe_prompt = generate_prompt(self.ai_response)
            self.imageLink = text2img(recipe_prompt)

    def handle_reset(self):
        self.ai_response = ""
        self.form_data = {}
        self.form_fields = []
        FieldState.ingredient = ""
        FieldState.quantity = 0
        self.cantSubmit = True
        yield
        if os.path.exists(file_path):
            os.remove(file_path)
