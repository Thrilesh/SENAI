from flask import Blueprint, jsonify, request
from data import people, tickets, assign_ticket_to_person, get_person_by_id
import uuid

tickets_bp = Blueprint('tickets', __name__)

def generate_unique_ticket_id():
    return str(uuid.uuid4())

current_person_index = 0

def assign_person_round_robin():
    global current_person_index
    person = people[current_person_index]
    current_person_index = (current_person_index + 1) % len(people)
    return person['id']

@tickets_bp.route('/ticket', methods=['POST'])
def create_ticket():
    data = request.get_json()
    
    user_id = data['user_id']
    issue = data['issue']
    
    ticket_id = generate_unique_ticket_id()
    assigned_to = assign_person_round_robin()
    
    assign_ticket_to_person(ticket_id, assigned_to)
    
    response_data = {
        "ticket_id": ticket_id,
        "assigned_to": assigned_to
    }
    
    response = {
        "message": "Ticket created and assigned successfully",
        "success": True,
        "data": response_data
    }
    
    return jsonify(response), 201
