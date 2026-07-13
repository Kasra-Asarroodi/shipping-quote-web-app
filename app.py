from flask import Flask
import os
from dotenv import load_dotenv
from database import create_enquiry_table
load_dotenv()

app = Flask(__name__)


SECRET_KEY = os.environ.get("SECRET_KEY")
ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD")


if not SECRET_KEY:
    raise RuntimeError("SECRET_KEY is missing from the .env file")

if not ADMIN_PASSWORD:
    raise RuntimeError("ADMIN_PASSWORD is missing from the .env file")

app.secret_key = SECRET_KEY


create_enquiry_table()



import app_routes

if __name__ == "__main__":

   app.run(debug=True)



