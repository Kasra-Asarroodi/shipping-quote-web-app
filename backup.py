
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
