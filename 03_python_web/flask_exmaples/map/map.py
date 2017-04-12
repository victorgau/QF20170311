from flask import Flask, render_template
import folium
import geocoder

app = Flask(__name__)

@app.route('/')
def index():
    map_osm = folium.Map()
    return map_osm._repr_html_()

@app.route('/<location>')
def map(location):
    center = geocoder.osm(location).latlng
    map_osm = folium.Map(location=center, zoom_start=16)
    return map_osm._repr_html_()
