#Write a program that adds to a travel log
#Create a function add_new_country to add the Russia's travel 

travel_log = [
{
    "country":"France",
    "visits":12,
    "cities":["Paris","Lille","Dijon"]
},
{
    "country":"Germany",
    "visits":5,
    "cities":["Berlin","Hamburg","Stuttgart"]
},
]
country_new={}
def add_new_country(country_visited,visit_times,visited_cities):
    country_new["country"]=country_visited
    country_new["visits"]=visit_times
    country_new["cities"]=visited_cities
    travel_log.append(country_new)
    
add_new_country("Russia",3,["Moscow","Saint Petersberg","Kremlin"])
print(travel_log)

