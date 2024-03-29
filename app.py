from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)
# Load configuration from the environment: https://flask.palletsprojects.com/en/2.3.x/config/#configuring-from-environment-variables
# Use the ADDRESSY_ prefix
app.config.from_prefixed_env("ADDRESSY")


@app.route("/")
def index():
    return render_template(
        "index.html",
        user=app.config["LOQATE_USER"],
        password=app.config["LOQATE_PASSWORD"],
    )


@app.route("/home", methods=["GET", "POST"])
def home():
    return render_template(
        "index.html",
        user=app.config["LOQATE_USER"],
        password=app.config["LOQATE_PASSWORD"],
    )


@app.route("/process", methods=["GET", "POST"])
def process():
    if request.method == "POST":
        fullAddress = str(request.json["fullAddress"])
        postcode = str(request.json["postcode"])

        # Use relative path to the database file
        db_dir = "nswgovschools.db"
        conn = sqlite3.connect(db_dir)

        details_cur = conn.execute(
            "select School_name, Town_suburb, Postcode from NSW_govt_schools_master_dataset where Postcode = ? COLLATE NOCASE",
            [postcode],
        )

        details = details_cur.fetchall()
        conn.close()

        # conn = sqlite3.connect(db_dir)
        # details_cur = conn.execute(
        #      'select Name, Address, Suburb, Postcode, Phone, ED from NSW_Health_Services = ? where Postcode = ? COLLATE NOCASE', [postcode])

        # health_details = details_cur.fetchall()
        # conn.close()

    return render_template("result.html", fullAddress=fullAddress, details=details)


# 404 error handler
@app.errorhandler(404)
def page_not_found(e):
    return render_template("errors/404.html"), 404


# 500 error handler
@app.errorhandler(500)
def internal_server_error(e):
    return render_template("errors/500.html"), 500


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
