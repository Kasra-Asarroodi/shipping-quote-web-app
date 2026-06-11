from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    result = ""

    if request.method == 'POST':
        
    


    return render_template('index.html', result=result)

app.run(debug=True)
def num_items(items):
   pass

def sender_info (sender_name, sender_phone, sender_email):
    sender = int(request.form['sender_name'])




def calculate_volume (volume, height, width, length):
        volume : float = height * width * length
        height = float(request.form['height'])
        width = float (request.form ['width'])
        length = float(request.form ['length'])
        return volume

       
        

 
def calculate_distance (city):
    distance_cost: int 
    city = str(request.form['city']).upper()
    while len(city) != 3 :
        if city == "Adelaide":
            distance_cost = 20
        elif city == "Shiraz":
            distance_cost = 30
        elif city == "Mashhad":
            distance_cost = 40
        elif city == "Tabriz":
            distance_cost = 50
        else:
         print(f"Unfortunetly, we currently dont offer services for city of {city}")
    else:
     print(f" Please select a valid city located in IRAN!")
    return distance_cost
    


       
def calculate_chargableweight(weight, weight_price):
    try:
        weight = float(request.form['weigth'])
        weight_price : int
        if weight < 25:
         print("The minimum weight of a parcel must be atleast 25KG!")
        else : weight_price = weight * 2
    except ValueError :
        print("Please enter a number instead of a digit")
    
    
    return weight_price
     
       
   
   
def calculate_service(service_price, distance_cost, weight_price):
   service_price :int = weight_price + distance_cost / 2
   return service_price
   


def calculate_pretotalcost(pretotal_price, service_price, weight_price, distance_price) :
   pretotal_price :float = weight_price + service_price + distance_price
   return (pretotal_price)

def calculate_insurance(pretotal_cost, insurance):
    insurance :float = pretotal_cost / 2
    return insurance

def calculate(total_cost, pretotal_price, insurance):
    total_cost: float = pretotal_price + insurance
    return total_cost

def save_enqury (receiver_info, sender_info, estquote):
   pass
 