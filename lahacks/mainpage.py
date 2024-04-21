
import reflex as rx
from lahacks.pages.components import recipe
from lahacks.pages.components import recipe_image

# @rx.page(route= "/output") 
class MainComponent(rx.Component):

    def render(self):
        return rx.box(
            recipe(),
            recipe_image(),
          
        )



