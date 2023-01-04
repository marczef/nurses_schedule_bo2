#!/usr/bin/python
# -*- coding: utf-8 -
import numpy as np

from utilities import *
from calendar import monthrange
import matplotlib.pyplot as plt



def is_night_shift(shift):
    return shift % 4 == 2 or shift % 4 == 3


def is_day_shift(shift):
    return shift % 4 == 1 or shift % 4 == 0


class Solution:
    def __init__(self, year_, month_, number_of_nurses_, number_of_rooms_):
        self.number_of_rooms = number_of_rooms_
        self.number_of_nurses = number_of_nurses_
        self.month = month_
        self.year = year_
        # first_day_of_month mówi, jaki dzień tygodnia wypada w pierwszy dzień miesiąca (0 - pon, 6 - ndz)
        # size_of_month - ile dni w miesiącu
        (self.first_day_of_week_in_month, self.size_of_month) = monthrange(self.year, self.month)
        self.data = Data(self.number_of_nurses, self.number_of_rooms)
        self.solution = np.ndarray(shape=(4 * self.size_of_month, self.data.number_of_rooms, 2), dtype=float)
        self.data.nurses.sort(key=lambda x: 0 if (x.status < 3) else 1)
        self.value = 0
        self.kara = 0
        # powyżej base_work_hours naliczają się nadgodziny
        self.base_work_hours = 5*7*4 + (self.size_of_month - 4*7)*7  # - holidays*7
        # minimalna ilość pielęgniarek
        min_number_of_nurses = self.min_number_of_nurses_()

        self.data_for_chart = []
        self.best_solutions = []
        self.tabu_list_for_chart = []

        for i in range(self.solution.shape[1]):
            for j in range(self.solution.shape[0]):
                for nr in range(0, 2):
                    self.solution[j][i][nr] = inf

        # Pierwsze randomowe rozwiązanie, wartość funkcji celu
        self.week()
        self.data.print_nurses()
        self.data.print_room()
        print(self.value_of_solution())
        self.write_schedule()
        if self.check_solution() is True:
            print("Solution can't be found!")
            print("\n")
            self.value_of_solution = inf
            print(self.value_of_solution)
        else:
            # Najlepsze rozwiązanie
            best_sol = self.correction()
            self.nurses_salary(best_sol)
            best_sol.data.print_nurses()
            best_sol.data.print_room()
            print(best_sol.value_of_solution())
            best_sol.write_schedule()

            fig = self.chart()
            plt.show()


    def check_solution(self):
        if inf in self.solution:
            return True

    def chart(self):
        print(self.best_solutions)
        x = np.arange(len(self.data_for_chart))
        y1 = self.data_for_chart
        y2 = self.best_solutions
        y3 = self.tabu_list_for_chart

        fig, [ax1, ax2] = plt.subplots(2, 1, layout='constrained')

        ax1.plot(x, y1, x, y2)
        ax1.set_title('Objective function graph')
        ax1.set_xlabel('Iterations')
        ax1.set_ylabel('Function value')
        ax1.legend(["Solution","Best solution"])
        ax2.plot(x, y3, 'g')
        ax2.set_title('Tabu list graph')
        ax2.set_xlabel('Iterations')
        ax2.set_ylabel('Tabu list length')
        return fig

    def min_number_of_nurses_(self):
        needed_nurses_per_shift = 0
        for room in self.data.rooms:
            needed_nurses_per_shift += room.needed_number_of_nurses

        # aby minimalnie wypełnić grafik (12 h zmian) wystarczą 3 pule pielęgniarek wystarczających na jeden dzień
        return 3 * needed_nurses_per_shift

    def has_nurse_overall_hours(self, nurse):
        overall_hours = nurse.number_of_hours - self.base_work_hours
        return overall_hours > 0

    def salary_for_each_day(self, day_of_week, shift, nurse):
        if day_of_week <= 4:  # pon - pt
            if is_day_shift(shift):
                nurse.salary += 6 * self.data.wage
            if is_night_shift(shift):
                nurse.salary += 2 * 6 * self.data.wage
        if day_of_week == 5:  # sob
            if is_day_shift(shift):
                nurse.salary += 1.5 * 6 * self.data.wage
            if is_night_shift(shift):
                nurse.salary += 2.5 * 6 * self.data.wage
        if day_of_week == 6:  # ndz
            if is_day_shift(shift):
                nurse.salary += 2 * 6 * self.data.wage / 2
            if is_night_shift(shift):
                nurse.salary += 2.5 * 6 * self.data.wage / 2

    def salary_depend_on_overall(self, day_of_week, nurses, shift, best_sol, temp_hours_nurses):
        nurse1 = best_sol.data.nurses[int(nurses[0])]
        if self.has_nurse_overall_hours(nurse1):
            if temp_hours_nurses[nurse1.id] >= self.base_work_hours:
                if is_day_shift(shift):
                    nurse1.salary += 2 * 6 * self.data.wage
                if is_night_shift(shift):
                    nurse1.salary += 1.5 * 6 * self.data.wage
                temp_hours_nurses[nurse1.id] += 6
            else:
                self.salary_for_each_day(day_of_week, shift, nurse1)
        else:
            self.salary_for_each_day(day_of_week, shift, nurse1)

        if nurses[1] >= 0:
            nurse2 = best_sol.data.nurses[int(nurses[1])]
            if self.has_nurse_overall_hours(nurse2):
                if temp_hours_nurses[nurse2.id] >= self.base_work_hours:
                    if is_day_shift(shift):
                        nurse2.salary += 2 * 6 * self.data.wage
                    if is_night_shift(shift):
                        nurse2.salary += 1.5 * 6 * self.data.wage
                    temp_hours_nurses[nurse2.id] += 6
                else:
                    self.salary_for_each_day(day_of_week, shift, nurse2)
            else:
                self.salary_for_each_day(day_of_week, shift, nurse2)

    def nurses_salary(self, best_sol):
        day_of_week = self.first_day_of_week_in_month - 1
        temp_hours_nurses = np.ndarray(self.number_of_nurses)
        temp_hours_nurses[:] = 0
        for shift in range(0, best_sol.solution.shape[0]):
            if shift % 4 == 0:
                day_of_week += 1
                for nurses in best_sol.solution[shift][:]:
                    self.salary_depend_on_overall(day_of_week, nurses, shift, best_sol, temp_hours_nurses)
            if day_of_week == 6:
                day_of_week = 0

    def was_on_previous_night_shift(self, shift, nurse_id):
        if shift <= 3:
            return False

        if shift % 4 == 0:
            if (nurse_id in self.solution[shift - 1][:]) or (nurse_id in self.solution[shift - 2][:]):
                return True

        if shift % 4 == 1:
            if (nurse_id in self.solution[shift - 2][:]) or (nurse_id in self.solution[shift - 3][:]):
                return True

        if shift % 4 == 2:
            if (nurse_id in self.solution[shift - 3][:]) or (nurse_id in self.solution[shift - 4][:]):
                return True

        if shift % 4 == 3:
            if (nurse_id in self.solution[shift - 4][:]) or (nurse_id in self.solution[shift - 5][:]):
                return True

        return False

    def is_in_next_night_shift(self, shift, nurse_id):
        if shift >= self.solution.shape[0] - 2:
            return False

        if shift % 4 == 0:
            if (nurse_id in self.solution[shift + 2][:]) or (nurse_id in self.solution[shift + 3][:]):
                return True

        if shift % 4 == 1:
            if (nurse_id in self.solution[shift + 1][:]) or (nurse_id in self.solution[shift + 2][:]):
                return True

        if shift % 4 == 2:
            if (nurse_id in self.solution[shift + 4][:]) or (nurse_id in self.solution[shift + 5][:]):
                return True

        if shift % 4 == 3:
            if (nurse_id in self.solution[shift + 3][:]) or (nurse_id in self.solution[shift + 4][:]):
                return True

        return False

    def is_in_next_24hours(self, shift, nurse_id):
        if shift >= self.solution.shape[0] - 4:
            return False

        if (nurse_id in self.solution[shift + 1][:]) or (nurse_id in self.solution[shift + 2][:]) \
                or (nurse_id in self.solution[shift + 3][:]) or (nurse_id in self.solution[shift + 4][:]):
            return True

        return False

    def was_on_previous_12h(self, shift, nurse_id):
        if shift <= 2:
            return False

        if (nurse_id in self.solution[shift - 1][:]) or (nurse_id in self.solution[shift - 2][:]):
            return True

        return False

    def is_shift_valid(self, shift, nurse_id):
        if is_night_shift(shift):
            if self.was_on_previous_night_shift(shift, nurse_id):
                return False
            if self.was_on_previous_12h(shift, nurse_id):
                return False
            if self.is_in_next_24hours(shift, nurse_id):
                return False
            return True
        if is_day_shift(shift):
            if self.was_on_previous_night_shift(shift, nurse_id):
                return False
            if self.is_in_next_night_shift(shift, nurse_id):
                return False
            return True

    def value_of_solution(self):
        sum = 0
        for i in self.data.nurses:
            sum += np.abs((self.base_work_hours - i.number_of_hours) ** 2)
        self.value = np.sqrt(sum / self.data.number_of_nurses)
        self.value += self.kara

        return self.value

    def first_solution(self, shift, before_before=[]):
        """Pierwsze randomowe rozwiązanie"""
        before = []
        # To jest po to aby nie dodawało nam bez przerwy tych samych pielęgniarek
        # najpierw miesza pielęgniarki i potem sortuje je w kolejności po priorytecie
        if shift % 2 == 0:
            random.shuffle(self.data.nurses)
            self.data.nurses.sort(key=lambda x: 0 if (x.status < 3) else 1)

        # Dodawanie pielęgniarek do grafiku
        # Wstawiamy po kolei pielęgniarki do danej zmiany shift
        # Zapisujemy poprzednie wartości, dzięki czemu są zachowane 12 godzinne odstępy
        # Uwzględnione jest to, że na danej zmianie nie może się pojawić kilka razy ta sama pielęgniarka
        # Uwzględnione są priorytety pielęgniarek i sal
        # Dodajemy godziny
        # Funkcja zwraca nam dany grafik utworzonej zmiany
        for i in [nurse for nurse in self.data.nurses if nurse.id not in before_before]:
            if not self.was_on_previous_night_shift(shift, i.id):
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

    def week(self):
        """Tworzymy grafik dla tygodnia"""
        # Co 2 zmiany (12h tryb pracy) wstawiamy inne pielęgniarki za pomocą funkcji first_solution
        # Na końcu sortujemy pielęgniarki aby nie powodowało to późniejszych błędów
        self.first_solution(0)
        before_before = self.first_solution(1)
        for i in range(2, self.solution.shape[0], 2):
            self.first_solution(i, before_before)
            before_before = self.first_solution(i + 1, before_before)
        self.data.nurses.sort(key=lambda x: x.id)

    def min_max_hours(self, must_be_shuffled=0):
        """Funkcja wyznacza pielęgniarkę z najmniejszą i największą liczbą godzin"""

        # Parametr must_be_shuffled mówi nam o tym, że należy dokonać mieszania pielęgniarek
        # aby znaleźć inną o tekiej samej ilości godzin
        nurses_hours1 = [nurse.number_of_hours for nurse in self.data.nurses]
        if must_be_shuffled:
            random.shuffle(nurses_hours1)

        min_hours1 = min(nurses_hours1)
        min_hours_nurse1 = self.data.nurses[nurses_hours1.index(min_hours1)]
        max_hours1 = max(nurses_hours1)
        max_hours_nurse1 = self.data.nurses[nurses_hours1.index(max_hours1)]

        return min_hours_nurse1, max_hours_nurse1

    def status_nurses(self, must_be_shuffled=0):
        """Funkcja wyznacza pielęgniarki z tym samym statusem"""

        # Parametr must_be_shuffled mówi nam o tym, że należy dokonać mieszania pielęgniarek
        # aby znaleźć inną o tekim samym priorytecie
        nurse2 = None
        index = 0
        random.shuffle(self.data.nurses)
        while nurse2 is None:
            nurse1 = self.data.nurses[index]
            for i in self.data.nurses:
                if i != nurse1:
                    if i.status == nurse1.status:
                        nurse2 = i
                        break
            index += 1
        print(nurse1.number_of_hours, nurse2.number_of_hours)

        return nurse1, nurse2

    def nurses_swap(self, nurse_min, nurse_max, tabu_list):
        """Funkcja wstawia pielęgniarkę z minimalną liczbą godzin w miejsce pielęgniarki z max liczbą godzin
        Wykonuje 1 zmianę"""

        flag = 0
        # W tych zmiennych zapisujemy indeksy dla których zaszła zmiana
        i1 = None
        j1 = None

        # Iterujemy po zmianach (co 2 bo 12 wymiar godzin)
        for i in range(0, self.solution.shape[0], 2):
            if self.is_shift_valid(i, nurse_min.id):
                for j in self.data.rooms:
                    # Sprawdzam czy indeksy znajdują się na liście tabu(były wcześniej zmieniane)
                    if [i, j.id] not in tabu_list:
                        # Sprawdzam czy w miejscu znajduje siępielęgniarka, którą chcę zamienić
                        # Sprawdzam czy w danej zmianie nie ma pielęgniarki którą chcę wsadzić
                        # Jeżeli sprzeczne priorytety - stosuję karę
                        # flag w celu określenia czy zaszła zmiana
                        if self.solution[i][j.id][0] == nurse_max.id \
                                and nurse_min.id not in [self.solution[i][j][0] for j in range(self.number_of_rooms)] \
                                and nurse_min.id not in [self.solution[i][j][1] for j in range(self.number_of_rooms)]:
                            if j.priority == 2 and nurse_min.status < 3:
                                self.kara += 1
                            flag = 1

                            # Wsadzam pielęgniarkę min w 2 miejsca (12h)
                            # Dodaję godziny przepracowane dla min i odejmuję dla max
                            self.solution[i][j.id][0] = nurse_min.id
                            self.solution[i + 1][j.id][0] = nurse_min.id
                            self.data.nurses[nurse_min.id].number_of_hours += 12
                            self.data.nurses[nurse_max.id].number_of_hours -= 12

                            # Zapisuję dla jakich indeksów zachodzi zmiana
                            i1 = i
                            j1 = j
                            break

                        # Identyczne działanie jak wyżej z tym, że działąmy dla 1 (dla drugiej pielęgniarki w zmianie)
                        if self.solution[i][j.id][1] == nurse_max.id \
                                and nurse_min.id not in [self.solution[i][j][0] for j in range(self.number_of_rooms)] \
                                and nurse_min.id not in [self.solution[i][j][1] for j in range(self.number_of_rooms)]:
                            if j.priority == 2 and nurse_min.status < 3:
                                self.kara += 1
                            flag = 1
                            self.solution[i][j.id][1] = nurse_min.id
                            self.solution[i + 1][j.id][1] = nurse_min.id
                            self.data.nurses[nurse_min.id].number_of_hours += 12
                            self.data.nurses[nurse_max.id].number_of_hours -= 12
                            i1 = i
                            j1 = j
                            break
                    else:
                        # Gdy ruch jest zakazany to szukamy w kolejnej iteracji danego indeksu
                        continue
                        # print("Ruch zakazany", i, j.id)
            # Wychwytuje nam czy zaszła zmiana i przerywa funkcje
            if flag:
                break
        # Funkcja zwraca indeksy, dla których zachodzi zmiana (lub None, None gdy nie ma zmiany)
        return i1, j1

    def choose_method(self, method, tabu_list, must_be_shuffled = 0):
        """Funkcja wybiera metodę do przeprowadzenia zamiany"""
        #Pielęgniarki z min i max ilością godzin
        if method == 'Min_Max':
            min_hours_nurse1, max_hours_nurse1 = self.min_max_hours(must_be_shuffled)
            i1, j1 = self.nurses_swap(min_hours_nurse1, max_hours_nurse1, tabu_list)
        #Randomowe pielęgniarki
        elif method == 'Random':
            i1, j1 = self.nurses_swap(random.choice(self.data.nurses), random.choice(self.data.nurses), tabu_list)
        #Pielęgniarki z tym samym priorytetem
        elif method == 'Priority':
            min_hours_nurse1, max_hours_nurse1 = self.status_nurses(must_be_shuffled)
            i1, j1 = self.nurses_swap(min_hours_nurse1, max_hours_nurse1, tabu_list)
        return i1, j1

    def correction(self, method = 'Min_Max'):
        """Funkcja tworzy i zwraca najlepsze rozwiązanie"""
        flag = 0
        iteration1 = 0
        iteration2 = 0
        tabu_list = []

        # Tworzymy kopię aby następnie móc przechowywyać w niej najlepsze rozwiązanie
        best_sol = copy.deepcopy(self)
        self.data_for_chart.append(self.value_of_solution())
        self.best_solutions.append(best_sol.value_of_solution())
        self.tabu_list_for_chart.append(0)

        # Sprawdzamy czy czasem rozwiązanie pierwotne nie jest najlepsze
        # Jeżeli tak to zwracam je i program kończy się
        hours = [nurse.number_of_hours for nurse in self.data.nurses]
        if hours[:-1] == hours[1:]:
            return best_sol

        # Wyliczam pielęgniarki do zamiany i zamieniam je
        i1, j1 = self.choose_method(method, tabu_list)


        # Jeżeli zwrócone indeksy = None (czyli nie zaszła zamiana -
        # sprawdzamy iteracja max aby się nie zapętlić
        # Gdy przekroczy iteracje i nie znajdzie odpowiednich pielęgniarek to zwracamy bieżące rozwiązanie
        while j1 is None:
            iteration1 += 1
            i1, j1 = self.choose_method(method, tabu_list, 1)
            if iteration1 > 10:
                return best_sol

        # Jeżeli j1 != None (była zmiana) dodajemy indeksy do listy tabu
        tabu_list.append([i1, j1.id])


        # Wykonujemy zamiany aż do momentu gdy 10 razy pod rząd nie będzie zachodzić poprawa
        while 1:
            # zapisujemy poprzednie indeksy
            # Sprawdzamy czy aktualne indeksy znajdują się w tabu liście i usuwamy je
            # - żeby nie było zdublowań - jeżeli indeksy mają być na stałe w liście to zostaną dodane później
            i1_old, j1_old = i1, j1
            if [i1, j1.id] in tabu_list:
                tabu_list.remove([i1_old, j1_old.id])

            # Obiczam funkcje celu poprzedniego rozwiązania
            # Indeksy zamian
            value_of_solution_before = self.value_of_solution()
            i1, j1 = self.choose_method(method, tabu_list)


            # Tutaj podobnie jak poprzednio
            while j1 is None:
                iteration2 += 1
                i1, j1 = self.choose_method(method, tabu_list, 1)
                if iteration2 > 10:
                    return best_sol

            # Funkcja celu po zamianie
            value_of_solution_after = self.value_of_solution()

            # Dodajemy indeksy do listy tabu (zapamiętanie ostatnich ruchów)
            tabu_list.append([i1, j1.id])

            # Sprawdzamy czy nasze rozwiązanie jest lepsze od najlepszego porównując funkcje celu
            # Jeżeli tak to zapisujemy bieżące rozwiązanie jako najlepsze
            if value_of_solution_after < best_sol.value_of_solution():
                best_sol = copy.deepcopy(self)
            # Sprawdzamy czy nasze rozwiązanie jest lepsze od poprzedniego
            # Jeżeli nie to aktualizujemy flagę, która mówi nam ile razy jeszcze możemy mieć gorsze rozwiązanie
            # Przeciwnie - dodajemy do listy tabu nasze indeksy
            if value_of_solution_after >= value_of_solution_before:
                flag += 1
            else:
                tabu_list.append([i1, j1.id])
            self.data_for_chart.append(self.value_of_solution())
            self.best_solutions.append(best_sol.value_of_solution())
            self.tabu_list_for_chart.append(len(tabu_list))
            # Jeżeli 10 razy nasze rozwiązanie będzie gorsze od poprzedniego to zwracamy rozwiązanie
            if flag > 10:
                return best_sol




    def write_schedule(self):
        """Wypisanie rozkładu"""
        for i in range(self.solution.shape[1]):
            for j in range(self.solution.shape[0]):
                print("[", end="")
                for nr in range(0, 2):
                    if nr == 0:
                        print(self.solution[j][i][nr], " ", end="")
                    else:
                        print(self.solution[j][i][nr], end="")
                print("]", end="")
            print("")
