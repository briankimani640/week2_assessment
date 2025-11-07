day_of_week = input("Please enter the day of the week (where Mon = 1 all the way to sunday = 7): ")
match day_of_week:
    case "1":
        print("Monday!")
    case "2":
        print("Tuesday!")
    case "3":
        print("Wednesday!")
    case "4":
        print("Thursday!") 
    case "5":
        print("Looking forward to the weekend!")
    case "6":
        print("Looking forward to the weekend!")
    case "7":
        print("Looking forward to the weekend!")
    case _:
        print("Invalid day number.")

