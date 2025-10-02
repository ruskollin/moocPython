# Write your solution here
def find_movies(database: list, search_term: str):
    keyword= search_term.lower()
    result = []
    for movie in database:
        if keyword in movie["name"].lower():
            result.append(movie)
    
    return result