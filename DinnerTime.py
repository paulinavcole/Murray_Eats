'''Dinner Time - your quickest way to find delicious food in NYC!'''

# Import the modules
import requests
import json 
import config   
import restaurants  

def main():

    print('''
            (
            )
        __..---..__
    ,-='  /  |  \  `=-.
    :--..___________..--;
    \.,_____________,./

    ###       ###           ######                                   #######                 ### 
    #  ##### ###  ####     #     # # #    # #    # ###### #####        #    # #    # ###### ### 
    #    #    #  #         #     # # ##   # ##   # #      #    #       #    # ##  ## #      ### 
    #    #   #    ####     #     # # # #  # # #  # #####  #    #       #    # # ## # #####   #  
    #    #            #    #     # # #  # # #  # # #      #####        #    # #    # #          
    #    #       #    #    #     # # #   ## #   ## #      #   #        #    # #    # #      ### 
    ###   #        ####     ######  # #    # #    # ###### #    #       #    # #    # ###### ### 

    Welcome to Dinner Time - your new favorite way to decide what to eat in NYC! 
    The rules of the game are simple, let us know what cuisine you are in the mood for, where you are located, and we will 
    show you the best restaurants in area to pick from that are open now! Now, get hungry, and get picking!
    ''')

    print('We have many options in the area for you to pick from!')
    print('Pick a food and we will let you know if it is available in your area!')
    print('If it is available in the area, we will show you the best restaurants for that cuisine.')
    print('Start by letting us know what you are in the mood for:')
    
    # Get user's input on cuisine they are looking for and store in variable cuisine
    cuisine = input()
   
    
    print('Let us know where you are! Enter your zipcode.')
    
    # Get user's input on zipcode to update parameters
    zip = input()
    

    # Define API Key, Search Type, and header
    APIKEY = config.my_key
    ENDPOINT = 'https://api.yelp.com/v3/businesses/search'
    HEADERS = {'Authorization': 'bearer %s' % APIKEY}

    # Define the parameters of the search
    PARAMETERS = {'location': zip,
                'term' : 'restaurants',
                'sort_by' : 'rating',
                'open_now': 'True',
                'limit' : 50,
                'offset': 50}

    # Make a request to the API, and return results
    response = requests.get(url=ENDPOINT,params=PARAMETERS,headers=HEADERS)

    # Convert JSON string to dictionary
    business_data = response.json()

    for business in business_data['businesses']:
        if cuisine in business['categories'][0]['title']:
            name = business['name']
            cuisine = business['categories'][0]['title']
            address = business['location']['address1']
            print('Name: ' + name + ', ' 'Cuisine: ' + cuisine + ', ' 'Location: ' + address)

# If the program is run instead of imported, run the game:
if __name__ == '__main__':
    main()