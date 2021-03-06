from flask import Flask,  escape, request, render_template
app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/about.html")
def about():
    return render_template('about.html')

@app.route("/tushar_new.html")
def tushar_new():
    return render_template('tushar_new.html')

@app.route("/nagarajan.html")
def nagarajan():
    return render_template('nagarajan.html')

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=4081)
