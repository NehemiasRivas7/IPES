from .bd import Base
from sqlalchemy import Column, INTEGER, ForeignKey

class TeamMember(Base):
    __tablename__ = "team_member"

    # ATTRIBUTES OF TeamMember CLASS
    tm_id = Column("TM_ID", INTEGER, primary_key = True)
    id = Column('ID', INTEGER, ForeignKey('member.ID'), nullable = False)
    team_id = Column('TEAM_ID', INTEGER, ForeignKey('team.TEAM_ID'), nullable = True)

    # EACH REGISTER AS A DICT
    def get_dict(self):
        tm = {}
        tm["tm_id"] = self.tm_id
        tm["id"] = self.id
        tm["team_id"] = self.team_id

        return tm
    

    