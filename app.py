from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session, redirect

import os 
import json

app = Flask(__name__)

app.secret_key = "temporary_secret_key"

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
            "Address":form.get("receiver_address", "")}





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



   
ENQUIRY_FILE = "enquiries.json"

SETTING_FILE = "setting.json"

def save_enquiry(sender_info, receiver_info, quote_info, promo):
    enquiries= load_enquiries()
    enquiry = {
        "sender": sender_info,
        "receiver": receiver_info,
        "quote_information": quote_info,
        "status" : "new",
        "id" : len(enquiries) +1,
        "promo" : promo
    }

    
    enquiries.append(enquiry)

    with open(ENQUIRY_FILE, "w") as file:
        json.dump(enquiries, file, indent=4)





def load_enquiries():
    if os.path.exists(ENQUIRY_FILE):
        with open(ENQUIRY_FILE, "r") as file:
            return json.load(file)
    return []



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
            sender_email = enquiry["sender"]["email"]
            if sender_email == entered_email:
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



@app.route("/update_status/<int:enquiry_id>", methods=["POST"])
def update_status(enquiry_id):

    if not session.get ("admin_logged_in"):
        return redirect("/admin")
    
    new_status = request.form.get("status")

    enquiries = load_enquiries()

    for enquiry in enquiries:
        if enquiry["id"] == enquiry_id:
            enquiry["status"] = new_status
            break

    with open(ENQUIRY_FILE, "w") as file:
        json.dump(enquiries, file, indent=4)

    return redirect("/admin/dashboard")
    





if __name__ == "__main__":
   app.run(debug=True, port=5001)



