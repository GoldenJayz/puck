from flask import *

app = Flask(__name__)


@app.route("/api")
def home():
    return render_template("./puk.json")

if __name__ == "__main__":
    app.run()
