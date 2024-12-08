from flask import Blueprint, current_app, request, jsonify
from pydantic import ValidationError
from domain.dto.eventResponseDto import EventResponseDto
from domain.dto.clientTransactionDto import ClientTransactionDto
from domain.service.Event_handler import EventHandler

api = Blueprint("api", __name__)

@api.route("/event", methods = ["POST"])
def handle_user_event() -> dict:
    current_app.logger.info("Handling user event")
    data = request.get_json()
    
    try:
        event_data = ClientTransactionDto(**data)
        result = EventHandler.handle_event(event_data)

    except ValidationError as e:
        return jsonify({"error": e.errors()}), 400
    
    current_app.logger.info(f"Received event: {event_data}, returning {result}")
    return result