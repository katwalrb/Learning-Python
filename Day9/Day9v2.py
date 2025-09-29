#Nested dictionary in a dictionary

travel_log = {
    "France":{"cities_visited":["Paris","Lille","Dijon"],"total_visits": 12},
    "Germany":{"cities_visited":["Berlin","Hamberg","Dortmund"],"total_visits":3},
}
print(travel_log)

#Nested dictionary in a list
travel_log = [
    {
        "country":"France",
        "cities_visited":["Paris","Lille","Dijon"],
        "total_visits": 12,
    },
    {
        "country":"Germany",
        "cities_visited":["Berlin","Hamberg","Dortmund"],
        "total_visits": 3,        
    },
]
print(travel_log)

