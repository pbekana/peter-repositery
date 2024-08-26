class Item:
    def __init__(self, name, calories, is_alcohol, is_adult_only):
        self.name = name
        self.calories = calories
        self.is_alcohol = is_alcohol
        self.is_adult_only = is_adult_only

def displayCategories():
    print("Categories:")
    print("1. Snacks")
    print("2. Drinks")
    print("3. Desserts")

def displayItems(items, category):
    print(f"Items in {category}:")
    for item in items:
        print(f"{item.name} ({item.calories} calories)")

def canDispenseItem(item):
    return not (item.calories > 200 or item.is_alcohol or item.is_adult_only)

def main():
    snacks = [
        Item("Chips", 150, False, False),
        Item("Candy", 300, False, False),
        Item("Nuts", 250, False, True)  # Adult only
    ]
    drinks = [
        Item("Juice", 80, False, False),
        Item("Soda", 180, False, False),
        Item("Beer", 200, True, True)  # Alcohol
    ]
    desserts = [
        Item("Ice Cream", 250, False, False),
        Item("Cake", 350, False, False),
        Item("Cupcake", 300, False, True)  # Adult only
    ]

    displayCategories()
    categoryChoice = int(input("Enter the category number (1-3): "))
    if categoryChoice == 1:
        selectedCategory = snacks
        categoryName = "Snacks"
    elif categoryChoice == 2:
        selectedCategory = drinks
        categoryName = "Drinks"
    elif categoryChoice == 3:
        selectedCategory = desserts
        categoryName = "Desserts"
    else:
        print("Invalid category choice. Exiting.")
        return

    displayItems(selectedCategory, categoryName)
    itemChoice = input("Enter the item name: ")
    for item in selectedCategory:
        if item.name.lower() == itemChoice.lower():
            if canDispenseItem(item):
                print(f"Dispensing {item.name}. Enjoy!")
            else:
                print(f"Sorry, {item.name} cannot be dispensed for kids.")
            break
    else:
        print("Item not found in the selected category.")

if __name__ == "__main__":
    main()
