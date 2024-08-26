# tut on __name__ function 216
def LunchMealOptions():
    print("welcome to Lunch Meal Options") 
    print("1:-Caesar salad")
    print("2:- Spicy chicken wrap")
    print("3:- Butternut squash soup")
def DinnerMealOptions():
     print("welcome to Dinner Meal Options") 
     print("4:Baked salmon-")
     print("5:-Turkey burger ")
     print("6:-Mushroom risotto ")
ilnpu = input()
if ilnpu == "lunch" :
 LunchMealOptions()
elif ilnpu == "Dinner" :
    DinnerMealOptions()
choice = int(input())
if choice == 1:
   print("ure order :","1:-Caesar salad")
# Body 1
elif choice == 2:
   print("ure order :","2:- Spicy chicken wrap")
# Body 2
elif choice == 3 :
   print("ure order :","3:- Butternut squash soup")
# Body 3
#else:
   # print("invalid choice please try to choose number 1 up to 4")
elif choice == 4:
      print("ure order :","4:-Baked salmon--")
# Body 1
elif choice == 5:
      print("ure order :","5:-Turkey burger ")
# Body 2
elif choice == 6 :
     print("ure order :","6:- Mushroom risotto")
# Body 3
else:
       print("invalid choice please try to choose number 1 up to 4")
    # some problem x%2 == 0 "even" else "odd"
x = 12
if  x != 12:
    print("not equal")
else:
    print(x)

   
