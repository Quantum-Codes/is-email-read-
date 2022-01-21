from flask import Flask, render_template, request, send_file
import random

app = Flask("app")
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


@app.route("/", methods = ['GET'])
def form():
  if request.method == "GET":
    print(request.referrer, random.randint(0,1000))
    return send_file("clock.png"), 200

@app.route("/email")
def email():
  return render_template("index.html")


app.run(host='0.0.0.0', port=8080, debug=False)#replit's port