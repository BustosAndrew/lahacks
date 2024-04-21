

import reflex as rx


class RecipeImage(rx.Component):
    
    def render(self):
        return rx.box(
            rx.image(
                {
                    "src": "placeholder-image-url",
                    "alt": "Recipe Image",
                    "width": "300",
                    "height": "200",
                }
            )
        )



