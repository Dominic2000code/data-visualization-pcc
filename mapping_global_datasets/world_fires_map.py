from pathlib import Path
import csv

import plotly.express as px


path = Path('eq_data/world_fires_7_day.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_rows = next(reader)

lons, lats, all_brightness, dates = [], [], [], []
for row in reader:
    lat = float(row[0])
    lon = float(row[1])
    brightness = float(row[2])
    date = row[5]
    lats.append(lat)
    lons.append(lon)
    all_brightness.append(brightness)
    dates.append(date)

title = ''
fig = px.scatter_geo(lat=lats,
                     lon=lons,
                     size=all_brightness,
                     title=title,
                     color=all_brightness,
                     color_continuous_scale='reds',
                     labels={'color': 'Brightness'},
                     projection='natural earth',
                     hover_name=dates,
                     )
fig.show()
