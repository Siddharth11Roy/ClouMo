RUN BACKEND - 

cd backend

venv/scripts/activate ( create one if not there )

pip install -r requirements.txt

python run.py



Structure - 

🌐 Landing Page –  intro with redirection to login, signup, and model page

🔐 Login & Signup – Secure JWT-based authentication with Flask backend

📸 Model Page

Accepts image input

Sends image to Flask backend

Model processes it and returns a result

Displays output image on the frontend
