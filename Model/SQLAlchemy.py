from Model.bd import ENGINE, Base, SessionLocal, get_all, add, update,  delete
from Model.municipality import Municipality
from Model.address import Address
from Model.member import Member
from Model.team import Team
from Model.team_member import TeamMember
from Model.visit import Visit

# CREATE ALL TABLES IN THE DATABASE
Base.metadata.create_all(bind= ENGINE)

# CREATE A TEMPORARY SESSION
session = SessionLocal()

# MAKE AN INSTANCE OF 
# Example usage of the Municipality model
def get_municipalities():
    try:
        municipalities = get_all(session, Municipality)
        return municipalities
    except Exception as e:
        
        print(f"An error occurred while retrieving municipalities: {e}")
# EXAMPLE OF USAGE OF THE ADDRESS MODEL
def get_addresses():
    try:
        addresses = get_all(session, Address)
        return addresses
    except Exception as e:
        print(f"Sorry. Error: {e}")

# EXAMPLE OF USGAE OF THE MEMBERS M0DEL
def get_members():
    try:
        members = get_all(session, Member)
        return members
    except Exception as e:
        print(f" Error. {e}")

# EXAMPLE OF USGAE OF TEAMS M0DEL
def get_teams():
    try:
        teams = get_all(session, Team)
        return teams
    except Exception as e:
        print(f"An error ocureed. In fact, the error states: {e}")
# EXAMPLE TO GET TEAM MEMBERS
def get_team_members():
    try:
        team_members = get_all(session, TeamMember)
        return team_members
    except Exception as e:
        print(f"Alright, no. Nothing right. Error: {e}")

# EXAMPLE TO GET THE VISITS
def get_visits():
    try:
        visits = get_all(session, Visit)
        return visits
    except Exception as e:
        print(f"Error: {e}")

# Example usage
if __name__ == "__main__":
   # Get all municipalities
    #add(session, Municipality(mun_munipality = "New Municipality"))
    #update(session, Municipality(mun_id = 15, mun_munipality = "Updated Municipality"))
    #delete(session, Municipality(mun_id = 11))
    #add(session, Address(add_address = "SANTA CLARA", mun_id = 10))
    #delete(session, Member(id = 21, lastname = "Umaña", gender = False ))
    
    municipalities = get_municipalities()
    addresses = get_addresses()
    members = get_members()
    teams = get_teams()
    team_members = get_team_members()
    visits = get_visits()

    for municipality in municipalities:
        print(municipality)

    for address in addresses:
        print(address)
    
    for member in members:
        member = member.get_dict()
        print(member)

    for team in teams:
        team = team.get_dict()
        print(team)

    for team_member in team_members:
        tm = team_member.get_dict()
        print(tm)

    for visit in visits:
        visit = visit.get_dict()
        print(visit)

    # Close the session
    session.close()