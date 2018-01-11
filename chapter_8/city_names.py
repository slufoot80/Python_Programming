def city_country(city, country):
    """"Return a string like 'Santiago, Chile'."""
    return(city.title() + ", " + country.title())

city = city_country('roseville', 'michigan')
print("\n" + city)

city = city_country('corleone', 'sicily')
print("\n" +city)

city = city_country('london', 'england')
print("\n" +city)
