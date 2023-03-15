from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
  {
  'ID':1,
  'Title': 'Data analyst',
  'Location' : 'Bengaluru India',
  "Salary":"₹1,000,000"
   },
  {
  'ID':2,
  'Title': 'Data Scientist',
  'Location' : 'Delhi India',
  "Salary":"₹1,000,000"
},
{
  'ID':3,
  'Title': 'Front End Engeineer',
  'Location' : 'Remote',
  "Salary":"₹1,000,000"
},
{
  'ID':4,
  'Title': 'Back End Engeineer',
  'Location' : 'San Francisco , USA',
  "Salary":"$120,000"
}

]


@app.route("/")
def hello_world():
  return render_template("home.html",jobs=JOBS , Company_name="Max")


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
