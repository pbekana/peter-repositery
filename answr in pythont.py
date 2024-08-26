# this programm perform the food dispencery machine  work
import numpy as np
class foodmenu:
 name = "show ure name"
 calories = 56
 IsAdultOnly = 'teenage'
 IsAlcohol ='beer'
def __init__(self,name,calories,IsAdultOnly,IsAlcohol):
    
        self.name = name
        self.calories = calories
        self.IsAdultOnly = IsAdultOnly
        self.IsAlcohol = IsAlcohol
# SJF;LF
def func(self):
      print(self.name)
      print(self.calories)
      print(self.IsAdultOnly)
      print(self.IsAlcohol)
# fg
obj1 = foodmenu(chips,150,false,false,
            candy,300,false,false,
            nuts,250,false,true,juice,80,false,false,
           soda,180,false,false,
           beer,200,true,true)
# df
obj1.func()
# displaying available categories variables
def displaycatogires():
    print("Snacks")
    print("Drinks")
    print("Desserts")
    # checking the dispenced based on criterior
def candispence( Itemitem):
     return (item.calories > 200) or ( item.isAlcohol or item.isAdultOnly)
    # creating a vector
    
    Snacks = "chips",150,false,false
            "candy",300,false,false
            {"nuts",250,false,true
    Drinks="juice",80,false,false,
           "soda",180,false,false
           "beer",200,true,true
    Dresserts="ice cream",250,false,false
              "cake",350,false,false
              "cupcake",300,false,true
              displaycatogires():
print("please enter ure choice")
 categorychoice == int(input())
 match categorychoice:
     case categorychoice == Snacks:
     categoryname == "SNACKS"
     case categorychoice == Drinks:
      categoryname == "Drinks"
      case categorychoice == Desserts:
      categoryname == "Desserts"
      case _:
          print("invalid choice please try to choose the number one up to four")
      if (itemChoice >= 1 && itemChoice <= selectedCategory.size())
        const Item& selectedItem = selectedCategory[itemChoice-1];
        if (canDispenseItem(selectedItem)) 
            print ( "Dispensing " ( selectedItem.name ( ". Enjoy!\n")
         else 
            print ( "Sorry, this item cannot be dispensed.\n")
        
        else:
          print ( "Invalid item choice. Exiting.\n");
        return 1
   
              
