from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String
from flask_sqlalchemy import SQLAlchemy
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

# === CONFIGURARE SQLALCHEMY BASE ===
class Base(DeclarativeBase):
    pass

# === INSTANTIEREA APLICATIEI FLASK ===
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies-database.db"
app.config['SECRET_KEY'] = 'super-secret-key-123'  # 

# === INITIALIZARE DATABASE ===
db = SQLAlchemy(model_class=Base)
db.init_app(app)

class Movie(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(30) , nullable=False)
    year: Mapped[int] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(String(100), nullable=False)
    rating: Mapped[float] = mapped_column(nullable=False)
    ranking: Mapped[int] = mapped_column(nullable=False)
    review: Mapped[str] = mapped_column(String(20), nullable=False)
    img_url: Mapped[str] = mapped_column(String(100),nullable=False)

@app.route("/")
def home():
    all_movies = Movie.query.order_by(Movie.rating.desc()).all()
    db.session.commit()
    update_rankings()
    return render_template("index.html" , all_movies=all_movies)

@app.route("/edit/<int:id>" , methods=["GET", "POST"])
def edit(id):
    movie_to_edit = db.session.get(Movie , id)
    if request.method == "POST":
        new_rating = request.form["new_rating"]
        new_review = request.form["new_review"]
        movie_to_edit.rating = new_rating
        movie_to_edit.review = new_review
        update_rankings()
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", movie=movie_to_edit)

def update_rankings():
    all_movies = Movie.query.order_by(Movie.rating.desc()).all()
    for index, movie in enumerate(all_movies):
        movie.ranking = index + 1
    db.session.commit()

@app.route("/delete/<int:id>" , methods = ["GET" , "POST"])
def delete(id):
    movie_to_delete = db.session.get(Movie, id)
    if movie_to_delete:
        db.session.delete(movie_to_delete)
        db.session.commit()
        update_rankings()
    return redirect(url_for('home'))

#API PART

API_KEY = "86cf41a1cf72cdd3af00ce3e08833345"



@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        movie_searcher = request.form["movie-searcher"]
        url = f"https://api.themoviedb.org/3/search/movie?query={movie_searcher}&api_key={API_KEY}"
        response = requests.get(url)
        data = response.json()
        update_rankings()
        return render_template("movie_list.html" , data=data["results"])
    
    return render_template("add.html")

@app.route("/added" , methods=["GET" , "POST"])
def added():
    movie_id = request.args.get("movie_id")
    movie_url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}"
    response = requests.get(movie_url)
    movie = response.json()
    poster_path = f"https://api.themoviedb.org/3/movie/{movie_id}/images"

    new_movie = Movie(
        title = movie["original_title"] ,
        year = movie["release_date"] ,
        description = movie["overview"] ,
        rating = 0.0 ,
        ranking = 10 ,
        review = "None" ,
        img_url = f"https://image.tmdb.org/t/p/w500{movie['poster_path']}" ,
    )
    db.session.add(new_movie)
    db.session.commit()
    update_rankings()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
    with app.app_context():
        db.create_all()









