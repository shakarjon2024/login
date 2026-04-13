from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = request.form.get("user")
        parol = request.form.get("parol")

        if user == "admin" and parol == "1234":
            return render_template("welcome.html", user=user)
        else:
            return "Xato login"

    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)
