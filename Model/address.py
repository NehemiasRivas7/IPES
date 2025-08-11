from .bd import Base
from sqlalchemy import Column, String, INTEGER, ForeignKey   

class Address(Base):

    __tablename__ = 'address'

    
    # ATTRIBUTES OF THE CLASS
    add_id = Column('ADD_ID', INTEGER, primary_key= True)
    add_address = Column('ADD_ADDRESS', String(100))
    mun_id = Column('MUN_ID', INTEGER, ForeignKey('municipality.MUN_ID'), nullable = False)

    # REPRESENTATION OF THE OBJECT
    def __repr__(self):
        return f"ADDRESS\nADD_ID: {self.add_id}\nMUN_ID: {self.mun_id}\nADD_ADDRESS: {self.add_address}"