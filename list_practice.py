US_cities=["Oakland", "Atlanta", "New York City", "Seattle", "Memphis", "Miami", "Boston", "Los Angeles", "Denver","New Orleans"]
print(US_cities)

print (US_cities[0],US_cities[2],US_cities[7])
three_cities = US_cities[3:6]
print (three_cities)
US_cities[0]= "San Francisco"
US_cities[2]= "BrookLyn"
US_cities[7]= "Hollywood"
US_cities[5]= "Tampa"
print (US_cities)

US_cities.append ("Oakland")
US_cities.extend(["New York City", "Los Angeles"])
US_cities.insert(0,"Miami")
print(US_cities)

del  US_cities[4]
US_cities.pop(5)
US_cities.remove("Boston")
print(US_cities)


Rappers=["Lil Uzi", "Drake", "J.Cole", "Tupac", "Travis Scott", "Kanye West", "Kendrick Lamar", "Lil Baby", "21 Savage", "Jack Harlow"]
print(Rappers)
three_rappers= Rappers[0:4]
print (three_rappers)

