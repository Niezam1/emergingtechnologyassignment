import requests
import os

# Import functions
from choice1 import fetchData
from choice2 import fetchUserData
from choice3 import fetchRoomData
from choice4 import createRoom
from choice5 import sendMessageToRoom

def get_user_input(prompt):
    """
    Helper function to get user input with clear prompt.
    """
    return input(prompt).strip()

def display_menu():
    """
    Function to display the menu options.
    """
    print("\n================================")
    print("|             MENU              |")
    print("--------------------------------")
    print("| 0 | Test Connection To Webex  |")
    print("| 1 | Fetch User Data           |")
    print("| 2 | Fetch Room Data           |")
    print("| 3 | Create Room               |")
    print("| 4 | Send Message To Room      |")
    print("| 5 | Exit                      |")
    print("================================")

# Main program
print("====================")
print("       WEBEX       ")
print("====================")

try:
    tokenData = ""

    # Prompt user for token
    while True:
        tokenData = get_user_input("Enter the token: ")

        # Verify token by making a request to Webex API
        url = 'https://webexapis.com/v1/people/me'

        # Prepare the header for authorization token
        headers = {'Authorization': 'Bearer {}'.format(tokenData)}

        response = requests.get(url, headers=headers)

        # Check response status
        if response.status_code == 200:
            break
        else:
            # Error message for failed connection
            print("\nFailed to connect to the server. Please try again.")
            print("--------------------------------------------------")

    while True:
        display_menu()
        
        try:
            select = int(get_user_input("Enter your choice: "))

            if select == 0:
                fetchData(tokenData)
            elif select == 1:
                fetchUserData(tokenData)
            elif select == 2:
                fetchRoomData(tokenData)
            elif select == 3:
                createRoom(tokenData)
            elif select == 4:
                sendMessageToRoom(tokenData)
            elif select == 5:
                print("\nExiting...")
                os._exit(0)
            else:
                print("\nInvalid choice. Please enter a number between 0 and 5.")
        except ValueError:
            print("\nInvalid input. Please enter a number.")

# Handle exceptions that might occur during the execution of the code
except Exception as e:
    print("\nAn error occurred:", e)