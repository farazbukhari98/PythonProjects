import folium
import googlemaps
import pandas

gmaps = GoogleMaps("AIzaSyAQjAy3erNNqIyCztFRwCcNT8Z377gD82Y")

address = "320 Christopher Luke Circle, Perry, GA 31069"

lat, lng = gmaps.address_to_latlng(address)

print(lat, lng)
#data = pandas.read_csv("CrimedataATL.csv")

#location = list(data["location"])

#map = folium.Map(location = [33.74, -84.38], zoom_start = 10)


# fg = folium.FeatureGroup(name = "CrimeData")

# for address in zip(location):
#     fg.add_child(folium.Marker(location = [], popup = None))


 #Convert all addresses into lattitude and longitude
 #for address in zip(location):





#map.add_child(fg)
#map.save("CrimeApp.html")
