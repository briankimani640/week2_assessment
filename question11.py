user_profile = {
    "name": "Jane Doe",
    "email": "jane@example.com",
    "verified": False
}
response = input("Is your email verified? (yes/no): ").lower()
if response == "yes":
    user_profile["verified"] = True
    print("Updated user profile:", user_profile)
else:
    print("Verification pending.")