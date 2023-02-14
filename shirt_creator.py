def make_shirt(size, text):
    """Displays size and text for the shirt"""
    print(f'\nThe shirt will be size {size} and will say "{text}"\n')

customers = {}

design_active = True

while design_active:
    user_start = input("Would you like to design a shirt? (Yes/No): ").title()
    if user_start == 'No':
        print("\nWere sorry to see you go...Come back soon!")
        design_active = False
        continue
    elif user_start != 'Yes':
        print("That is not a valid response...please type Yes or No.")
        continue
    else:
        full_name = input("What is your full name?: ").title()
        user_size = input("Enter a shirt size?: ").title()
        user_text = input("Enter what you would like the shirt to say?: ")

        order_info = {user_size: user_text}

        customers[full_name] = order_info

    make_shirt(user_size, user_text)

print(customers)


    