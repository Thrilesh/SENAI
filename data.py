people = [
    {'id': '#1', 'name': 'Alice', 'tickets_assigned': []},
    {'id': '#2', 'name': 'Bob', 'tickets_assigned': []},
    {'id': '#3', 'name': 'Charlie', 'tickets_assigned': []},
    {'id': '#4', 'name': 'David', 'tickets_assigned': []},
    {'id': '#5', 'name': 'Eve', 'tickets_assigned': []},
]

tickets = []

def assign_ticket_to_person(ticket_id, person_id):
    for person in people:
        if person['id'] == person_id:
            person['tickets_assigned'].append(ticket_id)
            break

def get_person_by_id(person_id):
    return next((person for person in people if person['id'] == person_id), None)
