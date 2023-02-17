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

FIRST_FILM_URL = "https://swapi.dev/api//people/"


def write_data_into_file(data: Dict) -> None:
    """writes dict data into a file"""

    with open("output_people.txt", "w") as fp:
        fp.write(json.dumps(data))


def first_task() -> Dict:
    """Returns a dict object from swapi.dev/api/people/"""

    response = requests.get(FIRST_FILM_URL)
    result_ = response.json()
    write_data_into_file(result_)
    return result_

def second_task(data_: Dict) -> List:
    """pull data from swapi people sequentially"""

    peoples = data_.get("peoples")  # returns None by default

    name = []
    for people in peoples:
        people_data = hit_url(people)
        people_data = people_data.json()
        name.append(people_data.get("name"))

    return name


if __name__ == "__main__":
    # first task
    first_result = first_task()
    pprint(first_result)

    # second task : capture people
    second_result = second_task(first_task)
    pprint(second_result)
