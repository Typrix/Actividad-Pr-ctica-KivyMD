import json

from kivy.config import Config
Config.set("graphics", "width", "360")
Config.set("graphics", "height", "640")
Config.set("graphics", "resizable", "0")

from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton

class DiagnosticoApp(MDApp):

    def close_app(self, instance):
        self.stop()

    def save_organization(self, instance):
        text = self.organization_input.text

        data = {
            "organización": text
        }

        with open("organization.json", "w", encoding = "utf-8") as f:
            json.dump(data, f, ensure_ascii = False, indent = 4)
        print("Text Saved!")


    def build(self):
        # Configuración Material Design
        self.theme_cls.primary_palette = 'Orange'
        self.theme_cls.theme_style = 'Dark'

        screen = MDScreen()

        toolbar = MDTopAppBar(
            title="Organización APP",
            pos_hint={"top": 1}
        )

        welcome = MDLabel(
            text = "Bienvenido",
            halign = "center",
            font_style = "H4",
            size_hint_y =  None,
            pos_hint = {"center_y": 0.7}
        )

        self.organization_input = MDTextField(
            hint_text = "Ingrese el nombre de la organización",
            mode = "rectangle",
            size_hint = (0.9,None),
            pos_hint = {"center_x": 0.5, "center_y": 0.5},
        )

        save_button = MDRaisedButton(
            text = "Guardar",
            pos_hint = {"center_x": 0.5, "center_y": 0.2},
            size_hint = (0.7, None),
            on_release = self.save_organization
        )

        close_button = MDRaisedButton(
            text = "Salir",
            pos_hint = {"center_x": 0.5, "center_y": 0.1},
            size_hint = (0.7, None),
            on_release = self.close_app
        )

        screen.add_widget(toolbar)
        screen.add_widget(save_button)
        screen.add_widget(close_button)
        screen.add_widget(self.organization_input)
        screen.add_widget(welcome)

        return screen


if __name__ == "__main__":
    DiagnosticoApp().run()