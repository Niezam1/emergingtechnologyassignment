import requests, os

def sendMessageToRoom(tokenData):
    try:
        #Define the URL for fetching rooms
        url = 'https://webexapis.com/v1/rooms'

        #Prepare the header for authorization token
        headers = {
            'Authorization' : 'Bearer {}'.format(tokenData)
        }

        #Send a GET request to fetch the list of rooms
        response = requests.get(url, headers=headers)

        #Check if the response status code indicates success(200)
        if response.status_code != 200:
            #error message
            print("Failed to connect to the server. Please try again.")
            print("____________________________________________________")
        else:
            #Extract the room data from the response
            roomData = response.json()
            roomNo = 0

            print("-------------------------------")
            print("          Room Lists           ")
            print("-------------------------------")

            #Iterate through each room and print its details
            for room in roomData["items"]:
                roomNo = roomNo + 1

                print(f"| {roomNo} | {room['title']}")
            
            print("-------------------------------")
            
            #Prompt the user to choose a room by number to send a message
            selectedRoomNo = int(input("Room Number: "))

            #prompt the user to enter the message
            print("")
            message = input("Enter your message: ")

            #mDefine the URL for sending messages
            messages_url = 'https://webexapis.com/v1/messages'

            #Prepare the header for sending messages
            header2 = {
            'Authorization': 'Bearer {}'.format(tokenData),
             'Content-Type': 'application/json'
            }

            #Retrieve the room id of the selected room
            roomId = roomData["items"][selectedRoomNo - 1]["id"]

            #Prepare the parameters for sending message
            params = {'roomId': roomId, 'markdown': message}

            #Send a POST request to send the message to the selected room
            response2 = requests.post(messages_url, headers=header2, json=params)

            #Check if the response status code indicates success(200)
            if response2.status_code != 200:
                #error message
                print("Failed to connect to the server. Please try again.")
                print("____________________________________________________")
                print(response2.json())
            else:
                #success message
                print("")
                print("---------------")
                print("Message Sent!")
                print("---------------")

                while True:
                    #Offer options to the user after successful connection
                    print("")
                    print("--------------------------")
                    print("| 1 | Back To Menu        |")
                    print("| 2 | Exit                |")
                    print("--------------------------")
                    nav = int(input("Enter your choice: "))
            
                    if nav == 1:
                        return
                    elif nav == 2:
                        print("")
                        print("Exiting...")
                        os._exit(0)
                    else:
                        print("")
                        print("* Invalid choice. Please enter 1 or 2. *")

    #Handle exceptions that might occur during the execution of the code                
    except Exception as e:
        #error message
        print("An error occurred:", e)