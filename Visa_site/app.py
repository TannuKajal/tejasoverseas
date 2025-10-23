from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

# Service detail pages
@app.route("/services/admission_guidance")
def admission_guidance():
    return render_template("admission_guidance.html")

@app.route("/services/uae-tourist-visa")
def uae_tourist_visa():
    return render_template("uae_visa.html")

@app.route("/services/document-preparation")
def document_preparation():
    return render_template("document_preparation.html")

@app.route("/services/visa_application_assistance")
def visa_application_assistance():
    return render_template("visa_application_assistance.html")

@app.route("/services/passport-services")
def passport_services():
    return render_template("passport.html")

@app.route("/services/nulla-osta")
def nulla_osta():
    return render_template("nulla_osta.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=False)
