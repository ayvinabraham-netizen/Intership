"""mylist=[1,2,3,4,5] 
print(mylist)
mylist.append(7)
print(mylist)
mylist.remove(2)
print(mylist)
mylist.pop()
print(mylist)
print(len(mylist))
for num in mylist:
    if num%2==0:
        newlist = [num]
        print(newlist) 
# tuple...............................
mytuple = (1,2,3,4,5,6,7,8,9,10)
listfor =list(mytuple)
listfor[2]=99
anewtuple = tuple(listfor)
print(anewtuple)  
"""


# function................................
"""
def square(a):
    square = a * a
    print(square)

a = int(input("enter the number"))
square(a)

def student(name,age,course):
    print("the name of the student is",name)
    print("the age of the student is",age)
    print("the course opted is",course)

student(name="ayvin",age=19,course="bca")
"""

# dictionary ...................
thedict = {
    "name":"Ayvin",
    "age":"19",
    "course":"BCA"
}
print(thedict)
thedict["name"] = "kiran"
thedict.update({"name":"ashwin"})
print(thedict)



