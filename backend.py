from flask import Flask, render_template, request, jsonify, redirect, url_for
import microservices
from microservices import email_service
from dotenv import load_dotenv
import os

app = Flask(__name__,template_folder='pages')

# Static files handled automatically by Flask
# Flask looks for static files in a directory called 'static'
# and templates in a directory called 'templates' by default

# Env Variables
load_dotenv('Variables.env')

apiData = {
    "notifier_mail":os.getenv('NOTIF_EMAIL'),
    "notifier_pass":os.getenv('GOOGLE_ENV_PASS')
}

# Homepage route
@app.route("/", methods=["GET"])
def read_root():
    return render_template("index.html")

# About route
@app.route("/about", methods=["GET"])
def read_about():
    return render_template("about.html")

# Services route
@app.route("/services", methods=["GET"])
def read_services():
    return render_template("services.html")

@app.route("/contact", methods=["GET"])
def read_contact():
    return render_template("contact.html")

# Contact form route
@app.route("/send-email", methods=["POST"])
def submit_contact():
    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")
    service_type = request.form.get("service_type")

    if name and service_type and email and message:
        data = {
            "NAME": name,
            "CONTACT": email,
            "MESSAGE": message,
            "ENQUIRY": service_type
        }
        try:
            # Call the email service to send the email
            email_service.SendDetailsToMainMail(data,apiData)

            # Call email service to send a receipt to the client
            receipt_Data = {
                "CLIENT_NAME": name,
                "CLIENT_EMAIL": email,
                "ENQUIRY": service_type
            }

            email_service.SendReceiptToClient(receipt_Data,apiData)
            return render_template("thankyou.html")
        except Exception as e:
            print(f"Error logging: mail couldn't be sent for this individual: {email}")
            print(f"Exception in question:\n{e}")
            return jsonify({"success": False, "error": "Failed to send email"}), 500
    else:
        return redirect(url_for('read_contact'))
    
if __name__ == "__main__":
    app.run(debug=True)