import pymongo
from pymongo import MongoClient
from pymongo import collection
import pandas as pd


cluster = MongoClient(

    'mongodb+srv://revus:revus@cluster0.n76oc9r.mongodb.net/?retryWrites=true&w=majority')

db = cluster["Data"]

collection = db["response"]

import numpy as np
import matplotlib.pyplot as plt
 

# a= collection.find()
# b = []
# for i in a:
#     # print(i)
#     b.append(i)
# print(b)
# print(a.values())
# print(list(b.index('Java')))
# b[1]
# b = pd.DataFrame(a)
# pr
java_good = 12
sql_good = 11
php_good = 10
java_average = 2
sql_average = 1
php_average = 1
java_bad = 2
sql_bad = 1
php_bad = 0

width = 0.25
a = [1,2,3,1,2,3,1,2,3]
java_good = a[0]
java_bad=a[2]
print(java_bad)
java_bad+=1
print(java_bad)
# course = ["java","sql","php"]
# good = [java_good,sql_good,php_good]
# bad = [java_bad,sql_bad,php_bad]
# average = [java_average,sql_average,php_average]
# # br = np.arrange(len(java))
# fig = plt.figure(figsize = (10, 5))

 
# # creating the bar plot
# plt.bar(2,java,  color ='maroon',
#         width = 0.4)
        

# plt.xlabel("Courses offered")
# plt.ylabel("No. of students enrolled")
# plt.title("Students enrolled in different courses")
# plt.show()
cplu = [0,0,0]
jav = [0,0,0]
jes = [0,0,0]
sq = [0,0,0]
py = [0,0,0]
fls= [0,0,0]
print(cplu)
cplu[2]+=1
print(cplu)