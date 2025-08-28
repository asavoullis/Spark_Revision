import requests


def get_random_joke():
    url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(url)
    if response.status_code == 200:
        joke = response.json().get("value")
        return joke
    else:
        return "Sorry, couldn't fetch a joke."


def get_categories():
    url = "https://api.chucknorris.io/jokes/categories"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return []


def get_joke_by_category(category):
    url = f"https://api.chucknorris.io/jokes/random?category={category}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get("value")
    else:
        return "Sorry, couldn't fetch a joke from this category."


def search_jokes(query):
    url = f"https://api.chucknorris.io/jokes/search?query={query}"
    response = requests.get(url)
    if response.status_code == 200:
        jokes = response.json().get("result")
        return [joke["value"] for joke in jokes]
    else:
        return []


# Example usage
if __name__ == "__main__":
    print("Random Joke:")
    print(get_random_joke())

    print("\nCategories:")
    categories = get_categories()
    print(categories)

    if categories:
        print(f"\nRandom Joke from 'dev' category:")
        print(get_joke_by_category("dev"))

    print("\nSearch Jokes with 'Robert Oppenheimer':")
    print(search_jokes("Robert Oppenheimer"))
