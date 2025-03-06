from twilio.rest import Client
from config import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_WHATSAPP_NUMBER

# Initialize Twilio Client
twilio_client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

def send_whatsapp_message(to_number, message_body):
    """Sends a WhatsApp message using Twilio API."""
    try:
        message = twilio_client.messages.create(
            from_=TWILIO_WHATSAPP_NUMBER,
            body=message_body,
            to=to_number
        )
        return {'status': 'success', 'sid': message.sid}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}
