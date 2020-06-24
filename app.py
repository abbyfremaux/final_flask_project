import requests
from flask import Flask, render_template, jsonify, request
from creds.keys import OMDB_API_KEY

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/JSON')
def json_endpoint():
    return jsonify(render_template('json_endpoint.html'))


@app.route('/HTML')
def html_endpoint():
    return render_template('html_endpoint.html')


@app.route('/API')
def api_endpoint():
    return render_template('api_endpoint.html')


@app.route('/API/movie_search', methods=["POST"])
def movie_search():
    movie_title = request.form["movieTitle"]
    title_query = f"{movie_title.replace(' ', '+')}"

    year_query = ""
    release_year = request.form["releaseYear"]
    if release_year != "":
        year_query = f"&y={release_year}"

    synopsis_length_query = ""
    synopsis_length = request.form["movieSynopsisLength"]
    if synopsis_length == "Long":
        synopsis_length_query = f"&plot=full"

    api_query = f"http://www.omdbapi.com/?apikey={OMDB_API_KEY}&t={title_query}{year_query}{synopsis_length_query}"

    return requests.get(api_query).text


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
