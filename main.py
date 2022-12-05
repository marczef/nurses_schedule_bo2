from utilities import *

def main():
    data = Data(5,3)
    data.print_nurses()
    data.print_room()

    solution = Solution(Data(5, 6), 1)
    solution.print_solution()

if __name__ == "__main__":
    main()