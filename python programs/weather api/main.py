from flask import Flask , render_template

app=Flask("Website")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/api/v1/<station>/<date/")
def route(station,date):
    
    return render_template(".html")


app.run(debug=True)