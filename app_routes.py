
from flask import render_template, request, url_for, flash, session, redirect



from calculation import sender_info , receiver_info, quote_info

from database import get_connection, save_enquiry, load_enquiries

from settings import load_settings, save_setting

from app import app, ADMIN_PASSWORD





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




@app.route("/about")
def about():
    return render_template("Aboutus.html")


@app.route("/contact")
def contact():
    return render_template("contactus.html")




@app.route("/info")
def info():
    return render_template("info.html")


@app.route("/enquiries", methods=["GET", "POST"])
def enquiries():

    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()

        all_enquiries = load_enquiries()
        email_exists = False

        for enquiry in all_enquiries:
            stored_email = enquiry["sender_email"].strip().lower()

            if email == stored_email:
                email_exists = True
                break

        if not email_exists:
            flash("There are no matching enquiries with this email.")
            return redirect(url_for("enquiries"))

        session["costumer_email"] = email
        return redirect(url_for("enquiries_dashboard"))

    return render_template("enquiries_login.html")



@app.route("/enquiries_dashboard")
def enquiries_dashboard():

    if not session.get("costumer_email"):
        return redirect(url_for("enquiries"))

    email = session.get("costumer_email")
    all_enquiries = load_enquiries()
    matching_enquiries = []

    for enquiry in all_enquiries:
        stored_email = enquiry["sender_email"].strip().lower()

        if stored_email == email:
            matching_enquiries.append(enquiry)

    return render_template(
        "enquiries.html",
        enquiries=matching_enquiries
    )








@app.route("/enquiries/logout")
def enquiries_logout():

    session.pop("costumer_email", None)

    flash("You have exited your enquiries.")

    return redirect(url_for("enquiries"))






@app.route("/admin", methods = ["GET", "POST"])
def admin_login():


    if session.get("admin_logged_in"):
        return redirect(url_for("admin_dashbaord"))


    if request.method == "POST":
       admin_password = request.form["password"]

       if admin_password == ADMIN_PASSWORD :
           session ["admin_logged_in"] = True
           return redirect(url_for("admin_dashboard"))
       
       flash("incorrect password")
           
    return render_template("admin_login.html")


@app.route("/admin/logout")
def admin_logout():
    session.pop("admin_logged_in", None)
    flash("You have been logged out.")
    return redirect(url_for("admin_login"))



@app.route("/admin/dashboard", methods = ["GET"])
def admin_dashboard():
    if not session.get("admin_logged_in"):
        return redirect(url_for("admin_login"))
    all_enquiries = load_enquiries()
    settings = load_settings()

    return render_template("admin.html", enquiries= all_enquiries, promo_rate = settings["promo"])









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
    


def delete_enquiry(enquiry_id):
    connection = get_connection()

    connection.execute(
        "DELETE FROM enquiries WHERE id = ?",
        (enquiry_id,)
    )

    connection.commit()
    connection.close()


@app.route("/delete_enquiry/<int:enquiry_id>", methods=["POST"])
def delete_enquiry_route(enquiry_id):
    delete_enquiry(enquiry_id)
    flash("Enquiry deleted successfully.")
    
    redirect_to = request.form.get("redirect_to")

    if redirect_to == "admin":
        return redirect(url_for("admin_dashboard"))
    
    return redirect(url_for("enquiries_dashboard"))
    
