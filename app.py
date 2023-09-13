from flask import Flask
import os, client_data_collector

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Use /cdc to use the application. See the readme for more details.</p>"

@app.route("/cdc/<file1>/<file2>/<countries>")
def cdc(file1, file2, countries):
    formatted_countries = countries.replace("_", " ").split(",")
    client_data_collector.write_file(file1, file2, formatted_countries, '')
    return f"Creating file from {file1} and {file2} using the following countries: {formatted_countries}. Target directory: {os.curdir}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8000')