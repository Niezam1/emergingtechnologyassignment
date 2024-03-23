import requests, os

def fetchData(tokenData):
    try:
        #Define the URL for the Webex API endpoint to fetch user data
        url = 'https://webexapis.com/v1/people/me'

        #Prepare the headers with the authorization token
        headers = {
            'Authorization' : 'Bearer {}'.format(tokenData)
        }

        #Send a GET request to the Webex API endpoint with the header
        response = requests.get(url, headers=headers)
        
        #Check if the response status code indicates success(200)
        if response.status_code != 200:
            #error message
            print("")
            print("****************************************************")
            print("Failed to connect to the server. Please try again.")
            print("____________________________________________________")
        else:
            #success message
            print("")
            print("************************")
            print(" Successfully Connected ")
            print("************************")
            
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