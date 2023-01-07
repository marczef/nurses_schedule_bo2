from solution import Solution
from app import *

def main():
    data = Solution(2022, 12, 130, 20, 70, 'Min_Max', 100, False)

    data.write_schedule()

if __name__ == "__main__":
    app()

#kara (normalna jej pensja* dodatkowa ilość godzin)**2 tyg - zmęczeniu
#TODO: minimum pielęgniarek
