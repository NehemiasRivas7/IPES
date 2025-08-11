from .bd import Base
from sqlalchemy import Column, String, INTEGER, Boolean, CHAR, ForeignKey, Date, Time

class Visit(Base):
    __tablename__ = "visit"

    vis_id = Column("VIS_ID", INTEGER, primary_key = True)
    vis_date = Column("VIS_DATE",Date, nullable = False)
    vis_time = Column("VIS_TIME", Time, nullable = False)
    vis_completed = Column("VIS_COMPLETED", Boolean, nullable = False)
    team_id = Column('TEAM_ID', INTEGER, ForeignKey('team.TEAM_ID'), nullable = True)

    # ATTRIBUTES OF THE MODEL VISIT
    def get_dict(self):
        visit = {}
        visit["vis_id"] = self.vis_id
        visit["vis_date"] = self.vis_date
        visit["vis_time"] = self.vis_time
        visit["vis_completed"] = self.vis_completed
        visit["team_id"] = self.team_id

        return visit
    
    
