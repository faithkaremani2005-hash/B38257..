print("1. Add")
print("2. View")
print("3. Exit")



while True:
    try:
        option = input("Select an option: ")
    except ValueError:
        print("Select a valid option.")

    match option:
        case "1":
            print("Adding...")
        case "2":
            print("Viewing...")
        case "3":
            print("Exiting...")
            break
        case _:
            print("Invalid input")