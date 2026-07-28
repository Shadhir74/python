#STRINGS

# str1="shadhir"
# str2='ram'
# str3='''yuvaraj'''
# print(str1)
# print(str2)
# print(str3)
# str4="ramu has many wive's"
# print(str4)


#escape sequence char

# str5="my name is shadhir.\niam a software engineer." #\n is for nxt line
# print(str5)

# str6="iam a graduate.\talso an unemployed."
# print(str6)


#basic operatins of str

# str1 = "hello"
# str2 = "world"
# print(str1+str2)                         #concatenation

# str3 = "mohammed shadhir pasha"
# len=len(str3)
# print(len)                                #length of str 
# print(str3)


#indexing

# str="mohammed shadhir"
# print(str[8])                                #position of Char in str

#slicing

# str="shadhir pasha"
# print(str[9:])                                  #removing of char by ratio
# print(str[3:6])                                 #negative slicing
# print(str[-2:])
# print(str[-9:])
# print(str[:12])


#string functions

# str="my dream is to become an software engineer"
# print(str.endswith("eer"))                      #endswith
# print(str.endswith("ir"))
# print(str.capitalize())                         #capitalizing first char
# print(str)
# print(str.replace("e","i"))                      #replacing
# print(str.replace("to","2"))
# print(str.find("e"))                              #finding
# print(str.find("soft"))
# print(str.count("e"))                             #no. of times it exists in str
# print(str.count("k"))

#practise questions
#WAP to input user first name and print its length

# str=input("enter user name :")
# print(len(str))

#WAP to find the occurence of '$' in a string

# str = "my name is mohammed shadhir.i need a lot of $ so i rob banks $"
# print(str.count("$"))

#Conditional statements

# age =int(input("enter age:"))
# if(age>=18):
#     print("eligible to vote")
#     print("can drive")
# else:
#     print("not eligible to vote and drive")

# light =input("enter colour :") 
# if (light =="yellow"):
#     print("wait")
# elif(light=="red"):
#     print("stop")
# elif(light=="green"):
#     print("go")
# else:
#     print("not valid")


#marks
# marks =int(input("enter your marks :"))
# if(marks>=90):
#     print("Grade A")
# elif(marks >=80 and marks <90):
#     print("grade B")
# elif(marks >=70 and marks<80):
#     print("grade c")
# elif(marks >= 35):
#     print("grade d")
# else:
#     print("fail")
     

#nesting

# age=int(input("enter age ="))
# if(age>=18):
#     if(age>80):
#         print("cannot drive" )
#     else:
#         print("can drive")
# else:
#     print("cannot drive")

#practise questions

# number=int(input("enter a number :"))      #evenodd
# if(number%2==0):
#     print("even")
# else:print("odd")

# number1=int(input("enter number1 :"))         #which is greater
# number2=int(input("enter number2 :"))
# number3=int(input("enter number3 :"))
# if number1>number2 and number1> number3 :
#     print("number1 is greater")
# elif number2 > number1 and number2 > number3:
#     print("number2 is greater")
# else:
#     print("number3 is greater")

number=int(input("enter a number :"))      #multiple of 7
if number%7==0 :
    print("multiple of 7")
else:
    print("not multiple of 7 ")