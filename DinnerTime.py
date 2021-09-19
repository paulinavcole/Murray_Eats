'''Dinner Time - your quickest way to find delicious food in NYC!'''

# Import the modules
import requests
import json 
import config   

def main():

    restaurants = ["Afghan", "African", "American", "Andalusian", "Arabian", "Arab", "Argentine", "Armenian", "Asian", "Asturian",
    "Australian",	"Austrian","Baguettes",	"Bangladeshi", "Barbeque", "Basque", "Bavarian", "Beer", "Beisl", "Belgian",
    "Bistros", "Brasseries", "Brazilian",	"Breakfast", "British",	"Buffets", "Bulgarian",	"Burgers", "Burmese", "Cafes",
    "Cafeteria", "Cajun/Creole", "Cambodian",	"Canadian", "Canteen", "Caribbean", "Catalan", "Cheesesteaks", "Chicken", "Chilean",
    "Chinese", "Cantonese",	"Congee",	"Dim", "Fuzhou", "Hainan", "Hakka",	"Henghwa", "Hokkien", "Hunan", "Pekinese", "Shanghainese",
    "Szechuan", "Teochew", "Comfort",	"Corsican", "Creperies", "Cuban",	"Curry", "Cypriot",	"Czech", "Czech/Slovakian",	"Danish",	
    "Delis",	"Diners",	"Dinner",	"Dumplings", "Eastern", "Eritrean", "Ethiopian", "Fast", "Filipino", "Fischbroetchen", "Fish",
    "Flatbread", "Fondue", "Freiduria", "French", "Gastropubs", "Georgian",	"German",	"Gluten-Free", "Greek",	"Guamanian",
    "Halal", "Hawaiian", "Heuriger", "Himalayan/Nepalese", "Honduran", "Hungarian",	"Iberian", "Indian", "Indonesian",
    "International", "Irish", "Island", "Israeli", "Italian", "Japanese", "Jewish", "Kebab", "Kopitiam", "Korean", "Kosher", "Kurdish",
    "Laos", "Laotian", "Latin", "Malaysian", "Mamak",	"Nyonya",	"Meatballs", "Mediterranean", "Falafel", "Mexican",	"Egyptian",
    "Lebanese", "Milk",	"Modern",	"Mongolian", "Moroccan", "Nicaraguan", "Noodles", "Oriental",	"PF/Comercial", "Pakistani",
    "Pan", "Persian/Iranian", "Peruvian",	"Pita", "Pizza", "Polish", "Pierogis", "Polynesian", "Portuguese", "Potatoes", "Poutineries",
    "Pub", "Rice", "Romanian", "Rotisserie", "Russian", "Salad", "Sandwiches", "Scandinavian", "Schnitzel", "Scottish",	"Seafood",
    "Serbo", "Signature", "Singaporean", "Slovakian", "Somali", "Soul",	"Soup", "Southern",	"Spanish", "Steakhouses", "Supper",
    "Sushi", "Swabian",	"Swedish", "Swiss",	"Syrian",	"Tabernas", "Taiwanese", "Tapas",	"Tavola",	"Tex-Mex", "Thai", "Traditional",
    "Trattorie", "Turkish", "Ukrainian", "Uzbek", "Vegan", "Vegetarian", "Venison", "Vietnamese", "Waffles", "Wok",	"Wraps",
    "Yugoslav"]

    newRestaurants = [x.lower() for x in restaurants]

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