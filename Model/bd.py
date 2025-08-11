from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declarative_base

# GLOBAL VARIABLES 

# SPECIFIC DATABASE
SERVER_NAME = "localhost"
DATABSE_NAME = "ipes"
PASSWORD = "12345"

# DATABSE URL
DATABASE_URL = None
# ENGINE TO CONNECT TO THE DATABASE
ENGINE = None

# TEMPORARY SESSION
SessionLocal = None

# BASE CLASS FOR MODELS
Base = None


# METHOD TO CREATE CONNECTION TO THE DATABASE [ENGINE], START A SESSION AND CREATE THE BASE CLASS
def create_database_connection(password):

    # MAKE GLOBAL VARIABLES ACCESSIBLE
    global DATABASE_URL, ENGINE, Base, PASSWORD, SessionLocal

    # SET PASSWORD 
    PASSWORD = password

    # CREATE DATABASE URL
    DATABASE_URL = f"mysql+pymysql://root:{PASSWORD}@{SERVER_NAME}/{DATABSE_NAME}"

    # CREATE ENGINE
    ENGINE = create_engine(DATABASE_URL, echo = False)
    # ECHO IS SET TO FALSE TO AVOID LOGGING QUERIES

    # CREATES A TEMPORARY SESSION
    SessionLocal = sessionmaker(bind=ENGINE, autocommit=False, autoflush=False)
    # AUTOCOMMIT IS SET TO FALSE TO MANAGE TRANSACTIONS MANUALLY
    # AUTOFLUSH IS SET TO FALSE TO AVOID AUTOMATIC FLUSHING OF CHANGES

    # TEST TO VERIFY CONNECTION
    try:
        test_session = SessionLocal()
        test_session.close()
        print("Database connection established successfully.")
    except Exception as e:
        print(f"Database connection could not be done with success. Error name: {e}")

# NOW, THE CLASS BASE IS CREATED
Base = declarative_base()

# EXAMPLE USAGE        
create_database_connection("12345")
    
# METHOD TO GET ALL REGISTERS FROM A MODEL
def get_all(db: Session, model):
    """
    READS AND RETURNS ALL THE REGISTER FROM A TABLE .
    :param db: THE DATA BASE SESSION
    :param modelo_obj: THE SPEFICI ENTITIES WHOSE DATA IS ASKED
    """
    return db.query(model).all()
# METHOD TO GET A REGISTER FROM A TABLE BY ID
def get_by_id(db: Session, model, id):
    """
    READS AND RETURNS THE SPECIFIC REGISTER ASKED BY ID .
    :param db: THE DATA BASE SESSION
    :param modelo_obj: THE SPEFICIC ID OF THE REGISTER WHOSE DATA IS ASKED
    """
    return db.query(model).get(id)


# METHOD TO ADD A REGISTER 
def add(db: Session, model_object):
    """
    ADDS A REGISTER TO THE MODEL
    :param db: ADDS IT TO THE DATA BASE GIVEN
    :param model: TABLE 
    :instance: AN OBJECT OF THE SPECIFIED CLASS [THE RESPECTIVE TABLE]
    FOR INSTANCE, model_object can be MEMBER(atribute1 = "somethig")
    """
    db.add(model_object)
    db.commit()
    db.refresh(model_object)

    return model_object
    # model_object is re

# METHOD TO UPDATE A REGISTER
def update(db: Session, model_object):
    """
    UPDATES A REGISTER IN THE MODEL
    :param db: THE DATA BASE SESSION
    :param model_object: AN OBJECT OF THE SPECIFIED CLASS [THE RESPECTIVE TABLE]
    FOR INSTANCE, model_object can be MEMBER(atribute1 = "somethig")
    """

    merged_object = db.merge(model_object)  # Merge with session
    db.commit()
    db.refresh(merged_object)  # Refresh the merged object
    return merged_object

# METHOD TO DELETE A REGISTER
def delete(db: Session, model_object):
    """
    DELETES A REGISTER IN THE MODEL
    :param db: THE DATA BASE SESSION
    :param model_object: AN OBJECT OF THE SPECIFIED CLASS [THE RESPECTIVE TABLE]
    FOR INSTANCE, model_object can be MEMBER(atribute1 = "somethig")
    """
    merged_object = db.merge(model_object)
    db.delete(merged_object)
    db.commit()






