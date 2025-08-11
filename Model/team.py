from .bd import Base
from sqlalchemy import Column, String, INTEGER, Boolean, CHAR, ForeignKey, Date

class Team(Base):
    __tablename__ = "team"

    # ATTRIBUTES OF TEAM
    team_id = Column("TEAM_ID", INTEGER, primary_key = True)
    team_name = Column("TEAM_NAME", String(20), nullable = False)
    team_family = Column("TEAM_FAMILY", Boolean, nullable = False)
    add_id = Column('ADD_ID', INTEGER, ForeignKey('address.ADD_ID'), nullable = True)

    # EACH REGISTER AS A DICT
    def get_dict(self):

        team = {}
        team["team_id"] = self.team_id
        team["team_name"] = self.team_name
        team["team_family"] = self.team_family
        team["add_id"] = self.add_id

        return team