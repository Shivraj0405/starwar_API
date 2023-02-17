"""
The task 2 goes like following:
Pull data for the the first movie in star wars
Write the json data into a file named output.txt


SUBTASKS -
1. Output should be only list of names (first name & last name) of characters
in the movie.
2. Output should only print list of planet names used in the movie
3. Output should only print list of vehicle names used in the movie.
"""

import json
import requests

from pprint import pprint
from typing import Dict, List

from utils.fetch_data import hit_url, fetch_data

FIRST_FILM_URL = "https://swapi.dev/api/vehicles/"


def write_data_into_file(data: Dict) -> None:
    """writes dict data into a file"""

    with open("output_vehicle.txt", "w") as fp:
        fp.write(json.dumps(data))


def first_task() -> Dict:
    """Returns a dict object from swapi.dev/api/vehicle/"""

    response = requests.get(FIRST_FILM_URL)
    result_ = response.json()
    write_data_into_file(result_)
    return result_

def fourth_task(data_: Dict) -> List:
    """pull data from swapi vehicle sequentially"""

    vehicles = data_.get("vehicle")  # returns None by default

    names2 = []
    for vehicle in vehicles:
        planet_data = hit_url(vehicle)
        planet_data = planet_data.json()
        names2.append(planet_data.get("name"))

    return names2


if __name__ == "__main__":
    # first task
    first_result = first_task()
    pprint(first_result)

    # fourth task : capture vehicle
    fourth_result = fourth_task(first_task)
    pprint(fourth_result)
