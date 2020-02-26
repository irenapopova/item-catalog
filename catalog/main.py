from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
  '''Main page of the forum.'''
  # TODO Fetch it from db
  categories = ["History", "Geography", "Fiction", "Prose"] 
  return render_template("index.html", categories=categories)

app.config["TESTING"] = True
app.config["FLASK_ENV"] = "development"
app.config["TEMPLATES_AUTO_RELOAD"] = True 
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0
app.run(host='0.0.0.0', port=8000, debug=True)
