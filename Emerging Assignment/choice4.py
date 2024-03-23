import requests, os

def createRoom(tokenData):
    try:
        #Define the URL for the Webex API endpoint to create a room
        url = 'https://webexapis.com/v1/rooms'

        #Prepare the header with the authorization token and content type
        headers = {
            'Authorization' : 'Bearer {}'.format(tokenData),
            'Content-Type': 'application/json'
        }

        #Prompt the user to enter the room name
        print("")
        roomName = input("Enter room name: ")

        #Prepare the parameters for the POST request
        params = { 'title' : roomName }

        #Send a POST request to create the room with the provided name
        response = requests.post(url, headers=headers, json=params)

        #Check if the response status code indicates success(200)
        if response.status_code != 200:
            #error message
            print("Failed to connect to the server. Please try again.")
            print("____________________________________________________")
        else:
            #print output
            print("")
            print("-----------------------------")
            print("Room Successfully Created!")
            print("-----------------------------")

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