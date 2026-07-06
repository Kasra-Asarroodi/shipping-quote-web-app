from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session, redirect
import sqlite3
import os   
import json

app = Flask(__name__)

app.secret_key = "Beograd1071@"

@app.route('/', methods=['GET', 'POST'])

def home():
    result = None
    form_data = {}
    if request.method == 'POST':
        
        action = request.form.get("action")
        sender = sender_info(request.form)
        receiver = receiver_info(request.form)
        quote = quote_info(request.form)
        promo = request.form.get("promo")
      

        result = quote["total_price"]


        if action == "calculate": 
             form_data = request.form
             


        if action == "submit":
            save_enquiry(sender, receiver, quote, promo)
            flash("Your enquiry has been submitted successfully!")

            
        
    return render_template('index.html', result=result, form_data = form_data)



def sender_info (form):
   return {"name": form.get("sender_name", ""),
           "phone":form.get("sender_phone", ""),  
           "email": form.get("sender_email","")}

  

def receiver_info(form):
    return {"name": form.get("receiver_name", ""), 
            "phone":form.get("receiver_phone", ""), 
            "email": form.get("receiver_email", ""), 
            "address":form.get("receiver_address", "")}





def quote_info(form):
    weight = float(form.get("weight", 0))
    value = float(form.get("value", 0))
    medications = int(form.get("medications", 0))
    electronics = int(form.get("electronics", 0))
    makeup = int(form.get("makeups", 0))
     

    settings = load_settings()
    promo = settings["promo"]

    weight_price = calculate_weight_price(weight)
    insurance_price = calculate_insurance(value)
    medication_price = calculate_medication_price(medications)
    electronics_price = calculate_electronic_price(electronics)
    makeup_price = calculate_makeup_price(makeup)

    total_price = calculate_total_price(
        weight_price,
        insurance_price,
        medication_price,
        electronics_price,
        makeup_price
    )

    total_price = apply_promo_discount(total_price, promo)

    return {
        "weight": weight,
        "value": value,
        "medications": medications,
        "electronics": electronics,
        "makeup": makeup,
        "weight_price": weight_price,
        "insurance_price": insurance_price,
        "total_price": total_price,
        "promo": promo
    }


def calculate_weight_price(weight):

    weight_rates = [(1,90), (2, 140), (3, 195), (4, 250), (5, 300), 
                    (6, 355), (7, 415), ( 8, 465), (9, 515), 
                    (10, 565), (11, 610), (12, 655), (13, 705), (14, 750), (15, 795),
                    (16, 840), (17, 885), (18, 930), (19, 970), (20, 1020),
                    (25, 1225) ]
    for max_weight, price in weight_rates:
       if weight <= max_weight:
           return price
    return 0


   
def calculate_insurance(value):
    
   return value / 5
   


def calculate_medication_price(medication):
 return medication * 6

def calculate_electronic_price(electronic):
   return electronic * 60

def calculate_makeup_price(makeup):
   return makeup * 6

def calculate_total_price(weight_price, insurance_price, medication_price, electronics_price, makeup_price):

   return weight_price + insurance_price + medication_price + electronics_price + makeup_price

def apply_promo_discount(total_price, promo):
    return total_price * ( 100 - promo) / 100



   


SETTING_FILE = "setting.json"




def load_settings():
    if not os.path.exists(SETTING_FILE):
        return {"promo" : 0}
    with open(SETTING_FILE, "r") as setfile:
         return json.load(setfile) 
    


def save_setting(setting):
  
  with open(SETTING_FILE, "w") as setfile:
        json.dump(setting, setfile, indent=4)

  
    

@app.route("/update_promo", methods=["POST"])
def update_promo():
    if not session.get("admin_logged_in"):
        return redirect ("/admin")
    
    promo_value = int(request.form.get("promo"))
    
    if promo_value is None or promo_value == "":
        promo_value = 0
    
    setting = load_settings()
    
    setting["promo"] = int(promo_value)
    save_setting(setting)

    return redirect("/admin/dashboard")
    


@app.route("/about")
def about():
    return render_template("Aboutus.html")


@app.route("/contact")
def contact():
    return render_template("contactus.html")


@app.route("/enquiries", methods = ["GET", "POST"])
def enquiries():
    matching_enquiries =[]

    if request.method == "POST":
        entered_email = request.form.get("email")

        all_enquiries = load_enquiries()

        for enquiry in all_enquiries:
            sender_email = enquiry["sender_email"]
            if sender_email.lower() == entered_email.lower():
                matching_enquiries.append(enquiry)

        if not matching_enquiries:
            flash("There is not matching enquiries with this email!")
            return render_template("enquiries.html", enquiries= None)
        

    return render_template("enquiries.html", enquiries=matching_enquiries)


@app.route("/info")
def info():
    return render_template("info.html")

@app.route("/admin", methods = ["GET", "POST"])
def admin_login():

    if request.method == "POST":
       admin_password = request.form["password"]

       if admin_password == "KimiaKasra1071" :
           session ["admin_logged_in"] = True
           return redirect ("/admin/dashboard")
           
    return render_template("admin_login.html")



@app.route("/admin/dashboard", methods = ["GET", "POST"])
def admin_dashboard():
    if not session.get("admin_logged_in"):
        return redirect("/admin")
    all_enquiries = load_enquiries()
    settings = load_settings()

    return render_template("admin.html", enquiries= all_enquiries, promo_rate = settings["promo"])





DB_FILE = "enquiries.db"

#creating a connection to the SQlite database
def get_connection():
    return sqlite3.connect(DB_FILE)

#creating the enquiry table
def create_enquiry_table():
    connection = get_connection()

    query = """
    CREATE TABLE IF NOT EXISTS enquiries (
        id INTEGER PRIMARY KEY AUTOINCREMENT,

        sender_name TEXT,
        sender_email TEXT,
        sender_phone TEXT,
        

        receiver_name TEXT,
        receiver_email TEXT,
        receiver_phone TEXT,
        receiver_address TEXT,

        insuranca_price INTEGER,

        weight INTEGER,
        value INTEGER,
        medications INTEGER,
        makeups INTEGER, 
        electronics INTEGER,


        total_price REAL,
        promo INTEGER,
        status TEXT DEFAULT 'new'
    );
    """

    connection.execute(query)
    connection.commit()
    connection.close()

# saving enquiries
def save_enquiry(sender_info, receiver_info, quote_info, promo):
    connection = get_connection()

    query = """
    INSERT INTO enquiries (
        sender_name, sender_email, sender_phone,
        receiver_name, receiver_email, receiver_phone, receiver_address,
        weight, value, medications, makeups, electronics, total_price, promo
    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """

    values = (
        sender_info["name"],
        sender_info["email"],
        sender_info["phone"],
       

        receiver_info["name"],
        receiver_info["email"],
        receiver_info["phone"],
        receiver_info["address"],

        quote_info["weight"],
        quote_info["value"],
        quote_info["medications"],
        quote_info["makeup"],
        quote_info["electronics"],
       
       quote_info["insurance_price"],

        quote_info["total_price"],
        promo

        
    )

    connection.execute(query, values)
    connection.commit()
    connection.close()

#Loading enquiries
def load_enquiries():
    connection = get_connection()
    connection.row_factory = sqlite3.Row

    query = """     
    SELECT *
    FROM enquiries
    ORDER BY id DESC
    """

    rows = connection.execute(query).fetchall()
    connection.close()

    return [dict(row) for row in rows]



@app.route("/update_status/<int:enquiry_id>", methods=["POST"])
def update_status(enquiry_id):
    if not session.get("admin_logged_in"):
        return redirect("/admin")

    new_status = request.form.get("status")

    connection = get_connection()

    query = """
    UPDATE enquiries
    SET status = ?
    WHERE id = ?
    """

    connection.execute(query, (new_status, enquiry_id))
    connection.commit()
    connection.close()

    return redirect("/admin/dashboard")





if __name__ == "__main__":
   create_enquiry_table()
   app.run(debug=True, port=5001)



