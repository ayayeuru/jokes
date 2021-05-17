def try_me():
    import requests
    response = requests.get("https://official-joke-api.appspot.com/jokes/ten")
    return print("Random joke : ",response.json()[0]["setup"],response.json()[0]["punchline"])