from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, 
                           QTableWidget, QTableWidgetItem, QPushButton,
                           QLabel, QLineEdit, QFormLayout, QMessageBox,
                           QHeaderView)
from PyQt6.QtCore import Qt
from Controller.municipality_controller import MunicipalityController
from View.tools.colors import Color

class MunicipalityWidget(QWidget):
    def __init__(self):
        super().__init__()
        
        # Inicializar controlador
        self.controller = MunicipalityController()
        
        # Configurar layout principal
        main_layout = QHBoxLayout()
        self.setLayout(main_layout)
        
        # Panel izquierdo (tabla)
        left_panel = QWidget()
        left_layout = QVBoxLayout()
        left_panel.setLayout(left_layout)
        
        # Título de la sección
        title = QLabel("Municipios")
        title.setStyleSheet(f"""
            color: {Color.WHITE.value};
            font-size: 24px;
            font-weight: bold;
            margin: 10px;
        """)
        left_layout.addWidget(title)
        
        # Crear tabla
        self.table = QTableWidget(0, 2)
        self.table.setHorizontalHeaderLabels(["ID", "Nombre"])
        self.table.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        self.table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.table.selectionModel().selectionChanged.connect(self.on_selection_change)
        left_layout.addWidget(self.table)
        
        # Panel derecho (formulario)
        right_panel = QWidget()
        right_layout = QVBoxLayout()
        right_panel.setLayout(right_layout)
        
        # Formulario
        form = QFormLayout()
        
        # Campos del formulario
        self.id_field = QLineEdit()
        self.id_field.setEnabled(False)  # ID es autogenerado
        self.name_field = QLineEdit()
        
        form.addRow("ID:", self.id_field)
        form.addRow("Nombre:", self.name_field)
        
        # Contenedor del formulario
        form_container = QWidget()
        form_container.setLayout(form)
        right_layout.addWidget(form_container)
        
        # Botones
        button_layout = QHBoxLayout()
        
        self.add_btn = QPushButton("Añadir")
        self.update_btn = QPushButton("Actualizar")
        self.delete_btn = QPushButton("Eliminar")
        self.clear_btn = QPushButton("Limpiar")
        
        # Conectar botones con sus funciones
        self.add_btn.clicked.connect(self.add_municipality)
        self.update_btn.clicked.connect(self.update_municipality)
        self.delete_btn.clicked.connect(self.delete_municipality)
        self.clear_btn.clicked.connect(self.clear_form)
        
        # Estilos de los botones
        button_style = f"""
            QPushButton {{
                background-color: {Color.MIDDLE_PURPLE.value};
                color: {Color.WHITE.value};
                border: none;
                padding: 5px 10px;
                border-radius: 3px;
            }}
            QPushButton:hover {{
                background-color: {Color.LIGHT_PURPLE.value};
            }}
        """
        self.add_btn.setStyleSheet(button_style)
        self.update_btn.setStyleSheet(button_style)
        self.delete_btn.setStyleSheet(button_style)
        self.clear_btn.setStyleSheet(button_style)
        
        # Deshabilitar botones inicialmente
        self.update_btn.setEnabled(False)
        self.delete_btn.setEnabled(False)
        
        button_layout.addWidget(self.add_btn)
        button_layout.addWidget(self.update_btn)
        button_layout.addWidget(self.delete_btn)
        button_layout.addWidget(self.clear_btn)
        
        button_container = QWidget()
        button_container.setLayout(button_layout)
        right_layout.addWidget(button_container)
        
        # Añadir espacio flexible
        right_layout.addStretch()
        
        # Añadir paneles al layout principal
        main_layout.addWidget(left_panel, 2)
        main_layout.addWidget(right_panel, 1)
        
        # Cargar datos iniciales
        self.load_data()
    
    def load_data(self):
        """Cargar datos desde la base de datos"""
        # Limpiar tabla
        self.table.setRowCount(0)
        
        # Obtener municipios
        municipalities = self.controller.get_all_municipalities()
        
        # Llenar tabla
        for i, municipality in enumerate(municipalities):
            self.table.insertRow(i)
            self.table.setItem(i, 0, QTableWidgetItem(str(municipality.mun_id)))
            self.table.setItem(i, 1, QTableWidgetItem(municipality.mun_munipality))
    
    def on_selection_change(self, selected, deselected):
        """Manejar cambio en la selección de la tabla"""
        # Verificar si hay fila seleccionada
        if selected.indexes():
            # Habilitar botones
            self.update_btn.setEnabled(True)
            self.delete_btn.setEnabled(True)
            
            # Obtener fila seleccionada
            row = selected.indexes()[0].row()
            
            # Llenar formulario
            self.id_field.setText(self.table.item(row, 0).text())
            self.name_field.setText(self.table.item(row, 1).text())
        else:
            # Deshabilitar botones si no hay selección
            self.update_btn.setEnabled(False)
            self.delete_btn.setEnabled(False)
    
    def add_municipality(self):
        """Añadir municipio"""
        name = self.name_field.text().strip()
        
        if not name:
            QMessageBox.warning(self, "Error de Validación", "El nombre del municipio no puede estar vacío")
            return
        
        # Añadir municipio
        result = self.controller.add_municipality(name)
        
        if result:
            # Recargar datos
            self.load_data()
            
            # Limpiar formulario
            self.clear_form()
            
            QMessageBox.information(self, "Éxito", "Municipio añadido correctamente")
    
    def update_municipality(self):
        """Actualizar municipio"""
        # Obtener valores del formulario
        id_text = self.id_field.text()
        name = self.name_field.text().strip()
        
        if not id_text or not name:
            QMessageBox.warning(self, "Error de Validación", "Todos los campos deben estar llenos")
            return
        
        # Actualizar municipio
        result = self.controller.update_municipality(int(id_text), name)
        
        if result:
            # Recargar datos
            self.load_data()
            
            # Limpiar formulario
            self.clear_form()
            
            QMessageBox.information(self, "Éxito", "Municipio actualizado correctamente")
    
    def delete_municipality(self):
        """Eliminar municipio"""
        # Obtener ID del formulario
        id_text = self.id_field.text()
        
        if not id_text:
            return
        
        # Confirmar eliminación
        reply = QMessageBox.question(self, "Confirmar Eliminación", 
                                   "¿Está seguro que desea eliminar este municipio?",
                                   QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        
        if reply == QMessageBox.StandardButton.Yes:
            # Eliminar municipio
            result = self.controller.delete_municipality(int(id_text))
            
            if result:
                # Recargar datos
                self.load_data()
                
                # Limpiar formulario
                self.clear_form()
                
                QMessageBox.information(self, "Éxito", "Municipio eliminado correctamente")
    
    def clear_form(self):
        """Limpiar formulario"""
        self.id_field.clear()
        self.name_field.clear()
        self.update_btn.setEnabled(False)
        self.delete_btn.setEnabled(False)
        self.table.clearSelection()