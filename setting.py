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
    