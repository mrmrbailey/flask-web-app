from flask import Flask
from flask import request, render_template

import temperature_converter

app = Flask(__name__)

@app.route("/")
def index():
    print('Request for index page received')
    return render_template('index.html')

@app.route("/convert", methods=['POST'])
def convert():

    celsius = request.form.get('celsius')
    fahrenheit = temperature_converter.fahrenheit_from(celsius)

    print('Request for convert page received with celsius=%s' % celsius)
    return render_template('converter.html', fahrenheit=fahrenheit)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)