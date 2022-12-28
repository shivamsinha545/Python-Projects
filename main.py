# fname=input("Enter your first name: ")
# lname=input("Enter your last name: ")
# age=input("Enter your age: ")
# print(fname+lname)
# print(age)
# if(fname=="tony" or fname=="Tony"):
#     print("he is a genius")
# else:
#     print("he is meh")


#range
# numbers=range(5)
# print(numbers)

#loop
# i=5
# while(i>=0):
#     print(i * "*")
#     i-=1
#


#for loop
# for i in range(10):
#     print(i+1)

# list
# marks=[98,56,45,"pass"]
# marks.insert(0,99)
# # print(999 in marks)
# # print(len(marks))
# # for i in marks:
# #     print(i)
# i=0
#
# marks.clear()
#
# print(len(marks))

# list=["ram","shyam","seeta","geeta","radha","radhika"]
# for i in list:
#     if(i=="seeta"):
#         continue
#     else:
#         print(i)
# [] list
# () tuple or write nothing foreg. name="shivam","sinha","raj"
# {} set
# tuple - similar like list  we cannot modify the items in a tuple
# shiva={"shivam","sinha","is","great"}
# for i in shiva:
#     print(i)
# dictionary
# marks={"hindi":85,"english":856,"maths":89}
# marks["hindi"]=99
# print(marks)
def check(a):
    if(a%2==0):
        return True
    return False


def sum(a,b):
    print("sum is:",a+b)

# x=int(input("Enter: "))
# if(check(x)==True):
#     print("it is even")
# else:
#     print("its is odd")

i=int(input("a: " ))
j=int(input("b: "))
print(sum(i,j))
