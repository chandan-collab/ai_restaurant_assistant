AI Restaurant Chatbot

Overview

The AI Restaurant Chatbot is a WhatsApp-based 
chatbot that helps customers place orders, view menus, 
and get assistance through AI-powered responses. 
It integrates Twilio for WhatsApp messaging, OpenAI GPT 
for intelligent replies, and Flask to handle backend logic. 
Additionally, SQLite is used for storing orders efficiently.



Features ✨

✅ WhatsApp Integration – Customers can chat via WhatsApp to place orders.
✅ AI-Powered Responses – Uses OpenAI GPT for smart and interactive replies.
✅ Order Management – Stores and tracks orders in an SQLite database.
✅ Interactive Menu – Customers can view menu items and place orders seamlessly.
✅ Easy Deployment – Simple Flask API for quick and hassle-free deployment.




Requirements /Tech Stack

Before running the project, ensure you have the following installed:

1️⃣ Python 3.x – Download from python.org
2️⃣ Flask – Web framework for handling API requests.
3️⃣ Twilio Account – Required for sending and receiving WhatsApp messages.
4️⃣ OpenAI API Key – Needed for AI-generated responses.
5️⃣ SQLite – For order storage (built-in with Python).
6️⃣ Ngrok – To expose the local server to the internet.
7️⃣ Virtual Environment – To manage dependencies.
8️⃣ Vs code: Recommended code editor for development.


Install Required Packages
pip install flask twilio openai ngrok
open api key, ngrok tokens.



How It Works 
1️⃣ User sends a message via WhatsApp.
2️⃣ Flask receives and processes the message.
3️⃣ AI generates a response (if applicable).
4️⃣ Response is sent back to the user via Twilio API.
5️⃣ Orders are stored in SQLite for tracking.



## Steps
1. Create free account in [openai], [Twilio],and [Ngrok].
2. Open twilio console, register your whatsapp number. 
3. Install requirements.
4. Fill API key, twilio whatsapp number and token in app.py.
5. Run Flask App.
6. Run Ngrok on same port as Flask App.
7. Setup Ngrok URL in Whatsapp Sandbox (in Twilio console).
8. Done, chatbot is activated!! 
9. 
10. 



Future Improvements 🔮

🔹 Add payment integration (Stripe, Razorpay).
🔹 Implement user authentication for personalized experiences.
🔹 Deploy to cloud platforms (AWS, Heroku, Render) for scalability.


Contributing 🤝

Feel free to fork this repository and submit pull requests.
 Suggestions & improvements are always welcome!

📧 Contact: chandan.eloss@gmail.com