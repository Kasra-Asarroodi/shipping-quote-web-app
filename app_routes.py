
from flask import render_template, request, url_for, flash, session, redirect



from calculation import sender_info , receiver_info, quote_info

from database import get_connection, save_enquiry, load_enquiries, update_enquiry_status, increment_quote_calculations, get_quote_calculations

from settings import load_settings, save_setting

from app import app, ADMIN_PASSWORD





@app.route('/', methods=['GET', 'POST'])

def home():

    """
    Route to the homepage of the website where the calcuation of the quotes happen and where the user is able to submit an enquiry.
    """
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

             increment_quote_calculations()
             


        if action == "submit":
            save_enquiry(sender, receiver, quote, promo)
            flash("Your enquiry has been submitted!")



            
        
    return render_template('index.html', result=result, form_data = form_data)




@app.route("/about")
def about():
    """
    This function creates the route to the about us page.
    This page briefly introduces the company of freight and packaging.
    """

    return render_template("Aboutus.html")


@app.route("/contact")
def contact():

    """
    This function creates the route to the contact us page.
    In this page the user is able to find multiple ways of communcation with the company.
    
    """
    return render_template("contactus.html")




@app.route("/info")
def info():
    """
    This function creates the route to the information page.
    In this page the user is able to find out more about the pricing details of the quotes.
    """
    return render_template("info.html")


@app.route("/enquiries", methods=["GET", "POST"])
def enquiries():

    """
    Allows the user to enter an email which they have previously used to submit a quote.
    The entered email is then compared with the emails available in the database and is also stored in a session.
    This function is crucial in order to determine wether there is any previous quotes available with this email.
    
    """

    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()

        all_enquiries = load_enquiries()
        email_exists = False

        for enquiry in all_enquiries:
            stored_email = enquiry["sender_email"].strip().lower()

            if email == stored_email:
                email_exists = True  # Indicates there is a mathcing email from a previous quote with the email user has entered.
                break

        if not email_exists:
            flash("No matching enquiries with this email.")
            return redirect(url_for("enquiries"))

        
        session["customer_email"] = email # Remembers the email input in order to show the corresponding previous quotes in the dashboard page.
        
       
        return redirect(url_for("enquiries_dashboard"))

    return render_template("enquiries_login.html")



@app.route("/enquiries_dashboard")
def enquiries_dashboard():
    """
    This function displays the quotes that have been made with the same email user has entered.
    """

    if not session.get("customer_email"):
        return redirect(url_for("enquiries"))

    email = session.get("customer_email")
    all_enquiries = load_enquiries()

    

    matching_enquiries = [
    enquiry
    for enquiry in all_enquiries
    if enquiry["sender_email"].strip().lower() == email
    ]


    return render_template(
        "enquiries.html",
        enquiries=matching_enquiries
    )








@app.route("/enquiries/logout")
def enquiries_logout():

    """
    Once the user is done in the enquiries dashboard page,
    They can safely exit the dashboard page with the logout option which also terminates the running session.
    """

    session.pop("customer_email", None)

    flash("You have exited your enquiries.")

    return redirect(url_for("enquiries"))






@app.route("/admin", methods = ["GET", "POST"])
def admin_login():
    """
    This page collects the admin password and compares it with the actual password located as an environment variable.
    If the entered password matches the real password, the logged in session becomes valid and the admin is redireced to the dashboard.
    """

    if session.get("admin_logged_in"):
        return redirect(url_for("admin_dashboard"))


    if request.method == "POST":
       admin_password = request.form["password"]

       if admin_password == ADMIN_PASSWORD :
           session ["admin_logged_in"] = True
           return redirect(url_for("admin_dashboard"))
       
       flash("incorrect password")
           
    return render_template("admin_login.html")


@app.route("/admin/logout")
def admin_logout():

    """
    This route allows the admin to successfully log out of the admin page and also terminate the logged in session.
    """
    session.pop("admin_logged_in", None)
    flash("You have been logged out.")
    return redirect(url_for("admin_login"))



@app.route("/admin/dashboard", methods = ["GET"])
def admin_dashboard():
    """
    Once the admin has entered the correct password, they are able to view all of the enquiries amde throughout this route.
    """
    if not session.get("admin_logged_in"):
        return redirect(url_for("admin_login"))
    all_enquiries = load_enquiries()
    settings = load_settings()
    return render_template("admin.html", enquiries= all_enquiries, promo_rate = settings["promo"], quote_calculations = get_quote_calculations())


@app.route("/update_status/<int:enquiry_id> ", methods = ["POST"])
def update_status(enquiry_id):
    """
    This function allows the admin to dynamically update the status of an individual quote.
    """
    if not session.get("admin_logged_in"):
        return redirect(url_for("admin_login"))
    new_status = request.form.get("status")
    update_enquiry_status(enquiry_id, new_status)
  

    return redirect(url_for("admin_dashboard"))






    

    





@app.route("/update_promo", methods=["POST"])
def update_promo():
    """
    This function allows the admin to enter a promotion rate which influences the final total price.
    """
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
    """ 
    Deletes an enquiry from the database so it no longer
    appears in either the customer dashboard or the
    administrator dashboard. 
    """
    connection = get_connection()

    connection.execute(
        "DELETE FROM enquiries WHERE id = ?",
        (enquiry_id,)
    )

    connection.commit()
    connection.close()


@app.route("/delete_enquiry/<int:enquiry_id>", methods=["POST"])
def delete_enquiry_route(enquiry_id):
    """
    Redirects the user or admin to the correct page based on the page where an application has been deleted from.
    """
    delete_enquiry(enquiry_id)
    flash("Enquiry deleted successfully.")
    
    redirect_to = request.form.get("redirect_to")

    if redirect_to == "admin":
        return redirect(url_for("admin_dashboard"))
    
    return redirect(url_for("enquiries_dashboard"))
    
