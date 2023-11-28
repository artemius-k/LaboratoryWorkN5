import numpy
import pandas


def pandas_ex():
    data = pandas.read_csv("test.csv", sep=",", nrows=1000)

    data = data.fillna({"Id": 0, "DistrictId": 0, "Rooms": 0., "Square": 0., "LifeSquare": 0., "KitchenSquare": 0.,
                        "Floor": 0, "HouseFloor": 0., "HouseYear": 0, "Ecology_1": 0., "Ecology_2": "Unspecified",
                        "Ecology_3": "Unspecified", "Social_1": 0, "Social_2": 0, "Social_3": 0, "Healthcare_1": 0.,
                        "Healthcare_2": 0, "Shops_1": 0, "Shops_2": "Unspecified"})


