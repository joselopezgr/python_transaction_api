from flask import Blueprint, current_app, request, jsonify
from pydantic import ValidationError
from transaction_challenge.domain.dto.clientTransactionDto import ClientTransactionDto
from transaction_challenge.domain.service.Event_handler import EventHandler

api = Blueprint("api", __name__)
# Initialize route/controller that handles the posting of events
@api.route("/event", methods=["POST"])
def handle_user_event() -> dict:
    current_app.logger.info("Handling user event")
    data = request.get_json()
    # try-except block to handle errors if anything fails at API layer
    try:
        # Validate the input using the Dto class
        event_data = ClientTransactionDto(**data)
        # Call the event handler method from domain layer
        result = EventHandler.handle_event(event_data)

    except ValidationError as e:
        current_app.logger.error(f"Validation error: {e}")
        return jsonify({"error": e.errors()}), 400
    # A log to print a succesful call to the api
    current_app.logger.info(f"Received event: {event_data}, returning {result}")
    return result
