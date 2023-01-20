import csv
from pathlib import Path
from datetime import datetime

import matplotlib.pyplot as plt

path = Path('weather_data/sitka_weather_2021_full.csv')
# path = Path('weather_data/death_valley_2021_full.csv')


lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)
index_header = {}
for index, column_header in enumerate(header_row):
    index_header[column_header] = index


rain_falls, dates = [], []
for row in reader:
    try:
        current_date = datetime.strptime(row[index_header['DATE']], '%Y-%m-%d')
        rain_fall = float(row[index_header['PRCP']])
    except ValueError:
        continue
    else:
        dates.append(current_date)
        rain_falls.append(rain_fall)

# print(rain_falls)

# Plot the precipitations.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, rain_falls, color='red', alpha=0.5)
# ax.plot(dates, lows, color='blue', alpha=0.5)
# ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)


# Format plot.
title = "Daily Rainfall in Sitka, Alaska 2021"
# title = "Daily Rainfall in Death Valley, CA 2021"
ax.set_title(title, fontsize=20)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('Precipitations(rainfalls)', fontsize=16)
ax.tick_params(labelsize=16)

plt.show()
# plt.savefig('daily_rainfall_sitka_2021.png')
