from settings import load_settings


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
    weight = float(form.get("weight")or 0)
    value = float(form.get("value") or 0)
    medications = int(form.get("medications") or 0)
    electronics = int(form.get("electronics")or 0)
    makeup = int(form.get("makeups", 0)or 0)
    
     
    settings = load_settings()
   
    promo = settings["promo"]
    

    weight_price = calculate_weight_price(weight)
    insurance_price = calculate_insurance(value)
    medication_price = calculate_medication_price(medications)
    electronics_price = calculate_electronic_price(electronics)
    makeup_price = calculate_makeup_price(makeup)

    total_preprice = calculate_total_price(
        weight_price,
        insurance_price,
        medication_price,
        electronics_price,
        makeup_price
    )

    total_price = apply_promo_discount(total_preprice, promo)

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

