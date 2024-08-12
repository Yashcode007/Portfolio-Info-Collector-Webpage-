from flask import Flask, render_template , request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/design")
def design():
    return render_template("design.html")

@app.route("/form")
def form():
    return render_template("form.html")

@app.route("/upload", methods=["GET","POST"])
def upload():
    if request.method == "POST":
        name=request.form.get("firstname")
        lastname=request.form.get("lastname")
        school=request.form.get("school")
        college=request.form.get("college")
        phone=request.form.get("phone")
        email=request.form.get("email")
        about=request.form.get("about")
        skill1=request.form.get("skill1")
        skill2=request.form.get("skill2")
        skill3=request.form.get("skill3")
        skill4=request.form.get("skill4")

    return "Uploaded"
app.run(debug=True)

