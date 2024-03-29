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
        print(file_name)
        df = pd.read_csv(file_name, skiprows=20, parse_dates=["    DATE"])
        temp = df.loc[df['    DATE'] == date]['   TG'].squeeze() / 10
        return {"station": station, "date": date, "temp": temp}
    except FileNotFoundError:
        return str("404: File not found")


# @app.route('/about/')
# def about():
#     return render_template('about.html')
#
#
# @app.route('/contact-us/')
# def contact_us():
#     return render_template('contact-us.html')
#
#
# @app.route('/store/')
# def store():
#     return render_template('store.html')


if __name__ == '__main__':
    app.run(debug=True)
