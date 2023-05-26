import datetime

class Incident:
    def __init__(self, incident_id, date, description, data_status):
        self.incident_id = incident_id
        self.date = date
        self.description = description
        self.data_status = data_status # 'Available' or 'Missing'

class IncidentDatabase:
    def __init__(self):
        self.incidents = []

    def add_incident(self, incident_id, description, data_status):
        incident = Incident(incident_id, datetime.datetime.now(), description, data_status)
        self.incidents.append(incident)
        print(f"Incident {incident_id} added.")

    def recover_incident(self, incident_id):
        for incident in self.incidents:
            if incident.incident_id == incident_id and incident.data_status == 'Missing':
                incident.data_status = 'Available'
                print(f"Incident {incident_id} recovered.")
                return

        print(f"No missing incident found with ID {incident_id}.")

# Sample usage
if __name__ == "__main__":
    incident_db = IncidentDatabase()

    incident_db.add_incident("INC001", "Mass shooting incident", "Missing")
    incident_db.add_incident("INC002", "Robbery incident", "Available")

    incident_db.recover_incident("INC001")
