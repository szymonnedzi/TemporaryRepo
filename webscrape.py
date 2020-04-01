MENU_PROMPT = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit: "
movies = []

def inputMovie():
    title = input("Enter the movie title: ")
    director = input("Enter the movie director: ")
    year = input("Enter the movie release year: ")
    movies.append({
        'director': director,
        'title': title,
        'year': year
    })


selection = input(MENU_PROMPT)
while selection != 'q':
    if selection == "a":
        inputMovie()
    elif selection == "l":
        for movie in movies:
            print(movie)
    elif selection == "f":
        findTitle = input("What movie are you looking for?")
        for movie in movies:
            if movie['title'] == findTitle:
                print("Yeah, it's here")
    else:
        print('Unknown command. Please try again.')

    selection = input(MENU_PROMPT)