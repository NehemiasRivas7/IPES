from PyQt6.QtWidgets import QPushButton
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QSize
from View.tools.colors import Color

class MenuImgButton(QPushButton):

    def __init__(self, icon_path, parent=None):
        super().__init__(parent)
        
        # Set the icon for the button
        self.setIcon(QIcon(icon_path))
        
        # SET THE SIZE OF THE ICON
        self.setIconSize(QSize(40, 40))
        
        # SET THE SIZE OF THE BUTTON
        self.setFixedSize(80, 110)

        
        # THE STYLE OF THE BUTTON DEPENDES ON THE SECTION IT LEADS TO
        if parent  == "MainWindow":
            self.setStyleSheet(f"""
                QPushButton {{
                    background-color: {Color.GRAY.value};
                    border: none;
                }}
                QPushButton:hover {{
                    background-color: {Color.LIGHT_PURPLE.value};
                }}
                QPushButton:pressed {{
                    background-color: {Color.MIDDLE_PURPLE.value};
                }}
            """)
        elif parent == "MembersWindow":
            self.setStyleSheet(f"""
                QPushButton {{
                    background-color: {Color.GRAY.value};
                    border: none;
                }}
                QPushButton:hover {{
                    background-color: {Color.LIGHT_ORANGE.value};
                }}
                QPushButton:pressed {{
                    background-color: {Color.DARK_ORANGE.value};
                }}
            """)
        elif parent == "TeamsWindow":
            self.setStyleSheet(f"""
                QPushButton {{
                    background-color: {Color.GRAY.value};
                    border: none;
                }}
                QPushButton:hover {{
                    background-color: {Color.LIGHT_BLUE_1.value};
                }}
                QPushButton:pressed {{
                    background-color: {Color.LIGHT_BLUE_2.value};
                }}
            """)
        elif parent == "VisitsWindow":
            self.setStyleSheet(f"""
                QPushButton {{
                    background-color: {Color.GRAY.value};
                    border: none;
                }}
                QPushButton:hover {{
                    background-color: {Color.LIGHT_PINK.value};
                }}
                QPushButton:pressed {{
                    background-color: {Color.DARK_PINK.value};
                }}
            """)
        else:
            self.setStyleSheet(f"""
                QPushButton {{
                    background-color: {Color.GRAY.value};
                    border: none;
                }}
                QPushButton:hover {{
                    background-color: {Color.LIGHT_PURPLE.value};
                }}
                QPushButton:pressed {{
                    background-color: {Color.MIDDLE_PURPLE.value};
                }}
            """)
        # SET THE BORDER TO BE FLAT
        self.setFlat(True)

        # EACH BUTTON HAS AN IMAGE IN IT AS AN ICON
        self.icon_path = icon_path
        self.setIcon(QIcon(icon_path))
        self.setIconSize(QSize(40, 40))

        # REMOVE THE TEXT, JSUT THE ICON CENTERED
        self.setText("")
        
        

