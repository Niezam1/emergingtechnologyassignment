import requests, os

def fetchRoomData(tokenData):
    try:
        #Define the URL for the Webex API endpoint to fetch room data
        url = 'https://webexapis.com/v1/rooms'

        #Prepare the header with the authorization token
        headers = {
            'Authorization' : 'Bearer {}'.format(tokenData)
        }

        #Send a GET request to the Webex API endpoint with the header
        response = requests.get(url, headers=headers)
        
        #Check if the response status code indicates success(200)
        if response.status_code == 200:
            #Extract room data from the response
            webexRoom = response.json()

            #Iterate through each room item and print its details
            for room in webexRoom["items"]:
                print("------------------------------------------------------------------------------------------------------------------")
                print("Room ID: " + room["id"])
                print("Room Title: " + room["title"])
                print("Date Created: " + room["created"])
                print("Last Activity: " + room["lastActivity"])
                print("------------------------------------------------------------------------------------------------------------------")

            while True:
                #Offer options to the user after successful connection
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
            #Error message
            print("\nFailed to connect to the server. Please try again.")
            print("--------------------------------------------------")

    #Handle exceptions that might occur during the execution of the code
    except Exception as e:
        #Error message
        print("An error occurred:", e)