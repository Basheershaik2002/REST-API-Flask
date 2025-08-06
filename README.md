# REST API with Flask + Streamlit Frontend

This project demonstrates how to build a simple RESTful API using Flask and  i connect it with a frontend built using Streamlit. The API allows users to be added, updated, and retrieved using standard HTTP methods.

### Live Deployment

### Streamlit Frontend (Live Link):  
**https://rest-api-flask-7fug8ilmae679w7c3xfr7l.streamlit.app/**



#### Features

Add User – Submit a username and email
Get Users – View all users in the system
Update User – Update an existing user’s email
Frontend – Built using Streamlit for easy interaction

#### Tech Stack

Backend: Python, Flask
Frontend: Streamlit
API Testing: Python requests module
Deployment: Streamlit Cloud (Frontend)

Sample Output

When running test_api.py (to test API endpoints), output is as follows:

- ADDING USER:
201 {'message': 'User basheer added'}

- GETTING ALL USERS:
200 {'basheer': {'email': 'basheer@example.com'}}

- UPDATING USER:
200 {'message': 'User basheer updated'}

- GETTING ALL USERS AFTER UPDATE:
200 {'basheer': {'email': 'newemail@example.com'}}

On the Flask server console, logs will look like:

[SERVER LOG] ➕ Added user: basheer  
[SERVER LOG] 📥 Fetched all users  
[SERVER LOG] 🔄 Updated user: basheer  

🛠️ How to Run Locally

1️. Clone the Repository

git clone https://github.com/yourusername/rest-api-task.git  
cd rest-api-task

2️. Install Dependencies

pip install -r requirements.txt

3️. Run Flask Server (Backend)

python app.py

API runs on: http://127.0.0.1:5000

4️. Run Streamlit App (Frontend)

streamlit run frontend.py

UI opens in browser at: http://localhost:8501

### Project Structure

rest-api-task/
├── app.py              # Flask backend API
├── test_api.py         # Script to test the REST endpoints
├── frontend.py         # Streamlit frontend UI
├── requirements.txt    # List of required Python packages
└── README.md           # Documentation


### UI Overview (Frontend)

The Streamlit interface includes:
- Form to add a new user
- Option to update existing user email
- Real-time display of all users after actions

### Important Links

🚀 Live Frontend (Streamlit):**https://rest-api-flask-7fug8ilmae679w7c3xfr7l.streamlit.app/  **
🗃️ Backend: Flask (Run Locally)
