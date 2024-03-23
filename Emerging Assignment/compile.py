import requests, os

# call file
from choice1 import fetchData
from choice2 import fetchUserData
from choice3 import fetchRoomData
from choice4 import createRoom
from choice5 import sendMessageToRoom

#Menu
print("====================")
print("       WEBEX       ")
print("====================")

try:
    tokenData = ""

    while True:
        #Prompt user for token
        tokenData = input("Enter the token: ")

        #Verify token by making a request to Webex API
        url = 'https://webexapis.com/v1/people/me'

        #Prepare the header for authorization token
        headers = {
            'Authorization' : 'Bearer {}'.format(tokenData)
        }

        response = requests.get(url, headers=headers)

        #Check response status
        if response.status_code == 200:
            break
        else:
            #error message
            print("Failed to connect to the server. Please try again.")
            print("____________________________________________________")

    while True:
        print("")
        print("")

        #Display menu options
        print("================================")
        print("|             MENU              |")
        print("--------------------------------")
        print("| 0 | Test Connection To Webex  |")
        print("| 1 | Fetch User Data           |")
        print("| 2 | Fetch Room Data           |")
        print("| 3 | Create Room               |")
        print("| 4 | Send Message To Room      |")
        print("| 5 | Exit                      |")
        print("================================")

        select = int(input("Enter your choice: "))

        #User chooses option 0
        if select == 0:
            fetchData(tokenData)

        #User chooses option 1
        if select == 1:
            fetchUserData(tokenData)

        #User chooses option 2
        if select == 2:
            fetchRoomData(tokenData)

        #User chooses option 3
        if select == 3:
            createRoom(tokenData)

        #User chooses option 4
        if select == 4:
            sendMessageToRoom(tokenData)

        #User chooses option 5
        if select == 5:
            print("")
            print("Exiting...")
            os._exit(1)

#Handle exceptions that might occur during the execution of the code
except Exception as e:
    print("An error occurred:", e)