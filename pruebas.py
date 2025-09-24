import os
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt6.QtGui import QFontDatabase, QFont
from PyQt6.QtCore import Qt

def get_project_root():
    current_path = os.path.dirname(os.path.abspath(__file__))
    while os.path.basename(current_path) != "IPES":
        parent = os.path.dirname(current_path)
        if parent == current_path:
            raise Exception("No se pudo encontrar la carpeta raíz del proyecto IPES")
        current_path = parent
    return current_path

def load_custom_font(font_relative_path):
    project_root = get_project_root()
    font_absolute_path = os.path.join(project_root, font_relative_path)
    
    print(f"Intentando cargar fuente desde: {font_absolute_path}")
    
    font_id = QFontDatabase.addApplicationFont(font_absolute_path)
    if font_id == -1:
        print(f"No se pudo cargar la fuente: {font_absolute_path}")
        return None
    
    font_families = QFontDatabase.applicationFontFamilies(font_id)
    if not font_families:
        print("No se encontraron familias de fuentes")
        return None
        
    font_family = font_families[0]
    print(f"Fuente cargada correctamente: {font_family}")
    return QFont(font_family, 24)  # Tamaño grande para que sea visible

# El error principal está aquí - NO debes crear widgets antes de QApplication
# Elimina estas líneas:
# font = load_custom_font("View/tools/penumbraserifstd-semibold.otf")
# label = QLabel("Texto con fuente personalizada")
# if font:
#     label.setFont(font)
# label.show()

if __name__ == "__main__":
    # 1. Primero crear la aplicación
    app = QApplication([])
    
    # 2. Crear una ventana principal con tamaño
    window = QMainWindow()
    window.setWindowTitle("Prueba de Fuente")
    window.setMinimumSize(500, 300)
    
    # 3. Cargar la fuente
    font = load_custom_font("View/tools/penumbraserifstd-semibold.otf")
    
    # 4. Crear y configurar el label DESPUÉS de crear QApplication
    label = QLabel("Texto con fuente personalizada")
    label.setAlignment(Qt.AlignmentFlag.AlignCenter)
    
    if font:
        label.setFont(font)
    else:
        # Mostrar un mensaje de error si la fuente no carga
        label.setText("ERROR: No se pudo cargar la fuente.\nVerifica la ruta del archivo.")
        label.setStyleSheet("color: red; font-size: 18px;")
    
    # 5. Añadir el label a la ventana
    window.setCentralWidget(label)
    
    # 6. Mostrar la ventana
    window.show()
    
    # 7. Iniciar el bucle de eventos
    app.exec()