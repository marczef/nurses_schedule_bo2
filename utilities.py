from dataclasses import dataclass
import numpy as np
import random
from math import inf


class Data:

    def __init__(self, number_of_nurses_, number_of_rooms_):
        self.number_of_rooms = number_of_rooms_
        self.number_of_nurses = number_of_nurses_
        self.next_id_nurse = 0
        self.next_id_room = 0
        self.nurses = []
        self.rooms = []

        for i in range(self.number_of_nurses):
            self.add_nurse()
        for i in range(self.number_of_rooms):
            self.add_room()

    def add_nurse(self):
        self.nurses.append(Nurse(self.next_id_nurse))
        self.next_id_nurse += 1

    def add_room(self):
        self.rooms.append(Room(self.next_id_room))
        self.next_id_room += 1

    def print_nurses(self):
        for i in self.nurses:
            print("Nurse: ", i.id, ", status: ", i.status, ", worked hours: ", i.number_of_hours)

    def print_room(self):
        for i in self.rooms:
            print("Room: ", i.id, ", priority: ", i.priority)

class Nurse:

    def __init__(self, next_id):
        self.status = random.randint(1,5)
        self.id = next_id
        self.number_of_hours = 0

class Solution:
    def __init__(self, number_of_nurses_, number_of_rooms_):
        self.number_of_rooms = number_of_rooms_
        self.number_of_nurses = number_of_nurses_
        self.data = Data(self.number_of_nurses, self.number_of_rooms)
        self.solution = np.ndarray(shape=(4*7, self.data.number_of_rooms,3), dtype=float)
        self.data.nurses.sort(key=lambda x: 0 if (x.status < 3) else 1)
        self.value = 0

        for i in range(self.solution.shape[1]):
            for j in range(self.solution.shape[0]):
                for nr in range(0,2):
                    self.solution[j][i][nr] = inf

        self.two_week()

        self.data.print_nurses()
        self.data.print_room()

        self.correction()

    def value_of_solution(self):
        overall_hours = self.solution.shape[0]*6*self.data.number_of_rooms/self.data.number_of_nurses
        sum = 0
        for i in self.data.nurses:
            sum += (overall_hours - i.number_of_hours)**2
        self.value = np.sqrt(sum / self.data.number_of_nurses)

        return self.value

    def first_solution(self, shift, before_before=[]):
        before = []
        #To jest po to aby nie dodawało nam bez przerwy tych samych pielęgniarek
        if shift%2 == 0:
            random.shuffle(self.data.nurses)
            self.data.nurses.sort(key=lambda x: 0 if (x.status < 3) else 1)
        for i in [nurse for nurse in self.data.nurses if nurse.id not in before_before]:
            for j in self.data.rooms:
                if j.priority == 2 and i.status >= 3 and \
                        self.solution[shift][j.id][0] == inf and self.solution[shift][j.id][1] == inf:
                    self.solution[shift][j.id][0] = i.id
                    i.number_of_hours += 6
                    before.append(i.id)
                    break
                elif j.priority == 2 and i.status >= 3 and self.solution[shift][j.id][0] != inf \
                        and self.solution[shift][j.id][1] == inf:
                    self.solution[shift][j.id][1] = i.id
                    i.number_of_hours += 6
                    before.append(i.id)
                    break
                elif j.priority == 1 and self.solution[shift][j.id][0] == inf:
                    self.solution[shift][j.id][0] = i.id
                    self.solution[shift][j.id][1] = -1
                    i.number_of_hours += 6
                    before.append(i.id)
                    break
        return before



    def min_max_hours(self):

        nurses_hours1 = [nurse.number_of_hours for nurse in self.data.nurses]

        min_hours1 = min(nurses_hours1)
        min_hours_nurse1 = self.data.nurses[nurses_hours1.index(min_hours1)]
        max_hours1 = max(nurses_hours1)
        max_hours_nurse1 = self.data.nurses[nurses_hours1.index(max_hours1)]


        return min_hours_nurse1, max_hours_nurse1

#NIE WKLEJAMY PIELĘGNIAREK W MIEJSCE INF W CELU POPRAWY - NIE JEST TO MOŻLIWE, NALEŻY DODAĆ WYSTARCZAJĄCĄ ILOŚĆ PIELĘGNIAREK


    def nurses_swap(self, nurse_min, nurse_max):
        flag = 0
        i1 = 0
        j1 = 0
        for i in range(self.solution.shape[0]):
            for j in self.data.rooms:
                if nurse_min.id in self.solution[i][j.id]:
                    break
                if self.solution[i][j.id][0] == nurse_max.id:
                    flag = 1
                    self.solution[i][j.id][0] = nurse_min.id
                    self.solution[i+1][j.id][0] = nurse_min.id
                    self.data.nurses[nurse_min.id].number_of_hours += 12
                    self.data.nurses[nurse_max.id].number_of_hours -= 12
                    i1 = i
                    j1 = j
                    break
                if self.solution[i][j.id][1] == nurse_max.id:
                    flag = 1
                    self.solution[i][j.id][1] = nurse_min.id
                    self.solution[i+1][j.id][1] = nurse_min.id
                    self.data.nurses[nurse_min.id].number_of_hours += 12
                    self.data.nurses[nurse_max.id].number_of_hours -= 12
                    i1 = i
                    j1 = j
                    break
            if flag:
                break
        return i1, j1


    def correction(self):
        self.write_schedule()
        tabu_list = []
        value_of_solution = self.value_of_solution()
        print(value_of_solution)
        min_hours_nurse1, max_hours_nurse1 = self.min_max_hours()
        i1, j1 = self.nurses_swap(min_hours_nurse1, max_hours_nurse1)
        tabu_list.append([i1, j1.id])
        while 1:
            i1_old, j1_old = i1, j1
            tabu_list.remove([i1_old, j1_old.id])
            value_of_solution_before = self.value_of_solution()
            min_hours_nurse1, max_hours_nurse1 = self.min_max_hours()
            i1, j1 = self.nurses_swap(min_hours_nurse1, max_hours_nurse1)

            if [i1, j1.id] in tabu_list:
                print("Ruch zakazany")

            value_of_solution_after = self.value_of_solution()

            print(value_of_solution_after)

            tabu_list.append([i1, j1.id])
            if value_of_solution_after >= value_of_solution_before:
                break
            else:
                tabu_list.append([i1, j1.id])


        value_of_solution = self.value_of_solution()

        self.data.print_nurses()



    def two_week(self):
        self.first_solution(0)
        before_before = self.first_solution(1)
        for i in range(2, 28, 2):
            self.first_solution(i, before_before)
            before_before = self.first_solution(i+1, before_before)
        self.data.nurses.sort(key=lambda x: x.id)


    def write_schedule(self):
        for i in range(self.solution.shape[1]):
            for j in range(self.solution.shape[0]):
                print("[", end="")
                for nr in range(0,2):
                    if nr == 0:
                        print(self.solution[j][i][nr]," ", end="")
                    else:
                        print(self.solution[j][i][nr], end="")
                print("]", end="")
            print("")

class Room:
    def __init__(self, next_id):
        self.priority = random.randint(1,2)
        self.id = next_id

        if self.priority == 1:
            self.needed_number_of_nurses = 1
        else:
            self.needed_number_of_nurses = 2