from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    result = ""

    if request.method == 'POST':
        sender = sender_info(request.form)
        receiver = receiver_info(request.form)
        quote = quote_info(request.form)

        save_enquiry(sender_info, receiver_info, quote_info)

        result = quote_info["total_price"]
    
    return render_template('index.html', result=result)




def sender_info (form):
   return {"name": form["sender_name"], "phone":form["sender_phone"],  "email": form ["sender_email"]}

  

def receiver_info(form):
    return {"name": form["receiver_name"], "phone":form["receiver_phone"],  "email": form ["receiver_email"], "Address":["receiver_address"]}





def quote_info(form):
    weight = float(form["weight"])
    value = float(form["value"])
    medications = int(form["medications"])
    electronics = int(form["electronics"])
    makeup = int(form["makeup"])

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

    return {
        "weight": weight,
        "value": value,
        "medications": medications,
        "electronics": electronics,
        "makeup": makeup,
        "weight_price": weight_price,
        "insurance_price": insurance_price,
        "total_price": total_price
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
    return None


   
def calculate_insurance(insurance, weight):
    
   insurance = weight / 5
   return insurance


def calculate_medication_price(medication):
 return medication * 6

def calculate_electronic_price(electronic):
   return electronic * 60

def calculate_makeup_price(makeup):
   return makeup * 6

def calculate_total_price(weight_price, insurance_price, medication_price, electronics_price, makeup_price):
    return weight_price + insurance_price + medication_price + electronics_price + makeup_price
   
   

def save_enquiry (sender_info, receiver_info, quote_info):
   import os
   import json
   enquiry = {"sender": sender_info, "receiver":receiver_info, "quote information": quote_info }
   
   file_path = "enquiries.json"
   if os.path.exists(file_path):
      with open (file_path, "r") as file:
         enquiries = json.load(file)
   else:
      enquiries = []
   enquiries.append(enquiry)

with open(file_path, "w") as file:
   json.dump(enquiries, file, "r")

 
app.run(debug=True)


