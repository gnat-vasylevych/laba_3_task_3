from flask import Flask, render_template, request
import logic
import folium
from geopy.geocoders import Nominatim

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/get', methods=['POST'])
def get_data_from_html():
    """
    Gets information from server and create map
    """
    name = request.form.get('screen_name')
    token = request.form.get('access_token')
    data = logic.get_data(token, name)
    friends = logic.extract_info(data)
    map = folium.Map(tiles="Stamen Terrain")
    geolocator = Nominatim(user_agent="Vlad")
    for el in friends:
        location = geolocator.geocode(el[0])
        if location is None:
            continue
        coordinates = (location.latitude, location.longitude)
        map.add_child(folium.Marker(location=coordinates, popup=el[1], icon=folium.Icon()))
    return map._repr_html_()


if __name__ == "__main__":
    app.run(debug=True)


