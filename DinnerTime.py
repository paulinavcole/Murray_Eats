'''Dinner Time - your quickest way to find delicious food in NYC!'''

# Import the modules
import requests
import json 
import config   

restaurants = ["Afghan",
"African",
"Senegalese",
"South",
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
"Black",
"Brasseries",
"Brazilian",
"Central",
"Northeastern",
"Northern",
"Rodizios",
"Breakfast",
"Pancakes",
"British",
"Buffets",
"Bulgarian",
"Burgers",
"Burmese",
"Cafes",
"Themed",
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
"Dim",
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
"Alsatian",
"Auvergnat",
"Berrichon",
"Bourguignon",
"Mauritius",
"Nicoise",
"Provencal",
"Reunion",
"Galician",
"Game",
"Gastropubs",
"Georgian",
"German",
"Baden",
"Franconian",
"Hessian",
"Palatine",
"Rhinelandian",
"Giblets",
"Gluten-Free",
"Greek",
"Guamanian",
"Halal",
"Hawaiian",
"Heuriger",
"Himalayan/Nepalese",
"Honduran",
"Hong",
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
"Abruzzese",
"Altoatesine",
"Apulian",
"Calabrian",
"Cucina",
"Emilian",
"Friulan",
"Ligurian",
"Lumbard",
"Napoletana",
"Piemonte",
"Roman",
"Sardinian",
"Sicilian",
"Tuscan",
"Venetian",
"Japanese",
"Blowfish",
"Conveyor",
"Donburi",
"Gyudon",
"Oyakodon",
"Hand",
"Horumon",
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
"New",
"Nicaraguan",
"Night",
"Nikkei",
"Noodles",
"Norcinerie",
"Open",
"Oriental",
"PF/Comercial",
"Pakistani",
"Pan",
"Parent",
"Parma",
"Persian/Iranian",
"Peruvian",
"Pita",
"Pizza",
"Polish",
"Pierogis",
"Polynesian",
"Pop-Up",
"Portuguese",
"Alentejo",
"Algarve",
"Azores",
"Beira",
"Fado",
"Madeira",
"Minho",
"Ribatejo",
"Tras-os-Montes",
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
"Signature",
"Singaporean",
"Slovakian",
"Somali",
"Soul",
"Soup",
"Southern",
"Spanish",
"Arroceria",
"Sri",
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
        print("Please try another type of Cuisine! This is not available.")
        exit()

    print('Let us know where you are! Enter your zipcode.')
    
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

    # Convert JSON string to dictionary
    business_data = response.json()

    for business in business_data['businesses']:
        if cuisine_title in business['categories'][0]['title']:
            name = business['name']
            cuisine_title = business['categories'][0]['title']
            address = business['location']['address1']
            print('Name: ' + name + ', ' 'Cuisine: ' + cuisine_title + ', ' 'Location: ' + address)

# If the program is run instead of imported, run the program:
if __name__ == '__main__':
    main()