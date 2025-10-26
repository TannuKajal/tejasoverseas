from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

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

# Seasonal Nulla Osta
@app.route('/seasonal-nulla-osta')
def seasonal_nulla_osta():
    return render_template('seasonal_nulla_osta.html')

# Domestic Nulla Osta
@app.route('/domestic-nulla-osta')
def domestic_nulla_osta():
    return render_template('domestic_nulla_osta.html')

# Family Reunion Nulla Osta
@app.route('/family-nulla-osta')
def family_nulla_osta():
    return render_template('family_nulla_osta.html')

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
