# print("NavGurukul")

# def say_hello():
#  print("Hello!")
#  print("Aap kaise ho?")

# say_hello()
# print("Python is awesome")
# say_hello()
# print("Hello…")
# say_hello()

# MERAKI QUESTION 1
# def ask_question():
#     print("ek baar")
# ask_question()

# MERAKI QUESTION 2
# numbers = [3, 5, 7, 34, 2, 89, 2, 5]
# def big():
#     c=max(numbers)
#     print("max no.=",c)
# big()

# QUESTION 2
# numbers = [1, 2, 3, 4, 5]
# def sum():
#     i=0
#     total_sum=0
#     while i<len(numbers):
#         total_sum=total_sum+numbers[i]
#         i+=1
#     print("sum=",total_sum)
# sum()

# QUESTION 3
# unorder_list = [6, 8, 4, 3, 9, 56, 0, 34, 7, 15]
# def accending():
#     unorder_list.sort()
#     print("SORTED LIST=",unorder_list)
# accending()

# QUESTION 4
# reverse_list = ["Z", "A", "A", "B", "E", "M", "A", "R", "D"]
# def rev():
#     reverse_list.reverse()
#     print("Reverse list=",reverse_list)
# rev()

# QUESTION 5
# list = [8, 6, 4, 8, 4, 50, 2, 7]
# def minimum():
#     small=min(list)
#     print("Minimum no.=",small)
# minimum()

# MERA KI QUESTION 2
# def function_print_line(name):
#     print("mera naam"+" "+name+" "+"hai")
# function_print_line("rishabh")
# print("mai navgurukul ka co-founder hu")

# MERAKI QUESTION 4
# def sum(a,b):
# 	res=[]
# 	i=0
# 	while i<len(a):
# 		res.append(a[i]+b[i])
# 		i=i+1
# 	print(res)
# a=[50, 60, 10] 
# b=[10, 20, 13]
# sum(a,b)

# MERAKI QUESTION 5
# def check_number(a,b):
#     if a%2==0 and b%2==0:
#         print("dono even hai")
#     else:
#         print("dono even nhi hai")
# a=int(input("enter no."))
# b=int(input("enter no."))
# check_number(a,b)

# #MERAKI QUESTION 5=part=2
# def check_number_list(a,b):
#     i=0
#     while i<len(a):
#         j=0
#         while j<len(b):
#             if a[i]%2==0 and b[j]%2==0:
#                 print("dono even hain")
#             else:
#                 print("dono even nahi hai")
#             j+=1
#         i+=1
# check_number_list([2, 6, 18, 10, 3, 75],[6, 19, 24, 12, 3, 87])

# # #MERAKI QUESTION6=PART=1
# def calculator(number_x,number_y,operation):
#     if operation=="add":
#         print(number_x+number_y)
#     elif operation=="subtract":
#         print(number_x-number_y)
#     elif operation=="multiply":
#         print(number_x*number_y)
#     elif operation=="divide":
#         print(number_x/number_y)
# number_x=int(input(" enter number: "))
# number_y=int(input(" enter number: "))
# operation=input(" enter operation: ")
# calculator(number_x,number_y,operation)

# #MERAKI QUESTION 7
# def vote(age):
#     if age>=18:
#         print("you are eligible")
#     else:
#         print("not eligible")
# age=int(input("enter your age:"))
# vote(age)

# #MERAKI QUESTION 8
# def num(first,second,third):
#     sum=first+second+third
#     avg=sum/3
#     print("sum of three numbers=",sum)
#     print("average of three numbers=",avg)
# first=int(input("enter first number"))
# second=int(input("enter second number"))
# third=int(input("enter third numner"))
# num(first,second,third)

# #MERAKI QUESTION 9
# def showNumber(limit):
#     i=0
#     while i<=limit:
#         if i%2==0:
#             print(i,"even")
#         else:
#             print(i,"odd")
#         i+=1
# limit=int(input("enter number:"))
# showNumber(limit)


# #MERAKI QUESTION 10
# def number(limit):
#     i=0
#     sum=0
#     while i<=limit:
#         if i%3==0 or i%5==0:
#             sum=sum+i
#         i+=1
#     print("sum",sum)
# limit=int(input("enter number:"))
# number(limit)

# MERAKI QUESTION 11
# def police(speed):
#     if speed<=70:
#         print("okey")
#     else:
#         print("licence suspended")
# speed=int(input("enter speed:"))
# police(speed)
# # # # # # # QUESTION 1
# # # # # def message():
# # # # #     print("hello python")
# # # # # message()

# # # # # # #QUESTION 2
# # # # # def add():
# # # # #     a=int(input("enter no.1"))
# # # # #     b=int(input("enter no.2"))
# # # # #     c=a+b
# # # # #     print("Addition=",c)
# # # # # # add()

# # # # # # #QUESTION 3
# # # # # def sub():
# # # # #     a=int(input("enter bigger no.then secound no."))
# # # # #     b=int(input("enterv smaller no. then pre no."))
# # # # #     c=a-b
# # # # #     print("subractiion=",c)
# # # # # sub()

#  # # # # #QUESTION 4
# # # # # #THIS QUESTION IS WITH ARGUMENTS
# # # # # def add(a,b):
# # # # #     c=a+b
# # # # #     print("Addition=",c)
# # # # # a=int(input("enter no."))
# # # # # b=int(input("enter second no."))
# # # # # add(a,b)

# # # # #SAME AS QUESTION 4
# # # # def add(a,b):
# # # #     c=a+b
# # # #     print("Addition=",c)
# # # # add(5,10)

# # # # #QUESTION 6 ODD EVEN WITHOUT ARGUMENT
# # # # def oddeve():
# # # #     a=int(input("enter no."))
# # # #     if a%2==0:
# # # #         print("even")
# # # #     else:
# # # #         print("odd")
# # # # oddeve()

# # # # #SAME QUESTION BUT WITH ARGUMENT
# # # # def oddeve(a):
# # # #     if a%2==0:
# # # #         print("even")
# # # #     else:
# # # #         print("odd")
# # # # a=int(input("enter no."))
# # # # oddeve(a)  

# # # def add(a,b):
# # #     c=a+b
# # #     return c
# # # x=int(input("enter no.1"))
# # # y=int(input("enter no.2"))
# # # z=add(x,y)
# # # print("addition=",z)

# # def add():
# #     a=int(input("enter no.1"))
# #     b=int(input("enter no.2"))
# #     c=a+b
# #     return c
# # sum=add()
# # print("Additon=",sum)

# # def add(a,b):
# #     c=a+b
# #     return(c)
# # a=int(input("enter no."))
# # b=int(input("enter no."))
# # z=add(a,b)
# # print("Addition=",z)

# #POSITIONAL ARGUMENT CODE
# # def add(a,b):
# #     c=a+b
# #     print("addition=",c)
# # add(5,6)

# # DEFAULT ARGUMENT CODE
# # def add(a,b=5):
# #     c=a+b
# #     print("Addition=",c)
# # add(10)

# # def interest(prin,rate,time):
# #     i=(prin+time*rate)/100
# #     print("Interest=",i)
# # # interest(5000,10,2)
# # interest(time=2,prin=5000,rate=10)

# def add(a,b):
#     c=a+b
#     return(c)
# a=int(input("enter no."))
# b=int(input("enter no."))
# z=add(a,b)
# print("Addition=",z)