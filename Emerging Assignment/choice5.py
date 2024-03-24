import requests
import os

def sendMessageToRoom(tokenData):
    try:
        # Define the URL for fetching rooms
        url = 'https://webexapis.com/v1/rooms'

        # Prepare the header for authorization token
        headers = {'Authorization': 'Bearer {}'.format(tokenData)}

        # Send a GET request to fetch the list of rooms
        response = requests.get(url, headers=headers)

        # Check if the response status code indicates success(200)
        if response.status_code != 200:
            print("Failed to connect to the server. Please try again.")
            print("--------------------------------------------------")
            return

        # Extract the room data from the response
        roomData = response.json()
        roomNo = 0

        print("-------------------------------")
        print("          Room Lists           ")
        print("-------------------------------")

        # Iterate through each room and print its details
        for room in roomData["items"]:
            roomNo += 1
            print(f"| {roomNo} | {room['title']}")

        print("-------------------------------")

        # Prompt the user to choose a room by number to send a message
        while True:
            try:
                selectedRoomNo = int(input("Room Number: "))
                if 1 <= selectedRoomNo <= len(roomData["items"]):
                    break
                else:
                    print("Invalid room number. Please enter a valid room number.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        # Prompt the user to enter the message
        message = input("Enter your message: ")

        # Define the URL for sending messages
        messages_url = 'https://webexapis.com/v1/messages'

        # Retrieve the room id of the selected room
        roomId = roomData["items"][selectedRoomNo - 1]["id"]

        # Prepare the header for sending messages
        header2 = {
            'Authorization': 'Bearer {}'.format(tokenData),
            'Content-Type': 'application/json'
        }

        # Prepare the parameters for sending message
        params = {'roomId': roomId, 'markdown': message}

        # Send a POST request to send the message to the selected room
        response2 = requests.post(messages_url, headers=header2, json=params)

        # Check if the response status code indicates success(200)
        if response2.status_code == 200:
            print("---------------")
            print("Message Sent!")
            print("---------------")

            # Offer options to the user after successful connection
            while True:
                print("\n--------------------------")
                print("| 1 | Back To Menu        |")
                print("| 2 | Exit                |")
                print("--------------------------")
                nav = int(input("Enter your choice: "))
        
                if nav == 1:
                    return
                elif nav == 2:
                    print("\nExiting...")
                    os._exit(0)
                else:
                    print("\n* Invalid choice. Please enter 1 or 2. *")
        else:
            print("\nFailed to connect to the server. Please try again.")
            print("--------------------------------------------------")

    # Handle exceptions that might occur during the execution of the code
    except Exception as e:
        print("An error occurred:", e)