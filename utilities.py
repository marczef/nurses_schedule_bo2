from dataclasses import dataclass
import numpy as np
import random
import pandas as pd
from calendar import monthcalendar

class Data:

    def __init__(self, number_of_nurses_, number_of_rooms_):
        self.number_of_room = number_of_rooms_
        self.number_of_nurses = number_of_nurses_
        self.next_id_nurse = 0
        self.next_id_room = 0
        self.nurses = []
        self.rooms = []

        for i in range(self.number_of_nurses):
            self.add_nurse()
        for i in range(self.number_of_room):
            self.add_room()

    def add_nurse(self, part_time = False):
        self.nurses.append(Nurse(self.next_id_nurse, part_time))
        self.next_id_nurse += 1

    def add_room(self):
        self.rooms.append(Room(self.next_id_room))
        self.next_id_room += 1

    def print_nurses(self):
        for i in self.nurses:
            if not i.part_time:
                print("Nurse: ", i.id, ", status: ", i.status, ", worked hours: ", i.number_of_hours)
            else:
                print("Nurse: ", i.id, ", status: ", i.status, ", worked hours: ", i.number_of_hours, ", part-time")

    def print_room(self):
        for i in self.rooms:
            print("Room: ", i.id, ", priority: ", i.priority)

class Nurse:

    def __init__(self, next_id, part_time = False):
        self.status = random.randint(1,5)
        self.id = next_id
        self.number_of_hours = 0

        #Part-time job (children, pregnancy, etc.).
        self.part_time = part_time

class Daily:
    """Klasa przechowująca dzienny grafik pielęgniarek"""
    def __init__(self, data, day):
        self.day = day
        self.nurses = data.nurses
        self.rooms = data.rooms
        self.daily = np.ndarray(shape=(len(self.rooms), 4), dtype = object)

    #losowe rozwiązanie
    def random_solution(self):
        for i in range(self.daily.shape[0]):
            for j in range(self.daily.shape[1]):
                self.daily[i][j] = random.choice(self.nurses).id

   #wyświetlenie
    def print_random_day(self):
        self.random_solution()
        daily = pd.DataFrame(self.daily,
                                   columns=["Day shift (1)", "Day shift (2)", "Night shift (1)", "Night shift (2)"],)
        print("Day ", self.day, ": ", daily)


class Weekly:
    def __init__(self, data):
        self.nurses = data.nurses
        self.rooms = data.rooms
        self.weekly = pd.DataFrame(Daily(data),
                                   columns = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
                                   index = [0])

class Solution:
    """Klasa generująca rozwiązanie miesięczne"""
    def __init__(self, data, month):
        self.month = month
        # self.weekly = Weekly(data)

        #Działamy na dniach z kalendarza
        self.solution = np.array(monthcalendar(2022, month), dtype = object)

        #Każdy dzień z kalendarza jest klasą Daily
        for i in range(self.solution.shape[0]):
            for j in range(self.solution.shape[1]):
                if self.solution[i][j] != 0:
                    self.solution[i][j] = Daily(data, self.solution[i][j])

    def print_solution(self):
        days = np.array(monthcalendar(2020, 1), dtype = object)
        solution = pd.DataFrame(days,
                                  columns=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])
        print(solution)
        for i in range(self.solution.shape[0]):
            for j in range(self.solution.shape[1]):
                if self.solution[i][j] != 0:
                    self.solution[i][j].print_random_day()


class Room:
    def __init__(self, next_id):
        self.priority = random.randint(1,2)
        self.id = next_id

        if self.priority == 1:
            self.needed_number_of_nurses = 1
        else:
            self.needed_number_of_nurses = 2
