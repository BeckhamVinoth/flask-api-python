from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('tutorial.html')


@app.route('/api/v1/<station>/<date>')
def about(station, date):
    temp = 20
    return {"station": station, "date": date, "temp": temp}


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
