from flask import Flask, render_template

app = Flask(__name__, static_folder="static", template_folder="templates")

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    # Important for Spyder: disable reloader to avoid SystemExit
    app.run(host="127.0.0.1", port=5000, debug=True, use_reloader=False, threaded=True)
