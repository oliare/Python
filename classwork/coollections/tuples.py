# ------ tuple: fixed size, cannot modify
coord = (1, 10)

location = (12.653, 10.5553, "Rivne", "Ukraine")
print(location[3])

lon, lat, city, country = location
print("City: ", city)