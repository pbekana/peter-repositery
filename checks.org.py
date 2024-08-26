import time

# Define an array with names and birthdays as tuples
birthdays = [
    ("John Doe", "1998-07-30"),
    ("Jane Smith", "1995-12-14"),
    ("Alice Johnson", "2001-08-17"),
    ("LEMI GELETU","2008-08-17"),
    ("Dawit Garomsa","1995-04-12"),
    ("Pet De Joy","1996-09-19")
]
birthdays.sort()
print(birthdays,end='\n')
def check_todays_birthdays():
    today = time.strftime('%m-%d')
    flag = False

    for name, birthdate in birthdays:
        if today == birthdate[5:]:
            print(f"Happy Birthday, {name}!")
            flag = True

    if not flag:
    
          print("No birthdays today!")

if __name__ == '__main__':
    check_todays_birthdays()

