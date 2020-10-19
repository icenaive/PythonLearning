import csv

from matplotlib import pyplot as plt
from datetime import datetime

filename = './data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, column_header in enumerate(header_row):
        print(index, column_header)

    dates, hights, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        dates.append(current_date)
        hights.append(int(row[5]))
        lows.append(int(row[6]))

    fig = plt.figure(dpi=128, figsize=(10, 6))
    plt.plot(dates, hights, c='red', alpha=0.5)
    plt.plot(dates, lows, c='blue', alpha=0.5)
    plt.fill_between(dates, hights, lows, facecolor='blue', alpha=0.1)

    # plt.title("Daily high temperatures, July 2014", fontsize=24)
    plt.title("Daily high and low temperatures - 2014", fontsize=24)
    plt.xlabel("", fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()
