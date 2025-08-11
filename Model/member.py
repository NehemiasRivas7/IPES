from .bd import Base
from sqlalchemy import Column, String, INTEGER, Boolean, CHAR, ForeignKey, Date
class Member(Base):
    
    __tablename__ = "member"

    # ATTRIBUTES
    id = Column("ID", INTEGER, primary_key = True)
    name = Column("NAME", String(30), nullable = False)
    lastname = Column("LASTNAME", String(30), nullable = False)
    age = Column("AGE", INTEGER, nullable = False)
    birthdate = Column("BIRTHDATE", Date)
    gender = Column("GENDER", Boolean, nullable = False)
    email = Column("EMAIL", String(50), nullable = True)
    phone = Column("PHONE", CHAR(8), nullable = True)
    add_id = Column('ADD_ID', INTEGER, ForeignKey('address.ADD_ID'), nullable = True)


    # GET THE MEMBERS
    def get_dict(self):
        member = {}
        member["id"] = self.id
        member["name"] = self.name
        member["lastname"] = self.lastname
        member["age"] = self.age
        member["birthdate"] = self.birthdate
        member["gender"] = self.gender
        member["email"] = self.email
        member["phone"] = self.phone
        member["add_id"] = self.add_id
        return member
    
   

   