user_input = input("Enter any value: ")
print("You entered:", user_input)
try:
    value = int(user_input)
except ValueError:
    try:
        value = float(user_input)
    except ValueError:
        value = user_input
if isinstance(value, int):
    print(f"Raw input is {user_input}: Data type: int")
elif isinstance(value, float):
    print(f"Raw input is {user_input}: Data type: float")
elif isinstance(value, str):
    print(f"Raw input is {user_input}: Data type: str")
