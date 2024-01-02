import datetime

def get_user_input():
    name = input("Enter your name: ")
    location = input("Enter your location: ")
    return name, location

def get_current_date():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def display_welcome_message(name, location):
    current_date = get_current_date()
    print(f"Welcome {name}! It is {current_date}. Here is the weather for {location} (weather information placeholder).")

if __name__ == "__main__":
    user_name, user_location = get_user_input()
    display_welcome_message(user_name, user_location)
