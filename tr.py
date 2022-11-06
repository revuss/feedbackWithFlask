from flask import Flask,request,url_for,render_template
class Question:
    title = ""
    name = ""
    good = "good"
    average = "average"
    bad= "bad"

    def __init__(self,title,name,good="good",average="average",bad="bad"):
        self.title=title
        self.name = name
        self.good= good
        self.average = average
        self.bad=bad
    
    
a = Question("1. C++","cpluss")
b= Question("2. Java","java")
c=Question("3. JavaScript","js")
d= Question("4. SQL/PostgreSQL","sql")
e= Question("5. Python","Py1")
f = Question("6. Flask","Fls")

subjects = [a,b,c,d,e,f]

for su in subjects:
  id = su.name
  print (id)

app = Flask(__name__)


@app.route('/')
def home():
  return render_template("so.html")
@app.route('/su',methods=["POST","GET"])
def submit():
  a = request.args['cpluss']
  return a

  return "hello"
if __name__=="__main__":
  app.run(debug=True)
