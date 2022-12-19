#!/usr/bin/python
# -*- coding: utf-8 -

from utilities import *


def is_night_shift(shift):
    return shift % 4 == 2 or shift % 4 == 3


def is_day_shift(shift):
    return shift % 4 == 1 or shift % 4 == 0


class Solution:
    def __init__(self, number_of_nurses_, number_of_rooms_):
        self.number_of_rooms = number_of_rooms_
        self.number_of_nurses = number_of_nurses_
        self.data = Data(self.number_of_nurses, self.number_of_rooms)
        self.solution = np.ndarray(shape=(4 * 7, self.data.number_of_rooms, 2), dtype=float)
        self.data.nurses.sort(key=lambda x: 0 if (x.status < 3) else 1)
        self.value = 0
        self.kara = 0

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

        print("\n")

        # Najlepsze rozwiązanie
        best_sol = self.correction()
        best_sol.data.print_nurses()
        best_sol.data.print_room()
        print(best_sol.value_of_solution())
        best_sol.write_schedule()

    def has_nurse_overall_hours(self, nurse):
        base_work_hours = self.solution.shape[0] * 6 * self.data.number_of_rooms / self.data.number_of_nurses
        overall_hours = nurse.number_of_hours - base_work_hours
        if overall_hours != 0:
            return True


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
        if shift >= 7 * 4 - 2:
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
        if shift >= 4 * 7 - 4:
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
        overall_hours = self.solution.shape[0] * 6 * self.data.number_of_rooms / self.data.number_of_nurses
        sum = 0
        for i in self.data.nurses:
            sum += (overall_hours - i.number_of_hours) ** 2
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
        for i in range(2, 28, 2):
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
                        # Sprawdzam czy w miejscu znajduje się max pielęgniarka, którą chcę zamienić
                        # Sprawdzam czy w danej zmianie nie ma min pielęgniarki którą chcę wsadzić
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

    def correction(self):
        """Funkcja tworzy i zwraca najlepsze rozwiązanie"""
        flag = 0
        iteration1 = 0
        iteration2 = 0
        tabu_list = []

        # Tworzymy kopię aby następnie móc przechowywyać w niej najlepsze rozwiązanie
        best_sol = copy.deepcopy(self)

        # Sprawdzamy czy czasem rozwiązanie pierwotne nie jest najlepsze
        # (w momencie gdy każda pielęgniarka ma tyle samo godzin)
        # Jeżeli tak to zwracam je i program kończy się
        hours = [nurse.number_of_hours for nurse in self.data.nurses]
        if hours[:-1] == hours[1:]:
            return best_sol

        # Wyliczam pielęgniarkę z najmniejszą i największą ilością godzin
        # robię podmianę pielęgniarek i zapamiętuję dla jakich indeksów zaszła zmiana
        min_hours_nurse1, max_hours_nurse1 = self.min_max_hours()
        i1, j1 = self.nurses_swap(min_hours_nurse1, max_hours_nurse1, tabu_list)

        # Jeżeli zwrócone indeksy = None (czyli nie zaszła zamiana -
        # sytuacja gdy mamy kilka pielęgniarek z max lub min godzinami i akurat dla tej nie ma możliwości zamiany)
        # sprawdzamy iteracja max aby się nie zapętlić
        # Gdy przekroczy iteracje i nie znajdzie odpowiednich pielęgniarek to zwracamy bieżące rozwiązanie
        while j1 is None:
            iteration1 += 1
            min_hours_nurse1, max_hours_nurse1 = self.min_max_hours(1)
            i1, j1 = self.nurses_swap(min_hours_nurse1, max_hours_nurse1, tabu_list)
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
            # minimalne i maksymalne pielęgniarki
            # Indeksy zamian
            value_of_solution_before = self.value_of_solution()
            min_hours_nurse1, max_hours_nurse1 = self.min_max_hours()
            i1, j1 = self.nurses_swap(min_hours_nurse1, max_hours_nurse1, tabu_list)

            # Tutaj podobnie jak poprzednio
            while j1 is None:
                iteration2 += 1
                min_hours_nurse1, max_hours_nurse1 = self.min_max_hours(1)
                i1, j1 = self.nurses_swap(min_hours_nurse1, max_hours_nurse1, tabu_list)
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
