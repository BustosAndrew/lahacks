import reflex as rx


class FieldState(rx.State):
    ingredient: str = ""
    quantity: int = 0
    unit: str = "g"
    details: str = ""

    def set_ingredient(self, ingredient: str):
        self.ingredient = ingredient

    def set_quantity(self, quantity: int):
        self.quantity = quantity

    def set_unit(self, unit: str):
        self.unit = unit

    def reset_vals(self):
        self.ingredient = ""
        self.quantity = 0
        self.unit = "g"
