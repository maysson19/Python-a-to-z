# this is basic:-
# x = 5 
# y = 'hello'
# print(x,y)
# print('Welcome, in the world')
# print(True,False)
# print(11111)
# print('hello'),print('welcome')
# y = 2+2
# print(y)
# //////////////////////////////////////////////////////////////////////////////////////
# //////////////////////////// We will start now:- /////////////////////////////////////
# name = 'Mayson'
# print('hello'+name+'welcomeee')
# ///////////////
# name1 = 'Ahmed '
# name2 = 'Mohamed'
# print(name1+name2)
# ///
# name1 = 'Ahmed '
# name2 = 'Mohamed'
# names = name1+name2
# print(names) 
# ///////////////////////////////////////////////////////////////////////////////////
#/////////////////// 'String' ///////////////////
# 1 :- "",'' (علامات التنصيص ليها شكلين)
# x = "hello"
# y = 'welcome'
# print(x),print(y)
# 2 :- \ (باقي الي في سطر الي تحت تبع الي فوق )
# x = "hell\
# oooooooo"
# y = 'welcome'
# print(x),print(y)
# 3 :- \n (بتخلي كل حاجه في سطر)
# x = "hello\n ahmed"
# y = 'welcome'
# print(x),print(y)
# 4 :- "\"\"" (عايز اعمل علامه علي الاسم)
# x = "hello \"ahmed\""
# y = 'welcome'
# print(x),print(y)
# 5 :- [] (لو عايز اطبع حرف معين) : (هيطبع من حرف لحرف)
# x = 'ahmed'
# print(x[0:3])
# 6 :- functions help me in string
# y = "ahmed"
# print(y.upper()) #بتحول الحروف لكبيره
# x = "AHMED"
# print(x.lower()) #بتحول الحروف لصغيره
# r = "AHMED"
# print(r.islower()) #بتجاوبك عل الحروف صغيره بصح ولا غلط
# t = "AHMED"
# print(t.isupper()) #بتجاوبك عل الحروف كبيره بصح ولا غلط
# u = "ahmed"
# print(u.capitalize()) #بتخلي اول حرف كبير
# g = "ahmed mohamed"
# print(g.title()) #بتخلي اول حرف في كل كلمه كبير
# 7 :- split (بتحول من نص ل ليست)
# x = "html css python c++ java flutter"
# print(x.split())
# r = "html_css_python_c++-java-flutter"  # بيطبعها زي ماكتبها بس جوا ليست
# print(r.split())
# t = "html css python c++ java flutter"
# print(t.split("h"))  # حددتله اني لو لقي الحرف ده يشيله ويحط فاصله مكانه
# y = "html_css_python_c++_java_flutter"
# print(y.split("_",4))  # من اليمين بعد الكلمه الرابعه مش هيعمل فاصله
# o = "html_css_python_c++_java_flutter"
# print(o.rsplit("_",4))  # هيعكس من الشمال بعد الكلمه الرابعه مش هيعمل فاصله
# 8 :- index (بدخله الحرف بيطلعلي الرقم بتاعه)
# l = "html css js php python"
# print(l.index('m')),print(l.index('php'))
# 9 :- len (بيحسبلي الحروف الي موجوده كام حرف)
# x = "html css js php python"
# print(len(x))
# print(len("html css"))  #بيحسبلي عدد الكلمات الي دخلتها
# 10 :- replace (بيبدل حاجه مكان حاجه)
# x = "html css js php python"
# print(x.replace('php','c++'))
#/////////////////////////////////////////////////////////////////////////////////
# ///////////////////////// Numbers //////////////////////
# 1 :- basic mathmatic
# print(4*4)
# print(7%5) #الباقي من القسمه
# print(9-9)
# print(4+6)
# 2 :- type the data number
# print(type(2)) #int
# print(type(6.9)) #float
# print(type(7+6j)) #complex
# 3 :- str (لاجراء عمليه حسابيه مع نص)
# print(str(6*1)+" age")
# 4 :- float (عايز احول رقم صحيح لرقم عشري)
# print(float(10))
# print(int(10.7))  #عايز احول الرقم لصحيح
# print(complex(10))  #عايز احول الرقم كومبيلكس
# 5 :- round (   لو الرقم الي بعد العلامه صغير بيرجع الرقم لورقم عشري الي بعد العلامه لو من 5 ل9 بيقرب الرقم)
# print(round(7.7)) ,print(round(7.4)) 
# 6 :- from math import* (بيعمل استعاء لمكتبه الماث كلها)
# 7 :- floor (لما بدخله رقم عشري بيطبع الرقم الاقل)
# print(floor(7.9))
# 8 :- floor (لما بدخله رقم عشري بيطبع الرقم الاكبر)
# print(ceil(7.9))
# 9 :- pow (بتاخد قيمتين بتعمل اوس)
# print(pow(7,9))
# 10 :- abs (لو اديتها قيمه سالب بتخليها موجب)
# print(abs(-6))
# 11 :- max ( بتطلعلي الرقم الكبير)
# print(max(3,6))
# 12 :- min ( بتطلعلي الرقم الصغير)
# print(min(3,6))
#/////////////////////////////////////////////////////////////////////////////////////////
#/////////////////////////////// Input data with users ////////////////////////////////////
#input("Enter your name :") #(نص"يشوفه اليوزر عشان يكتب الدات "ا)
#age = input("Enter your age :")
#print("your age is : "+age)
#/////////////////////////////// Simple Calculate ////////////////////////////////////
#"اليوزر يدخل الارقام والاله تحسب "
# num1 = input("Enter the first number :")
# num2 = input("Enter the second number :")
# result = int(num1) + int(num2)
# print(result)
#//////////////////////////////// Input With String /////////////////////////////////
#اليوزر يدخل اللغه الي عايزها وانا اكتبله معاها جمله
# x = input("I love Lan1 : ")
# y = input("I love Lan2 : ")
# print("I love "+x)
# print("I love "+y)
#//////////////////////////////////////////// DataType(4) ///////////////////////////////////////////////////////
#////////////////////////////////////(1) List [] ///////////////////////////////////////////
#بقدر اخزن جواها عدد كبير من البيانات
# listaa = ["Ahmed", 30, 4.8, True, 4j ,False, [2,4,6]]
# print(listaa[3],[4],[7]) #بحددله انا عايزه ابع ايه من الليست
# listaa [0] = "Mohamed" # بعدل علي حاجه جوا الليست
# print(listaa) #بطبع الي جوا الليست كلها
#///////////////////////////// List Methods /////////////////////////////////
# x = [1,2,3]
# y = [6,7,8]
# x.append(4) # بضيف عنصر داخل الليست
# x.insert(2,2.5) #بضيف عنصر في المكان الي عايزه بكتب الحاجه الي عايزها قبله وبكتب العنصر الجديد
# x.extend(y) # لو عايز الاتنين ليست سبعوا مع بعض
# print(x)
#/////////////////////
# w = [4,7,8,2,9,1,6,3,5,10]
# w.sort()# ببقي عايز اطبع الارقام بالترتيب
# w.remove(9) #بخليه يمسح الداتا الي قولت عليها 
# w.clear() # بتمسح كل الداتا
# print(w)
# v = ["Mayson","Ahmed","Ziad"]
# v.sort() #هيطبع الاسامي ببدايه الحرف بالترتيب
# print(v)
# e = [4,7,8,2,9,1,6,3,5,10]
# e.sort(reverse=True) #دي قيمه بتتكتب لو عايزه يطبع العكس من كبير لصغير 
# print(e)
#//////////////////////////////////// (2) Tuples //////////////////////////////////////
#زيها زي الليست بس دي مبقدرش اعدل عليها
# tuples =(1,4j,5.7,'helooooo')
# print(tuples)
#//////////////////////////////////(3) Dictionary ////////////////////////////////////
# بكتب فاريبال واجيب عنه معلومات
# info = {
#     "name": "ahmed",
#     "age": 25,
#     "country":"egypt"
# }
# print(info)
# print(info["age"]) # عشان اطبع الي بعد الكي
# print(info.get("id")) #لو لبت حاجه ومش موجوه بيقولي نان
#/////////////////////////////////////(4) Set /////////////////////////////////////////
#بتطبع مش بالتريب
#مش بتجيب انديكس من جوا
#مقدرش اكتب جواها ليست او ديكشنري
# mySet = {"Ahmed","Mostafa",(2,4,5),"Mohamed"}
# print(mySet)
#//////////////////////////////////// Set Methods //////////////////////////////////////
# a = {1,2,3}
# b = {4,5,6}
# print(a.union(b)) #هعمل دمج الاتنين مع بعض
# print(a|b) #هعمل دمج الاتنين مع بعض
# s = {1,2,3}
# s.add(4) #عايز اضيف جواعنصر السيت
# print(s) 
# r = {12,33,4}
# r.remove(33) #لو عايز امسح عنصر
# print(r)
# d = {12,33,4}
# d.discard(4) #لو عايز امسح عنصر ومش موجود مش هياثر
# print(d)
# c = {12,33,4}
# c.clear() #لو عايز امسح كل الي في سيت
# print(c)
#////////////////////////////////// def Function ///////////////////////////
# pow(3,3) #بتعمل اوص 
# def firstfunction(name,age):  #(بحط جوا القوسين مفتاح كي)
#     print("My name is " +name +" and Your age is "+str(age))  # لازم استخدم المفتاح هنا عشان يطبع
# firstfunction("ahmed",25)    # (بحط جوا القوسين القيمه بتاعت المفتاح الي فوق )
#/////////////////////////////////////// def Function Return ////////////////////////////////////
# def calc(num1,num2):
#     print("hellllllllo")
#     return num1+num2  # ريترن دي بتقبي في اخر سطر عندي في فانشكن
# print(calc(10, 5))
#//////////////////////////////// Create a game to calculate your age in days /////////////////////// 
# اله تقولها عندك 25 سنه تقولك عيشت كام يوم
# def calcdays(age):
#     return " Your age in days is : " + str(age*365) + " days"
# print(calcdays(20))
# #اله تقولها عندك 25 سنه تقولك عيشت كام ساعه
# def calchours(age):
#     return " Your age in hours is : " + str(age*365*24) + " hours"
# print(calchours(20))
# #اله المسخدم يدخل سنه ويطلعله عاش كام ساعه
# def calchours(age):
#     return " Your age in hours is : " + str(age*365*24) + " hours"
# print(calchours(int(input("Enter your age: "))))
#///////////////////////////////////////////// If //////////////////////////////////////////////
# اداه شرطيه بنستخدمها لو الشرطه اتحقق نفذ الاوامر الي مكتوبه لو متحققش نفذ الاوامر التانيه
#== يعني  هل  
# egyption = True
# if egyption == True:
# # if not egyption:    
#     print("Yes iam egyption")
#///////////////////////////////////
# egyption = False
# if egyption == True:   
#     print("Yes iam egyption")    
# else:
#     print("Iam not egyption")  
#//////////////////////////////////
# and لازم الشرطين يتحققو
# or شرط واحد يتحقق مش مشكله مش لاز الاتنين
# email = "x@gmail.com"
# password = 1234
# if email == "x@gmail.com" and password == 1234:
#     print("Welcome")
# elif email == "x@gmail.com" and password != 1234:
#     print("Invalid Password")
# elif email != "x@gmail.com" and password == 1234:
#     print("Invalid Email")    
# else:
#     print("Invalid email and password")
#///////////////////////////// Create an application to calculate your score /////////////////////
# ahmed = 89
# if ahmed >= 90:
#     print("Excellent") 
# elif ahmed >= 80:
#     print("Very good") 
# elif ahmed >= 60:
#     print("good") 
# elif ahmed >= 50:
#     print("Successfull") 
# else:
#     print("Not Successfull")
#//////////////////////////////////////////////// IF مقارنات /////////////////////////////////////////////////
# def names(ahmed,hassan,mohamed):
#     if ahmed > hassan and ahmed > mohamed:
#         return ahmed
#     elif hassan > ahmed and hassan> mohamed:
#         return hassan
#     else:
#         return mohamed
# print(names(80,40,91))    
#//////////////////////////////////////////// Calculate ////////////////////////////////////////////
# عندي تلت وحدات في الاله الحاسبه اول رقم وتاني رقم واداه الي تحسب بين الرقمين
# num1 = float (input("Enter number"))
# operator = input()
# num2 = float (input("Enter number"))
# if operator == "+":
#     print(num1+num2)
# elif operator == "-":
#     print(num1-num2)
# elif operator == "*":
#     print(num1*num2)
# elif operator == "/":
#     print(num1/num2)
# elif operator == "^":
#     print(num1**num2)
# else:
#     print("Error")
#//////////////////////////////////////// while loop,continue,break ///////////////////////////////////////
# بدل ما اكتب الامر ميت مره بكتبه مره واحده وهيتكرر في المده الي محدداها
# الي بيتكتب بعد while بيقبي شرط
# i = 1
# while i <= 10:
#     print(i)
#     i = i+1
# i = 1
#/////////////////////////////////// continue /////////////////////////////
# while i <= 10:
#     i = i+1    # كده  بقوله زود واحد قبل ماتطبع
#     if i == 8:
#         continue  # يعني اما يجي رقم 8 اعملها سكيب متجبهاش
#     print(i)
#////////////////////////////////////// break /////////////////////////////////////
# i = 1
# while i <= 10:
#     i = i+1    
#     if i == 8:
#         break  #بيوقف العداد
#     print(i)
#//////////////////////////////////Gameing(if,while loop)////////////////////////////////////////////
#/// لعبه زي من سيربح المليون لو جاوب غلط يعيد السؤال تاني
# secret_answer ="cairo"
# answer = ""
# while secret_answer != answer:
#     answer = input("Whatis capital of egypt?")
# print("You win!")
 ##////// عيزاه يجرب لو دخل كذا محاولع غل يبقي خسران لو دخلها مره صح يبقي كسبان
# secret_answer ="cairo"
# answer = ""
# count = 0
# limit = 3
# lose = False
# while secret_answer != answer and not lose:
#     if count < limit:
#         answer = input("Whatis capital of egypt?")
#         count +=1
#     else:
#         lose = True

# if lose:
#     print("You Lose")
# else:
#     print("You Win")
#////////////////////////////////// For Loop ///////////////////////////////////////////////////////////
#//// بتشتغل علي ليست او اي نوع من البيانات
#//// بع كل حرف في الاسم لوحده
# for name1 in "mayson":
#     print(name1)

# #///// بتتكتب بطريقه تانيه زي
# y = 'ahmed'
# for name2 in y:
#     print(name2)

#//// بيبع كده كل اسم في سطر لوحده
# x = ["ahmed","hasan","mohamed"]
# for name3 in x:
#     print(name3)

#///////////////////////////////// For loop range ////////////////////////////////////////////////
#////  الرنج هيطبع من 0 ل 4قبل الرقم لي حطيته برقم
# for num1 in range(5):
#     print(num1)
# #//// الرنج بتاخد رقم واحد لحد اتنين عادي بردو
# for num2 in range(5,10):
#     print(num2)
# /// ممكن اخليها تعد حروف الاسم
# name = 'ahmed'
# for num3 in range(len(name)):
#     print(num3)
# /////////////////////
# name = ["ahmed","css","php","python"]
# for num3 in range(len(name)):
#     print(name[num3])
#///////////////////////////////////////// For loop dictionary //////////////////////////////////////////////
# بنعمل لوب علي ليست 
# lan = ["js","python","c#","css","java"]
# for lista in range(len(lan)):
#      print(lista)  #هيطبعلي عدد الكلمات
#      print(lan[lista])  #هيطبعلي الي داخل ليست
# //////////////////////////////////////////////////////////
# lan = ["js","python","c#","css","java"]
# for lista in range(len(lan)):
#     if lan[lista] == "python":
#         print(lan[lista],"I love python")
#     else:
#         print(lan[lista])
#////////////////////////////// List In Dictionary ////////////////////////////// 
# info ={
#     "name":"Mayson",
#     "age":"20",
#     "country":"egypt",
# }
# for x in info:
#     print(info[x])
#     print(x)
#//////////////////////////////// try excpect ////////////////////////////////////////
# بستخدمهم عشان ميحصلش اي ايرور
# try:
#     x = 1/0
#     num = int(input("enter number:  "))
#     print(num)
# except ZeroDivisionError as error:
#     print(error)
# except ValueError:
#     print("invalid value")
    
# print("test")
#////////////////////////////////// Read Files //////////////////////////////////
# r يعني عايز اقرا الي جوا الملف
# w يعني عايز اكتب جوا الملف
# a  عايز اضيف حاجه في اخر الملف
# r+ يعني عايز اقرا واكتب في نفس الوقت
# files = open("test.text","r")
# print(files.readable()) # بيقولي قابل للقراءه ولا لا
# print(files.readline()) #بتقرا سطر سطر عندي
# print(files.readlines()) # بتقرا السطور كلها 
# files.close()

# نعمل عليها لوب
# files = open("test.text","r") 
# for lista in files.readlines():
#     print(lista)
# files.close()
#///////////////
# files = open("test.text","r") 
# print( files.read()) #بتطبعه زي ما انا كاتبه
# files.close()
#////////////////////////////////////////////////////////////////////////
# r بقرا الملف,
# r+ بقرا واكتب فيه,
# w  بيمسح القديم واكتب فيه,
# w+ بيمسح ويكتب من الاول,
# a بضيف علي الي كاتبه بس في الاخر,
# a+ بضيف حاجه جديده
# files = open("test.text","r") 
# print(files.read())
# files.close()
# #////////////////////////////
# files = open("test.text","r+") 
# print(files.write("helllllos"))
# files.close()
# #////////////////////////////////
# files = open("test.text","w") 
# print(files.write("Mohammmeddddd"))
# files.close()
# #////////////////////////////////
# files = open("test.text","w+") 
# print(files.write("welcomeeeeeeee"))
# files.close()
# #////////////////////////////////
# files = open("test.text","a") 
# print(files.write("\nMaysooooon"))
# files.close()
# #////////////////////////////////
# files = open("test.text","a+") 
# print(files.write("/nSaidddddd"))
# files.close()
#/////////////////////////////////////// Formating1 ///////////////////////////////////////////////////////
# name= "mayson" 
# age= 20
# country= "egypt"
#print("My name is "+name+" My age is "+str(age)+"  My nationality is "+country)

# print("My name is %s My age is %s My nationality is %s" % (name, age, country))
# print("My nationality is %s" %country)

# # %s  %d  %f
# # s string
# # d int
# # f float

# print("My age is %f" %age)
# print("My age is %d" %age)
# print("My age is %.3f" %age)  #بكتب عدد الصفر الي عايز يظهر
#print("My nationality is %.3f" %country) # بكتبله عدد الحروف الي عايزاها تظهر 
################################  Formating2 ##############################
# name= 'Mayson'
# age= 20
# print("My age is {}" .format(age))
# print("My age is {:,}" .format(100000000))
############################### Formating3 #############################
# a=1
# b=2
# c=3
# print("The Num is {0:f} {2:2f} {1:d}".format(a,b,c))
################################## Formating4 #######################
# a=1
# b=2
# c=3
# print(f"The Num is {a},{b:f},{c:d}")
##################################### Modules1 #############################33
# ملف بايثون بينفذ فكره محدده 
#بيحتوي علي مجموعه من المتغيرات والدوال والكلاسات
#اعاده استخدام الكود
# تساعدك في تنظيم مشروعك
# في modules انا بعملها وفي بيقي جاهز وفي بحمله من النت
##############################################
# (1)modules بعمله انا
#كده بعمل امبورت للملف كله
# import modules
# modules.callName("Ahmed")
#####################################################
# لو عايزه اعمل امبورت لفانكشن معينه
# from modules import callAge
# callAge(26)

# from modules import callName
# callName("Mayson")
################################### Modules2 ################################################
# (2)modules بجيبها من البايثون
# طريقه كتابه
# import math        
# print(math.floor(7.9))
# #طريقه اخري
# from math import ceil
# print(ceil(10.8))

# import random
# print(random.randint(1,10))

# from random import *
# print(randint(5,15))

##################################################### OOP1 ################################################
# لتنظيم الكود سهل قوي ومشهور

# Object-oriented programming : Object -< Attributes, Action

# Object (bird) : Attributes, Action ????

# Attributes Variables : color= "white" str , Weight= 1 int, Speed= 65 int

# Action Functions :Function Fly() Fly, Function Walk() Walk, Function Eat() Eat

####################

# Object (car) : Attributes, Action ????

# Attributes Variables : Color= "Blue" str , Speed= 300 int , Model= 2021 int

# Action Functions :Function Move() Move , Function Return() Return , Function Stop() Stop 

################################# OOP2 ######################################
#الكلاس هو الي بطلع منه كل الاوبجكت
#class: Object,Object,Object

# (Lion a object) <but Lion,cat,dog,horse a animals "Attributes"> (Animal a class)

# Class Car Attributes Variables : Color , Price, Model
# Object Car BMW : Color= "Blue" str , Price = 12444 int, Model= 2021 int
# Object Car Ferary : Color= "Black" str , Price = 14455 int, Model= 2023 int
#Actions Functions

#################################### OOP3 ######################################
#Cars 
# from cars import car
# BMW = car("red", 200000, 2012)
# FORD = car("balck", 400000, 2014)

# print(BMW.carColor)
# print(FORD.carPrice)

#################################### OOP5 ######################################




























































































