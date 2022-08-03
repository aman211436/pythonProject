# INHERETANCE
class person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    def printname(self):
        print(self.firstname,self.lastname)
# use the person class to create an object,then execute the program
x=person("CSE","PFSD")
x.printname()


# SUPER KEYWORD
class parent:
    def __init__(self,txt):
        self.message=txt
    def printmessage(self):
        print(self.message)
class child(parent):
    def __init__(self,txt):
        super().__init__(txt)
x=child("HELLO,AND WELCOME!")
x.printmessage()


# RANDOM FUNTION IN PYTHON
import random
n=random.randbytes(3)
print(n)
print(random.randrange(1,8))
print(random.randint(100,211))
mylist=["jadeja","ashwin","dhoni","kholi"]
mylist1=["jadeja","ashwin","dhoni","kholi"]
print(random.choice(mylist))
print(random.choice(mylist1))
random.shuffle(mylist)
print(mylist)


# RE
import re
txt="use of python in machine learning"
x=re.search("^use.*learning$",txdt)
if(x):
    print("yes!we have a match")
else:
    print("no match")
x=re.findall("in",txt)
print(x)
txt="pythone is one of the most popular language"
searchobj=re.search("\s",txt)
print("the first white-space character is located")

# EXCEPTIONS
