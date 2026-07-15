from settings import load_settings


def sender_info (form):
   """Collects the information of the sender"""

   return {"name": form.get("sender_name", ""),
           "phone":form.get("sender_phone", ""),  
           "email": form.get("sender_email","")}

  

def receiver_info(form):
    """Collects the information of the receiver"""

    return {"name": form.get("receiver_name", ""), 
            "phone":form.get("receiver_phone", ""), 
            "email": form.get("receiver_email", ""), 
            "address":form.get("receiver_address", "")}





def quote_info(form):
    """
    Collects and organises all of the information of one quote which simplifies the stage where all the information from one quote are saved.
    """
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
    """ Calcutes the price the customer has to pay for the parcel based on the the weight of packages.
        This goal is achieved by having a tuple list which goes through each weight a parcel could have with its cost.
    """


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
    """ This function calcultes the insurance fee on the parcel which is %20 based on the freight and packaging company policies """
    
    return value / 5

    
   


def calculate_medication_price(medication):
 """ 
    Based on the company policies, each bottle or package of medication has a cost of 6 dollars.
    This function allows the program to also consider the cost of medications if there was any. 
 """
 return medication * 5



def calculate_electronic_price(electronic):
 """ 
    Based on the company policies, each electronic device has a extra cost of 60 dollars.
    This function allows the program to also consider the cost of electronics if there was any. 
 """
 return electronic * 50 




def calculate_makeup_price(makeup):
    """ 
    Based on the company policies, each makeup product has a cost of 6 dollars.
    This function allows the program to also consider the cost makeups if there was any. 
    """
    return makeup * 3

def calculate_total_price(weight_price, insurance_price, medication_price, electronics_price, makeup_price):
    """ 
    This function calculates the total price for a quote that the user sees by considering all of the expenses based on the user's parcel details.
    """

    return weight_price + insurance_price + medication_price + electronics_price + makeup_price

def apply_promo_discount(total_price, promo):
    """ 
    This function considers a promo rate if the admin wanted to add a percentage of discount to the future quotes.
    """
    return total_price * ( 100 - promo) / 100

