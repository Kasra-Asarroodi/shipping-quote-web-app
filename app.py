from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None

    if request.method == 'POST':
        sender = sender_info(request.form)
        receiver = receiver_info(request.form)
        quote = quote_info(request.form)

        save_enquiry(sender, receiver, quote)

        result = quote["total_price"]
    
    return render_template('index.html', result=result)




def sender_info (form):
   return {"name": form["sender_name", ""], "phone":form["sender_phone", ""],  "email": form ["sender_email",""]}

  

def receiver_info(form):
    return {"name": form["receiver_name", ""], "phone":form["receiver_phone", ""],  "email": form ["receiver_email", ""], "Address":["receiver_address", ""]}





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
   
   


if __name__ == "__main__":
    app.run(debug=True)



