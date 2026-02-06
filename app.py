from flask import Flask
from flask import request, render_template

import temperature_converter

app = Flask(__name__)

@app.route("/")
def index():
    print('Request for index page received')
    return render_template('index.html')

@app.route("/fahrenheit_from", methods=['POST'])
def convert_from_celsius():

    celsius = request.form.get('celsius')
    fahrenheit = temperature_converter.fahrenheit_from(celsius)

    print('Request for convert page received with celsius=%s' % celsius)
    return render_template('converter.html', celsius=celsius, fahrenheit=fahrenheit)

@app.route("/celsius_from", methods=['POST'])
def convert_from_fahrenheit():

    fahrenheit = request.form.get('fahrenheit')
    celsius = temperature_converter.celsius_from(fahrenheit)

    print('Request for convert page received with celsius=%s' % celsius)
    return render_template('converter.html', celsius=celsius, fahrenheit=fahrenheit)