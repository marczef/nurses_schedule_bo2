from dataclasses import dataclass
import numpy as np
import random
from math import inf
import math
import copy



class Data:

    def __init__(self, number_of_nurses_, number_of_rooms_, percent_higher_status_):
        self.number_of_rooms = number_of_rooms_
        self.number_of_nurses = number_of_nurses_
        self.percent_higher_status = percent_higher_status_
        self.next_id_nurse = 0
        self.next_id_room = 0
        self.nurses = []
        self.rooms = []
        self.wage = random.randint(20, 25)

        number_of_nurses_with_lower_status = self.number_of_nurses - math.ceil((self.number_of_nurses * self.percent_higher_status) / 100)

        flag = -1

        for i in range(self.number_of_nurses):
            if i < number_of_nurses_with_lower_status:
                status = random.randint(1, 2)
                self.add_nurse(status)
            else:
                status = random.randint(3, 5)
                self.add_nurse(status)
        for i in range(self.number_of_rooms):
            flag = flag * (-1)
            self.add_room(flag)

    def add_nurse(self, status):
        self.nurses.append(Nurse(self.next_id_nurse, status))
        self.next_id_nurse += 1

    def add_room(self, flag):
        self.rooms.append(Room(self.next_id_room, flag))
        self.next_id_room += 1

    def print_nurses(self):
        nurses = ""
        for i in self.nurses:
            nurses += "Nurse: " + str(i.id) + ", status: " + str(i.status) + ", worked hours: " + str(i.number_of_hours) + ', salary: ' +  str(i.salary) + "\n"
        return nurses

    def print_room(self):
        rooms = ""
        for i in self.rooms:
            rooms += "Room: " + str(i.id) + ", priority: " + str(i.priority)  + "\n"
        return rooms

class Nurse:

    def __init__(self, next_id, status_):
        self.status = status_
        self.id = next_id
        self.number_of_hours = 0
        self.salary = 0



class Room:
    def __init__(self, next_id, flag):
        # co drugi pokój ma priorytet 1, a co drugi 2
        if flag == 1:
            self.priority = 1
        else:
            self.priority = 2

        self.id = next_id

        if self.priority == 1:
            self.needed_number_of_nurses = 1
        else:
            self.needed_number_of_nurses = 2