# Initial variable to track shopping status
shopping = 'y'

# List to track pie purchases
pie_purchases = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# Pie List
pie_list = ["Pecan", "Apple Crisp", "Bean", "Banoffee", "Black Bun",
            "Blueberry", "Buko", "Burek", "Tamale", "Steak"]

# Display initial message
print("Welcome to the House of Pies! Here are our pies:")

# While we are still shopping...
while shopping == "y":

    # Show pie selection prompt
    print("---------------------------------------------------------------------")
    print("(1) Pecan, (2) Apple Crisp, (3) Bean, (4) Banoffee, " +
          " (5) Black Bun, (6) Blueberry, (7) Buko, (8) Burek, " +
          " (9) Tamale, (10) Steak ")

    pie_choice = int(input("Which would you like? "))
    
    pie_choice -= 1

    pie_purchases[pie_choice] += 1

    print("------------------------------------------------------------------------")

    # Inform the customer of the pie purchase
    print("Great! We'll have that " + pie_list[pie_choice] + " right out for you.")

    # Provide exit option
    # Prompt the user if they would like to make another purchase
    # YOUR CODE HERE
    shopping = input("Would you like to make another purchase? (y/n) ")

# Once the pie list is complete
print("------------------------------------------------------------------------")

# Count instances of each pie
print("You purchased: ")

# Loop through the full pie list
# YOUR FOR LOOP HERE
for i in range(0, len(pie_list)):
    print(f" {pie_purchases[i]} {pie_list[i]}")

    # Gather the count of each pie in the pie list and print them alongside the pies
    # YOUR CODE HERE
