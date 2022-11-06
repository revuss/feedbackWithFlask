
import pymongo
from pymongo import MongoClient
from pymongo import collection
from flask import Flask,render_template,request,url_for

app = Flask(__name__)
cluster = MongoClient(

    'mongodb+srv://revus:revus@cluster0.n76oc9r.mongodb.net/?retryWrites=true&w=majority')
app.config["SECRET_KEY"]='6eac961eac9639593d965827cfd4c157ae5cfe5d'


db = cluster["Data"]

collection = db["response"]
baed = [0,0,0,0,0]
good = [0,0,0,0,0]
aver = [0,0,0,0,0]

class Question:
    title = ""
    name = ""
    good = "good"
    average = "average"
    bad= "bad"
    commnt=""

    def __init__(self,title,name,commnt,good="good",average="average",bad="bad"):
        self.title=title
        self.name = name
        self.good= good
        self.average = average
        self.bad=bad
        self.commnt = commnt
    
a = Question("1. C++","cpluss","cpluscommt")
b= Question("2. Java","java","javacommt")
c=Question("3. JavaScript","js","jscommt")
d= Question("4. SQL/PostgreSQL","sql","sqlcommt")
e= Question("5. Python","Py1","pycommt")
f = Question("6. Flask","Fls","flaskcommt")
good = [0,0,0,0,0,0]
average = [0,0,0,0,0,0]
bad = [0,0,0,0,0,0]
# java=[]
subjects = [a,b,c,d,e,f]
arr=[]
@app.route('/')
@app.route('/',methods=["GET","POST"])
def home():  
    if request.method=="POST":
        sle = 0 
        for subject in subjects:
            subject_name = subject.name
            option = request.form[subject_name]
            # if option == "good":
            #     arr.append(subject_name)
            # elif option=="average":
            #     arr.append(option)
            # elif option=="bad":
            #     arr.append(option)
            if subject_name == "cpluss":
                if option == "good":
                    good[0]+=1
                elif option=="average":
                    average[0]+=1
                elif option=="bad":
                    bad[0]+=1
            elif subject_name == "java":
                if option == "good":
                    good[1]+=1
                elif option=="average":
                    average[1]+=1
                elif option=="bad":
                    bad[1]+=1
            elif subject_name == "js":
                if option == "good":
                    good[2]+=1
                elif option=="average":
                    average[2]+=1
                elif option=="bad":
                    bad[2]+=1             
            elif subject_name == "sql":
                if option == "good":
                    good[3]+=1
                elif option=="average":
                    average[3]+=1
                elif option=="bad":
                    bad[3]+=1      
            elif subject_name == "Py1":
                if option == "good":
                    good[4]+=1
                elif option=="average":
                    average[4]+=1
                elif option=="bad":
                    bad[4]+=1   
            elif subject_name == "Fls":
                if option == "good":
                    good[5]+=1
                elif option=="average":
                    average[5]+=1
                elif option=="bad":
                    bad[5]+=1    
        for sub in subjects:
            if sub.commnt != "":
                print(sub.commnt)

        return good
    else:
        return render_template("index.html",subjects=subjects)

@app.route('/sd')
def submit():
    
    return render_template("sd.html")

if __name__ =="__main__":
    app.run(debug=True)