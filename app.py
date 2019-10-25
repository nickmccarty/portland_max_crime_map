from flask import Flask, render_template
import folium
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    # Set basemap

    crime_map = folium.Map(location = [45.54, -122.6750],
                        zoom_start = 11,
                        tiles = 'stamentoner')
 
# Iteratively add circle markers to map

    crime_count_by_station_id = pd.read_csv('data/crime_count.csv', index_col=0)

    for i in range(0, len(crime_count_by_station_id)):
        
        folium.Circle(
            
            location = [crime_count_by_station_id.iloc[i]['latitude'],
                        crime_count_by_station_id.iloc[i]['longitude']],
            tooltip = "Crimes within ~500 ft in 2019 (YTD): " + str(crime_count_by_station_id.iloc[i]['count']),
            popup = crime_count_by_station_id.iloc[i]['name'],
            radius = str(crime_count_by_station_id.iloc[i]['count']),
            color = 'crimson',
            fill = True,
            fill_color = 'crimson'
        
        ).add_to(crime_map)

    crime_map.save('templates/map.html')
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)