import reflex as rx
from lahacks.states.field_state import FieldState
from lahacks.api.gemini import generate_recipe


class DynamicFormState(rx.State):
    form_data: dict = {}
    form_fields: list[list[str]] = []
    ai_response: str = ""
    submitted: bool = False
    cantSubmit: bool = True

    def add_field(self, ingredient: str, quantity: int, unit: str):
        if not ingredient:
            return

        self.form_fields.append([ingredient, str(quantity), unit])
        self.cantSubmit = False

    def handle_submit(self, form_data: dict):
        self.submitted = True
        if not self.form_fields:
            self.submitted = False
            return
        self.ai_response = ""
        self.form_data = form_data
        self.ai_response = generate_recipe({
            "ingredients": ", ".join([
                f"{field[1]}{field[2]} {field[0]}"
                for field in self.form_fields
            ]),
            "description": form_data.get("details", ""),
        })
        self.form_fields = []
        self.submitted = False

    def handle_reset(self):
        self.ai_response = ""
        self.form_data = {}
        self.form_fields = []
        FieldState.ingredient = ""
        FieldState.quantity = 0
        self.cantSubmit = True
