import requests
import sys
command = sys.argv
movie_name = command[2:]

response = requests.get(f'http://omdbapi.com//?t={movie_name}&apikey=5b4e033c')

if len(command)>1:
    try:
        response_json = response.json()
        print('Title: ', response_json["Title"])
        print('Year: ', response_json["Year"])
        print('Released: ', response_json["Released"])
        print('Genre: ', response_json["Genre"])
        print('Director: ', response_json["Director"])
    except:
        print('The movie has not been found!')