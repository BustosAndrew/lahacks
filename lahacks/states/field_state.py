import reflex as rx


class FieldState(rx.State):
    ingredient: str = ""
    quantity: str = ""
    unit: str = ""

    def set_ingredient(self, ingredient: str):
        self.ingredient = ingredient

    def set_quantity(self, quantity: str):
        if quantity == "":
            self.quantity = "0"
            return
        elif not quantity.isnumeric():
            self.quantity = "0"
            return
        elif int(quantity) < 0:
            self.quantity = "0"
            return
        self.quantity = quantity

    def set_unit(self, unit: str):
        self.unit = unit

    def reset_vals(self):
        self.ingredient = ""
        self.quantity = "0"
        self.unit = ""
