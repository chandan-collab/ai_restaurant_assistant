import google.generativeai as genai
from config import GEMINI_API_KEY

#  Configure API Key
genai.configure(api_key=GEMINI_API_KEY)

def get_gemini_response(user_input):
    """Fetches AI-generated responses from Gemini AI."""
    try:
       
        model = genai.GenerativeModel("gemini-1.5-pro")

        #  Generate response from Gemini AI
        response = model.generate_content(f"Act as a Restaurant assistant. if 'ok' , 'yes' , 'thankyou' or related to this kind of messages reply 'Thankyou for choosing us' otherwise ask them to type 'menu' for menu and 'need help' for help.If adult message or pornograpy related content told user to 'we ere going to block you soon'.Answer the questions related to food or restaurant.\nUser: {user_input}")

        #  Extract and return text response
        return response.text if response and hasattr(response, "text") else "I'm sorry, I couldn't process your request."

    except Exception as e:
        print("Google Gemini API error:", e)
        return "Sorry, I couldn't process your request. Please try again later."
