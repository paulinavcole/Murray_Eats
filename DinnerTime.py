'''Dinner Time - your quickest way to find delicious food in NYC!'''

# Import the modules
import requests
import json 
import config   

restaurants = ["Afghan",
"African",
"American",
"Andalusian",
"Arabian",
"Arab",
"Argentine",
"Armenian",
"Asian",
"Asturian",
"Australian",
"Austrian",
"Baguettes",
"Bangladeshi",
"Barbeque",
"Basque",
"Bavarian",
"Beer",
"Beisl",
"Belgian",
"Flemish",
"Bistros",
"Brasseries",
"Brazilian",
"Breakfast",
"British",
"Buffets",
"Bulgarian",
"Burgers",
"Burmese",
"Cafes",
"Cafeteria",
"Cajun/Creole",
"Cambodian",
"Canadian",
"Canteen",
"Caribbean",
"Dominican",
"Haitian",
"Puerto",
"Trinidadian",
"Catalan",
"Cheesesteaks",
"Chicken",
"Chilean",
"Chinese",
"Cantonese",
"Congee",
"Dim Sum",
"Fuzhou",
"Hainan",
"Hakka",
"Henghwa",
"Hokkien",
"Hunan",
"Pekinese",
"Shanghainese",
"Szechuan",
"Teochew",
"Comfort",
"Corsican",
"Creperies",
"Cuban",
"Curry",
"Cypriot",
"Czech",
"Czech/Slovakian",
"Danish",
"Delis",
"Diners",
"Dinner",
"Dumplings",
"Eastern",
"Eritrean",
"Ethiopian",
"Fast",
"Filipino",
"Fischbroetchen",
"Fish",
"Flatbread",
"Fondue",
"Food",
"Freiduria",
"French",
"Game",
"Gastropubs",
"Georgian",
"German",
"Giblets",
"Gluten-Free",
"Greek",
"Guamanian",
"Halal",
"Hawaiian",
"Heuriger",
"Himalayan/Nepalese",
"Honduran",
"Hong Kong",
"Hot",
"Hungarian",
"Iberian",
"Indian",
"Indonesian",
"International",
"Irish",
"Island",
"Israeli",
"Italian",
"Japanese",
"Izakaya",
"Kaiseki",
"Kushikatsu",
"Oden",
"Okinawan",
"Okonomiyaki",
"Onigiri",
"Ramen",
"Robatayaki",
"Soba",
"Sukiyaki",
"Takoyaki",
"Tempura",
"Teppanyaki",
"Tonkatsu",
"Udon",
"Unagi",
"Western",
"Yakiniku",
"Yakitori",
"Jewish",
"Kebab",
"Kopitiam",
"Korean",
"Kosher",
"Kurdish",
"Laos",
"Laotian",
"Latin",
"Colombian",
"Salvadoran",
"Venezuelan",
"Live/Raw",
"Lyonnais",
"Malaysian",
"Mamak",
"Nyonya",
"Meatballs",
"Mediterranean",
"Falafel",
"Mexican",
"Jaliscan",
"Oaxacan",
"Pueblan",
"Tacos",
"Tamales",
"Yucatan",
"Middle",
"Egyptian",
"Lebanese",
"Milk",
"Modern",
"Mongolian",
"Moroccan",
"Nicaraguan",
"Nikkei",
"Noodles",
"Norcinerie",
"Oriental",
"Pakistani",
"Pan",
"Parma",
"Persian/Iranian",
"Peruvian",
"Pita",
"Pizza",
"Polish",
"Pierogis",
"Polynesian",
"Portuguese",
"Potatoes",
"Poutineries",
"Pub",
"Rice",
"Romanian",
"Rotisserie",
"Russian",
"Salad",
"Sandwiches",
"Scandinavian",
"Schnitzel",
"Scottish",
"Seafood",
"Serbo",
"Singaporean",
"Slovakian",
"Somali",
"Soul",
"Soup",
"Southern",
"Spanish",
"Steakhouses",
"Supper",
"Sushi",
"Swabian",
"Swedish",
"Swiss",
"Syrian",
"Tabernas",
"Taiwanese",
"Tapas",
"Tapas/Small",
"Tavola",
"Tex-Mex",
"Thai",
"Traditional",
"Trattorie",
"Turkish",
"Chee",
"Gozleme",
"Homemade",
"Lahmacun",
"Ottoman",
"Ukrainian",
"Uzbek",
"Vegan",
"Vegetarian",
"Venison",
"Vietnamese",
"Waffles",
"Wok",
"Wraps",
"Yugoslav"]

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
   
   # Check if user's input is available as an option
    if cuisine.casefold() not in map(str.casefold,restaurants):
        print("Please try another type of food! This is not available.")
        exit()

    print('Let us know where you are looking for food! Enter your zipcode.')
    
    # Get user's input on zipcode to update parameters
    zip = input()
    
    # Convert cuisine to title case to interface with Yelp API
    cuisine_title = cuisine.title()

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

    business_data = response.json()

    # Set boolean variable to False to use as check if cuisine is found in dictionary
    cuisines_available = False

    # Iterate through businesses to output name, cuisine type, and location of restaurants that fit search parameter
    for business in business_data['businesses']:
        if cuisine_title in business['categories'][0]['title']:
            name = business['name']
            cuisine_title = business['categories'][0]['title']
            address = business['location']['address1']
            cuisines_available = True
            print('Name: ' + name + ', ' 'Cuisine: ' + cuisine_title + ', ' 'Location: ' + address)
    
    # Check if boolean didn't flip to True. If so, tell the user to make another selection 
    if cuisines_available == False:
        print("This is not found! Try another cuisine!")

# If the program is run instead of imported, run the program:
if __name__ == '__main__':
    main()