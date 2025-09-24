import os
from PyQt6.QtGui import QFontDatabase, QFont
from enum import Enum

class Font(Enum):
    """Enum for font constants used in the application"""

    # Example font families; replace with actual font names as needed
    ROBOTO = "Roboto"
    OPEN_SANS = "Open Sans"
    LATO = "Lato"
    MONTSERRAT = "Montserrat"
    ARIAL = "Arial"
    TIMES_NEW_ROMAN = "Times New Roman"

    # TO GET THE ONWARD FONT WHICH IS A CUSTOM FONT
    def get_project_root(self):
        """Returns the root directory of the project"""
        # IT FOLLOWS THE STRUCTURE OF THE PROJECT
        current_path = os.path.dirname(os.path.abspath(__file__))
        while os.path.basename(current_path) != "IPES":
            parent = os.path.dirname(current_path)

            if parent == current_path: 
                raise Exception("No se pudo encontrar la carpeta raíz del proyecto IPES")
            current_path = parent
        return current_path

    def load_custom_font(self, font_relative_path):
        """
        LOADS A CUSTOM FONT FROM THE PROJECT ROOT DIRECTORY.
        
        """
        project_root = self.get_project_root()
        
        font_absolute_path = os.path.join(project_root, font_relative_path)
        
        font_id = QFontDatabase.addApplicationFont(font_absolute_path)
        if font_id == -1:
            print(f"No se pudo cargar la fuente: {font_absolute_path}")
            return None
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        return QFont(font_family)

    # ONWARD CUSTOM FONT
    ONWARD = load_custom_font("View/tools/penumbraserifstd-semibold.otf")

    