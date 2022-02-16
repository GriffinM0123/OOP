import InsectClass as I


def main():

    mosquito = I.Insect(2, 4)
    housefly = I.Insect(3, 6)

    mosquito.miles()
    housefly.miles()

    print("The number of miles the mosquito flies is: ", mosquito.get_miles())
    print("The number of miles the housefly flies is: ", housefly.get_miles())


main()
