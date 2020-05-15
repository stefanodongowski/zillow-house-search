# Stefano Dongowski
# 11.22.2019
# Test

from HouseClass import House


def get_file():
    """Gets the filename from user and opens it"""
    tries = 0
    while tries <= 4:
        try:
            filename = input("Enter filename: ")
            inFile = open(filename,"r")
            break
        except FileNotFoundError:
            print("File not found. Remaining attempts: " + str(4-tries))
            tries += 1
    if tries > 4:
        raise IOError
    else:
        return filename,inFile


def create_list():
    """Creates a list of all the houses in the CSV files provided by user
    (houses are stored as objects)"""

    filename,inFile = get_file()
    houses = []
    line = inFile.readline()
    line = inFile.readline()
    while line:
        house_aspects = line.split(',')
        house = House(house_aspects[0],house_aspects[1],house_aspects[2],house_aspects[3],house_aspects[4],house_aspects[5],house_aspects[6])
        houses.append(house)
        line = inFile.readline()
    return houses


def search(price,houses):
    """Searches the list of house objects for a house matching the price specified by the user"""
    found = False

    for house in houses:
        print("House #" + str(house.get_index()) + "\n\tPrice: " + str(house.get_list_price()))
        if house.get_list_price() == int(price):
            print("\tThis house is your target price!")
            found = True
            return "\n\tHouse index: " + str(houses.index(house)) + "\n\tFound? " + str(found)
            break
        else:
            print("\tThis house is not your target price")

    if found is False:
        return "\n\tNo houses with that price."


def sort(houses):
    """sorts the list of houses by the year they were built"""
    for i in range(len(houses)):
        for j in range(len(houses) - 1):
            if houses[j].year_built > houses[j + 1].year_built:
                temp = houses[j]
                houses[j] = houses[j + 1]
                houses[j + 1] = temp
    return houses


def main():
    houses = create_list()
    # initial list of houses display
    print("----INITIAL LIST----\n")
    for house in houses:
        print('House #' + str(house.get_index()) + ":\n\tLiving space - " + str(house.get_sq_ft()) + " sq ft\n\tBeds - " + str(house.get_beds()) + "\n\tBaths - " + str(house.get_baths()) + "\n\tZIP - " + str(house.get_zip()) + "\n\tYear built - " + str(house.get_year_built()) + "\n\tList price - " + str(house.get_list_price()))
    print("\n==============================\n")

    # displays the search algorithm in effect
    print("----SEARCHING----")
    target_price = input("What price of house are you looking for? ")
    print("\n\nSearch results: " + str(search(target_price,houses)) + "\n\n\n")
    print(input("Hit enter to continue (to see example of house not found in list)"))
    # shows what happens when a house with the specified price isnt in the list
    print("\n--SEARCHING FOR A VALUE NOT IN THE LIST--")
    target_price = 19384703
    print("\n\nSearch results: " + str(search(target_price, houses)))
    print(input("Hit enter twice to continue (to see list sorted by year)"))
    # sorts the list of houses by year they were constructed and displays the new sorted list
    print("\n\n----SORTING----")
    houses = sort(houses)
    for house in houses:
        print('House #' + str(house.get_index()) + ":\n\tLiving space - " + str(house.get_sq_ft()) + " sq ft\n\tBeds - " + str(house.get_beds()) + "\n\tBaths - " + str(house.get_baths()) + "\n\tZIP - " + str(house.get_zip()) + "\n\tYear built - " + str(house.get_year_built()) + "\n\tList price - " + str(house.get_list_price()))
    print("\n==============================\n")


main()