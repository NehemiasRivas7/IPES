from Model.bd import SessionLocal, get_all, get_by_id, add, update, delete
from Model.municipality import Municipality

class MunicipalityController:
    def __init__(self):
        self.session = SessionLocal()
        
    def get_all_municipalities(self):
        """Obtener todos los municipios"""
        try:
            return get_all(self.session, Municipality)
        except Exception as e:
            print(f"Error al obtener municipios: {e}")
            return []
            
    def get_municipality_by_id(self, mun_id):
        """Obtener un municipio por su ID"""
        try:
            return get_by_id(self.session, Municipality, mun_id)
        except Exception as e:
            print(f"Error al obtener el municipio: {e}")
            return None
            
    def add_municipality(self, name):
        """Añadir un nuevo municipio"""
        try:
            new_municipality = Municipality(mun_munipality=name)
            return add(self.session, new_municipality)
        except Exception as e:
            print(f"Error al añadir el municipio: {e}")
            return None
            
    def update_municipality(self, mun_id, name):
        """Actualizar un municipio existente"""
        try:
            municipality = Municipality(mun_id=mun_id, mun_munipality=name)
            return update(self.session, municipality)
        except Exception as e:
            print(f"Error al actualizar el municipio: {e}")
            return None
            
    def delete_municipality(self, mun_id):
        """Eliminar un municipio"""
        try:
            municipality = Municipality(mun_id=mun_id)
            delete(self.session, municipality)
            return True
        except Exception as e:
            print(f"Error al eliminar el municipio: {e}")
            return False
            
    def __del__(self):
        """Cerrar la sesión al destruir el controlador"""
        self.session.close()