def greet(name):
    # Notice .upper() is INSIDE the curly braces right next to name
    print(f"hellow {name.upper()}")

while True:
    user_name = input("Enter Your name: ")

    try:
        if user_name.strip() == "":
            raise ValueError("Name cannot be empty! Please try again.")
            
        if not user_name.replace(" ", "").isalpha():
            raise ValueError("Name must contain letters only! Please try again.")

        print("\n" + "=" * 30)
        greet(user_name)
        print("=" * 30)
        break  

    except ValueError as message:
        print("\n" + "=" * 30)
        print(f"Error: {message}")
        print("=" * 30 + "\n")
        continue
