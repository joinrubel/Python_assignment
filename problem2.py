def greet(name):
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
        
        # 📂 Open name.txt in write mode ('w') and save the uppercase name
        with open("name.txt", "a") as file:
            file.write(user_name.upper() + "\n")
            
            
        print("Successfully saved to name.txt!")
        break  

    except ValueError as message:
        print("\n" + "=" * 30)
        print(f"Error: {message}")
        print("=" * 30 + "\n")
        continue 
