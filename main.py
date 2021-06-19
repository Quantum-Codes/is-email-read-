from flask import Flask, render_template, request

app = Flask("app")

@app.route("/")
def form():
  return render_template("form.html" methods=['GET','POST'])


app.run(host='0.0.0.0', port=8080)