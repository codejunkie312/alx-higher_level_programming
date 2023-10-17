#!/usr/bin/python3
""" A module that includes Base class """
import json
import csv
import turtle


class Base:
    """ Base class."""
    __nb_objects = 0

    def __init__(self, id=None):
        """This function instantiates Base instances.

        Args:
            id (int): is an integer.
        """
        if id is not None:
            if not isinstance(id, int):
                raise TypeError
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """This function returns the JSON string representation of
        list_dictionaries.

        Args:
            list_dictionaries (list): is a list of dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """This function returns the list of the JSON string
        representation json_string.

        Args:
            json_string (str): is a string representing a list of
            dictionaries.
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """This function writes the JSON string representation of
        list_objs to a file.

        Args:
            cls: is a class.
            list_objs (list): is a list of instances.
        """
        filename = cls.__name__ + ".json"
        new_list = []
        if list_objs is not None:
            for obj in list_objs:
                new_list.append(obj.to_dictionary())
        with open(filename, "w") as f:
            f.write(cls.to_json_string(new_list))

    @classmethod
    def create(cls, **dictionary):
        """This function returns an instance with all attributes already set.

        Args:
            cls: is a class.
            dictionary (dict): is a double pointer to a dictionary.
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """This function returns a list of instances."""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as f:
                list_dict = cls.from_json_string(f.read())
            list_inst = []
            for dict in list_dict:
                list_inst.append(cls.create(**dict))
            return list_inst
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """This function writes the CSV string representation of
        list_objs to a file.

        Args:
            cls: is a class.
            list_objs (list): is a list of instances.
        """
        filename = cls.__name__ + ".csv"
        new_list = []
        if list_objs is not None:
            for obj in list_objs:
                new_list.append(obj.to_dictionary())
        with open(filename, "w") as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow(new_list[0].keys())
            csv_writer.writerows([d.values() for d in new_list])

    @classmethod
    def load_from_file_csv(cls):
        """This function returns a list of instances."""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r") as f:
                reader = csv.reader(f)
                header = next(reader)
                instances = []
                for row in reader:
                    instance = {}
                    for i in range(len(header)):
                        instance[header[i]] = int(row[i])
                    instance = cls.create(**instance)
                    instances.append(instance)
                return instances
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """This function draws rectangles and squares using the turtle module.

        Args:
            list_rectangles (list): is a list of Rectangle instances.
            list_squares (list): is a list of Square instances.
        """
        turtle.title("Ninja Turtle")
        turtle.setup(800, 600)
        turtle.shape("turtle")
        turtle.bgcolor("white")
        turtle.color("red")
        turtle.speed(10)
        turtle.penup()
        for rect in list_rectangles:
            turtle.goto(rect.x, rect.y)
            turtle.pendown()
            for i in range(2):
                turtle.forward(rect.width)
                turtle.left(90)
                turtle.forward(rect.height)
                turtle.left(90)
            turtle.penup()
        for square in list_squares:
            turtle.goto(square.x, square.y)
            turtle.pendown()
            for i in range(4):
                turtle.forward(square.width)
                turtle.left(90)
            turtle.penup()
        turtle.exitonclick()
