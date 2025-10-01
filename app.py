# 1. შექმენით flask-ის პროექტი(სტრუქტურა უნდა იყოს დაცული)
from flask import render_template, Flask
from models import movies, headings
app = Flask(__name__)

@app.route('/')
def index():
    count_movies = len(movies)
    avg_duration = sum(movie['duration'] for movie in movies) / len(movies)
    return render_template('index.html', headings=headings, movies=movies, all_movies=count_movies, count_movies=count_movies, avg_duration=avg_duration)

if __name__ == '__main__':
    app.run(debug=True)

