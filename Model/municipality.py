from .bd import Base
from sqlalchemy import Column, String, INTEGER   

class Municipality(Base):
    
    __tablename__ = 'municipality'

    # ATTRIBUTES OF THE TABLE 
    mun_id = Column('MUN_ID', INTEGER, primary_key=True)
    mun_munipality = Column('MUN_MUNICIPALITY', String(30), nullable = False)

    # REPRESENTATION OF THE OBJECT
    def __repr__(self):
        return f" MUNICIPALITY\nMUN_ID: {self.mun_id}\n MUNICIPALITY: {self.mun_munipality}\n"

