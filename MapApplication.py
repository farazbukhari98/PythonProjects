import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
names = list(data["NAME"])

def color_producer(elevation):
    if (elevation < 1000):
        return "green"
    elif (1000 <= elevation < 3000):
        return "orange"
    else:
        return "red"


html = """<h4>Volcano information:</h4>"""

#I put the lat and lon to start at the center of the United States
map = folium.Map(location = [40.76, 111.89], zoom_start = 6, tiles = "Stamen Terrain")

fgv = folium.FeatureGroup(name = "Volcanoes")

for lattitude, longitude, elevation, name in zip(lat, lon, elev, names):
    iframe = folium.IFrame(html = html + "Name: " + str(name) + "<br/>" + "<br/>" + "Elevation: " + str(elevation) + " meters", width=200, height=100)
    fgv.add_child(folium.CircleMarker(location=[lattitude, longitude], popup = folium.Popup(iframe), fill_color = color_producer(elevation), color = "gray", fill_opacity = 0.7))

fgp = folium.FeatureGroup(name = "Population")

fgp.add_child(folium.GeoJson(data = open("world.json", "r", encoding = "utf-8-sig").read(), style_function = lambda x: {"fillColor":"green" if x["properties"]["POP2005"] < 10000000 else "orange" if 10000000 <= x["properties"]["POP2005"] < 20000000 else "red"}))


map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("Map1.html")
