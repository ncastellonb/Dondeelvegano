from flask import Flask, render_template, request
from flask_mail import Mail, Message


app = Flask(__name__)

app.config['MAIL_SERVER'] = 'certiweb.hostchile.cl'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'ventas@electrode.cl'
app.config['MAIL_PASSWORD'] = 'Poillpoll123'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/contact")
def contact():
    return render_template("contact-us.html")


