from PyQt6.QtWidgets import QMainWindow, QTabWidget, QLabel, QWidget, QHBoxLayout, QVBoxLayout
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt
from View.municipality import MunicipalityWidget
from View.tools.colors import Color
from View.tools.button_img_menu import MenuImgButton

# Import your widgets later
# from View.widgets.municipality_widget import MunicipalityWidget
# from View.widgets.member_widget import MemberWidget
# etc.

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("IPES Management System")
        self.setMinimumSize(800, 600)

        # SET UP OF THE EXTERNAL CONTAINER
        self.widget_contenedor = QWidget()
        self.widget_contenedor.setStyleSheet(f"background-color: {Color.DARK_PURPLE.value};")
        self.widget_contenedor.setContentsMargins(0,0,0,0)
        self.setCentralWidget(self.widget_contenedor)

        self.layout_contenedor = QHBoxLayout()
        self.layout_contenedor.setContentsMargins(0,0,0,0)
        self.layout_contenedor.setSpacing(0)
        self.widget_contenedor.setLayout(self.layout_contenedor)

        # SET ICON OF THE APPLICATION
        self.setWindowIcon(QIcon("View/tools/img/logo.png"))


        # CREATE TWO MAIN WIDGETS: 2 LAYOUNTS. 
        # THE FIRST ONE: IS TO SET  BAR OF  BUTTONS TO NAVEGATE TO THE DIFFERENT SECTIONS
        # THE SECOND ONE: IS TO SET THE CONTENT OF THE SELECTED SECTION
        # BORTH LAYOUTS MUST BE ADDED TO THE MAIN CONTAINER

        # MAIN WIDGETS
        ## LEFT WIDGET [BAR OF BUTTONS]
        self.left_widget_contenedor = QWidget()
        self.left_widget_contenedor.setStyleSheet(f"background-color: {Color.GRAY.value};")
        self.left_widget_contenedor.setFixedWidth(80)
        self.left_widget_contenedor.setContentsMargins(0,0,0,0)
         


        # LAYOUT OF THE LEFT WIDGET
        self.left_layout_contenedor = QVBoxLayout()
        self.left_layout_contenedor.setContentsMargins(0,0,0,0)
        self.left_layout_contenedor.setSpacing(0)
        self.left_widget_contenedor.setLayout(self.left_layout_contenedor)
      
        # THE 7 IMAGE BUTTONS FOR THE LEFT BAR[ THE REST ARE TO BE ADDED]
        self.btn_main = MenuImgButton("View/tools/img/logo.png", "MainWindow")
        self.btn_members = MenuImgButton("View/tools/img/members.png", "MembersWindow")
        self.btn_teams = MenuImgButton("View/tools/img/teams.png", "TeamsWindow")
        self.btn_visits = MenuImgButton("View/tools/img/visits.png", "VisitsWindow")
        self.btn_services = MenuImgButton("View/tools/img/services.png", "ServicesWindow")
        self.btn_calendar = MenuImgButton("View/tools/img/calendar.png", "CalendarWindow")
        self.btn_privileges = MenuImgButton("View/tools/img/privileges.png", "PrivilegesWindow")
        # ADDING THE BUTTONS TO THE LEFT WIDGET
        self.left_layout_contenedor.addWidget(self.btn_main)
        self.left_layout_contenedor.addWidget(self.btn_members)
        self.left_layout_contenedor.addWidget(self.btn_teams)
        self.left_layout_contenedor.addWidget(self.btn_visits)
        self.left_layout_contenedor.addWidget(self.btn_services)
        self.left_layout_contenedor.addWidget(self.btn_calendar)
        self.left_layout_contenedor.addWidget(self.btn_privileges)


        # ADDS THE LEFT WIDGET TO THE MAIN CONTAINER
        self.layout_contenedor.addWidget(self.left_widget_contenedor, 0, Qt.AlignmentFlag.AlignLeft)


        # RIGHT WIDGET - CONTENT AREA
        self.right_widget_contenedor = QWidget()
        self.right_widget_contenedor.setContentsMargins(0,0,0,0)
        
        # Layout for right widget
        self.right_layout_contenedor = QVBoxLayout()
        self.right_layout_contenedor.setContentsMargins(0,0,0,0)
        self.right_layout_contenedor.setSpacing(0)
        self.right_widget_contenedor.setLayout(self.right_layout_contenedor)
        
        # Stacked widget to switch between views
        self.content_widget = QWidget()
        self.content_layout = QVBoxLayout()
        self.content_widget.setLayout(self.content_layout)
        
        # Set default view (Municipality)
        self.municipality_widget = MunicipalityWidget()
        self.content_layout.addWidget(self.municipality_widget)
        
        # Add content widget to right panel
        self.right_layout_contenedor.addWidget(self.content_widget)
        
        # Add right widget to main container
        self.layout_contenedor.addWidget(self.right_widget_contenedor, 1)
        
        # Connect buttons
        self.connect_buttons()
        
    def connect_buttons(self):
        """Connect menu buttons to their respective actions"""
        self.btn_main.clicked.connect(self.show_main)
        self.btn_members.clicked.connect(self.show_members)
        self.btn_teams.clicked.connect(self.show_teams)
        self.btn_visits.clicked.connect(self.show_visits)
    
    def clear_content(self):
        """Clear the content layout"""
        # Remove all widgets from content layout
        while self.content_layout.count():
            item = self.content_layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.hide()
                self.content_layout.removeWidget(widget)
    
    def show_main(self):
        """Show home screen"""
        self.clear_content()
        self.municipality_widget = MunicipalityWidget()
        self.content_layout.addWidget(self.municipality_widget)
    
    def show_members(self):
        """Show members screen"""
        self.clear_content()
        # Here you would create and add your MemberWidget
        label = QLabel("Members section - Under construction")
        label.setStyleSheet("color: white; font-size: 24px;")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.content_layout.addWidget(label)
    
    def show_teams(self):
        """Show teams screen"""
        self.clear_content()
        # Here you would create and add your TeamWidget
        label = QLabel("Teams section - Under construction")
        label.setStyleSheet("color: white; font-size: 24px;")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.content_layout.addWidget(label)
    
    def show_visits(self):
        """Show visits screen"""
        self.clear_content()
        # Here you would create and add your VisitWidget
        label = QLabel("Visits section - Under construction")
        label.setStyleSheet("color: white; font-size: 24px;")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.content_layout.addWidget(label)