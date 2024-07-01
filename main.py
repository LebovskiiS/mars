from flask import Flask
from flask import render_template
import requests
import json
app = Flask(__name__)


@app.route('/')
def mars_photos():
    data = requests.get('https://api.nasa.gov/mars-photos/api/v1/rovers/perseverance/latest_photos?api_key=DEMO_KEY')
    json_data = json.loads(data.text)
    photos = json_data['latest_photos']
    return render_template('index.html', photos= photos)





app.run(debug= True)