from flask import Flask, request, jsonify
from flask_cors import CORS
from twilio.twiml.messaging_response import MessagingResponse
from core.chatbot import chatbot_response
from core.order_manager import place_order, confirm_order
from core.menu import get_menu
from core.twilio_whatsapp import send_whatsapp_message

# Initialize Flask App
app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET', 'POST'])
def bot():
    """Handles incoming WhatsApp messages via Twilio."""
    if request.method == "GET":
        return "Webhook Verified!", 200

    incoming_msg = request.values.get("Body", "").strip().lower()
    user = request.values.get("From", "")
    response = MessagingResponse()
    msg = response.message()


    if "menu" in incoming_msg:
        msg.body(get_menu())
    elif "order" in incoming_msg:
        order_details = incoming_msg.replace("order", "").strip().lower()
        msg.body(place_order(user, order_details))
    elif "confirm" in incoming_msg:
        msg.body(confirm_order(user))
    else:
        # Calls chatbot.py for greetings, help, and AI responses
        msg.body(chatbot_response(incoming_msg))
    
    return str(response)

@app.route('/send', methods=['POST'])
def send_message():
    """Sends a message using Twilio WhatsApp API."""
    data = request.get_json()
    to_number = data.get('to')
    message_body = data.get('message')

    if not to_number or not message_body:
        return jsonify({'status': 'error', 'message': 'Missing "to" or "message" parameter.'}), 400
    
    return send_whatsapp_message(to_number, message_body)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
