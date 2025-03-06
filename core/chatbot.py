from integrations.gemini_ai import get_gemini_response

def chatbot_response(incoming_msg):
    """Handles chatbot responses based on user input."""
    incoming_msg = incoming_msg.lower().strip()

    if incoming_msg == "hi":
        return "Hello! Welcome to Salad Restaurant.\nType for services:\n\n- menu\n- need help?"
    
    elif incoming_msg == "need help":
        return "For any query or order-related issue, please contact +911234567890."
    
    # Delegate other responses to Gemini AI
    return get_gemini_response(incoming_msg)
