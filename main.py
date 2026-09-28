movies=[
    {
        "name":"Inception",
        "genre":"Sci-Fi",
        "language":"English",
        "rating":8.8,
        "year":2010
    },

    {
        "name":"The Dark Knight",
        "genre":"Action",
        "language":"English",
        "rating":9.0,
        "year":2008 
    },

    {
        "name":"Interstellar",
        "genre":"Sci-Fi",
        "language":"English",
        "rating":8.6,
        "year":2014
    },

    {
        "name":"3 Idiots",
        "genre":"Comedy",
        "language":"Hindi",
        "rating":8.4,
        "year":2009
    },

    {
        "name":"Dangal",
        "genre":"Sports",
        "language":"Hindi",
        "rating":8.4,
        "year":2016
    },

    {
        "name":"Ok Jaanu",
        "genre":"Romance",
        "language":"Hindi",
        "rating":6.5,
        "year":2017  
    }
]

print(movies)


def view_movies():
    print("\n===========MOVIE LIST===========")

    for i, movie in enumerate (movies, start=1):
        print(f"\n{i}. {movie['name']}")
        print(f" Genre:{movie['genre']}")
        print(f" Language:{movie['language']}")
        print(f" Rating:{movie['rating']}")
        print(f" Year:{movie['year']}")
        print("\n===============================")

view_movies()

def search_movie():
    search=input("Enter movie name:").lower()

    found=False

    for movie in movies:
        if search in movie ["name"].lower():
            print("\nMovie Found!")
            print(f"Name:{movie['name']}")
            print(f"Genre:{movie['genre']}")
            print(f"Language:{movie['language']}")
            print(f"Rating:{movie['rating']}")
            print(f"year:{movie['year']}")

            found=True

        if not found:
            print("Movie not found!")


def recommend_movies():
    genre=input("Enter your preferred genre:").lower()
    language=input("Enter your preferred landguage:").lower()
    found=False

    print("\n============Recommended Movies============")

    for movie in movies:
        if genre==movie["genre"].lower() and language==movie["language"].lower():
            print(f"\nMovie:{movie['name']}")
            print(f"Genre:{movie['genre']}")
            print(f"Rating:{movie['rating']}")
            print(f"year:{movie['year']}")

            found=True

        if not found:
            print("No movies found matching your preferrences.")

while True:
    print("\n===========MOVIE RECOMMENDATION SYSTEM===========")
    print("1. View Movies")
    print("2. Search Movie")
    print("3. Get Recommendation")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice=="1":
        view_movies()

    elif choice=="2":
        search_movie()

    elif choice=="3":
        recommend_movies()

    elif choice=="4":
        print("Exiting the program...")
        break

    else:
        print("invalid choice! Please try again.")



