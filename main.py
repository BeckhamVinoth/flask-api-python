from flask import Flask, render_template
import pandas as pd


app = Flask(__name__)
station_details = pd.read_csv("data_small/stations.txt", skiprows=17)
station_details = station_details[['STAID', 'STANAME                                 ']]


@app.route('/')
def home():
    return render_template('home.html', data=station_details.to_html())


@app.route('/api/v1/<station>/<date>')
def about(station, date):
    try:
        file_name = "data_small/TG_STAID"+str(station).zfill(6)+".txt"
        df = pd.read_csv(file_name, skiprows=20, parse_dates=["    DATE"])
        temp = df.loc[df['    DATE'] == date]['   TG'].squeeze() / 10
        return {"station": station, "date": date, "temp": temp}
    except FileNotFoundError:
        return str("404: Data not found")


@app.route('/api/v1/<station>')
def get_station_details(station):
    try:
        file_name = "data_small/TG_STAID"+str(station).zfill(6)+".txt"
        df = pd.read_csv(file_name, skiprows=20, parse_dates=["    DATE"])
        result = df.to_dict(orient='records')
        return result
    except FileNotFoundError:
        return str("404: Station not found")


@app.route('/api/v1/year/<station>/<year>')
def get_year_details(station, year):
    try:
        file_name = "data_small/TG_STAID"+str(station).zfill(6)+".txt"
        df = pd.read_csv(file_name, skiprows=20, parse_dates=["    DATE"])
        df['year'] = df['    DATE'].dt.year
        year_data = df[df['year'] == int(year)]
        year_data.drop(columns=['year'], inplace=True)
        result = year_data.to_dict(orient='records')
        return result
    except FileNotFoundError:
        return str("404: Year records not found")


if __name__ == '__main__':
    app.run(debug=True)
