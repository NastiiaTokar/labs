from enum import Enum
from datetime import date
from typing import List


class MovieType(Enum):
    ACTION = "Action"
    COMEDY = "Comedy"
    DRAMA = "Drama"
    FANTASY = "Fantasy"
    HORROR = "Horror"
    CRIME = "Crime"

class DayOfWeek(Enum):
    Monday = 50
    Tuesday = 40
    Wednesday = 70
    Thursday = 60
    Friday = 80
    Saturday = 200
    Sunday = 200
class Movie:
    def __init__(self, id: int, title: str, ranking: float, release_date: date,
                 character_number: int, ticket_price: float, comment: str, genre: MovieType, license_price: int):
        self.id = id
        self.title = title
        self.ranking = ranking
        self.release_date = release_date
        self.character_number = character_number
        self.ticket_price = ticket_price
        self.comment = comment
        self.genre = genre
        self.license_price = license_price

    def __del__(self):
        print(f"Movie '{self.title}' видалено")

    def display_info(self):
        print(f"ID: {self.id}, Назва: {self.title}, Рейтинг: {self.ranking}, "
              f"Дата випуску: {self.release_date}, Кількість героїв: {self.character_number}, "
              f"Ціна квитка: {self.ticket_price}, Коментар: {self.comment}, Жанр: {self.genre.value}, Ціна Ліцензії: {self.license_price}")

class Cinema:
    def __init__(self, name: str, location: str, movies: List[Movie]):
        self.name = name
        self.location = location
        self.movies = movies

    def __del__(self):
        print(f"Cinema '{self.name}' видалено")

    def display_movies(self):
        for movie in self.movies:
            movie.display_info()

    def calculate_profit(self, movie: Movie, day: DayOfWeek, viewers: int):
       
        day_multiplier = {
            DayOfWeek.Monday: 0.9,     
            DayOfWeek.Tuesday: 0.9,
            DayOfWeek.Wednesday: 0.95,
            DayOfWeek.Thursday: 1.0,   
            DayOfWeek.Friday: 1.1,     
            DayOfWeek.Saturday: 1.2,
            DayOfWeek.Sunday: 1.2
        }
        ticket_price = movie.ticket_price * day_multiplier[day]
        profit = ticket_price * viewers
        print(f"Прибуток від фільму '{movie.title}' при {viewers} глядачах у день '{day.name}' (ціна квитка {ticket_price}): {profit}")
        return profit

    def find_movie(self, genre: MovieType = None, min_ranking: float = 0.0):
        found_movies = [movie for movie in self.movies if (not genre or movie.genre == genre) and movie.ranking >= min_ranking]
        return found_movies

    def sort_movies_by_release_date(self):
        self.movies.sort(key=lambda movie: movie.release_date)
        print("Фільми відсортовано за датою випуску.")

    def calculate_total_license_cost(self, genre: MovieType):
        total_license_cost = 0
        for movie in self.movies:
            if movie.genre == genre:
                total_license_cost += movie.license_price
        print(f"Загальна вартість ліцензій для жанру '{genre.value}': {total_license_cost}")
        return total_license_cost

    def calculate_total_profit_for_genre(self, genre: MovieType, day: DayOfWeek, viewers_per_day: int = None):
        total_profit = 0
        viewers = viewers_per_day if viewers_per_day is not None else day.value
        for movie in self.movies:
            if movie.genre == genre:
                total_profit += self.calculate_profit(movie, day, viewers)
        print(f"Загальний прибуток для жанру '{genre.value}' у день '{day.name}' з {viewers} глядачами: {total_profit}")
        return total_profit



    def check_profit_vs_license_cost(self, genre: MovieType, day: DayOfWeek, viewers_per_day: int = None):
        total_license_cost = self.calculate_total_license_cost(genre)
        total_profit = self.calculate_total_profit_for_genre(genre, day, viewers_per_day)
        
        if total_license_cost > total_profit:
            print(f"Загальна вартість ліцензій для жанру '{genre.value}' ({total_license_cost}) перевищує отриманий прибуток ({total_profit}).")
        else:
            print(f"Прибуток ({total_profit}) перевищує загальну вартість ліцензій для жанру '{genre.value}' ({total_license_cost}).")



if __name__ == "__main__":
   
    movie1 = Movie(1, "Inception", 8.8, date(2010, 7, 16), 10, 15.0, "Mind-bending thriller", MovieType.ACTION, 50000)
    movie2 = Movie(2, "The Matrix", 8.7, date(1999, 3, 31), 8, 12.0, "Sci-fi classic", MovieType.ACTION, 300)
    movie3 = Movie(3, "The Grand Budapest Hotel", 8.1, date(2014, 3, 28), 12, 10.0, "Charming comedy", MovieType.COMEDY, 700)

    
    cinema = Cinema("Cinema City", "Kyiv", [movie1, movie2, movie3])

    
    print("Фільми в кінотеатрі:")
    cinema.display_movies()

    
    cinema.calculate_profit(movie1, DayOfWeek.Monday, 5)

   
    print("\nФільми жанру 'Action' з рейтингом вище 8.5:")
    found_movies = cinema.find_movie(MovieType.ACTION, 8.5)
    for movie in found_movies:
        movie.display_info()

    
    cinema.sort_movies_by_release_date()
    print("\nВідсортовані фільми:")
    cinema.display_movies()
    cinema.calculate_total_license_cost(MovieType.ACTION)
    cinema.calculate_total_profit_for_genre(MovieType.ACTION, DayOfWeek.Monday, viewers_per_day=100)
    
    cinema.check_profit_vs_license_cost(MovieType.ACTION,DayOfWeek.Monday)