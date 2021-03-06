from services.flightmanager import *
from services.bookingmanager import *

aircraftManager = AircraftManager()
flightManager = FlightManager(aircraftManager)
passengerManager = PassengerManager()
bookingManager = BookingManager(passengerManager, flightManager)

def main():
    flag = True
    options = [1, 2, 3, 4]
    while flag:
        mainMenu()
        menuOption = int(input("\t-->  "))
        if menuOption == 0:
            exit()
        elif menuOption in options:
            subMenu(menuOption)
        else:
            print("Please Enter a valid option")
            main()

def mainMenu():
    print(f"""
            Airline Management Menu
            Enter (1) to Manage Aircrafts
            Enter (2) to Manage Flights
            Enter (3) to Manage Passengers
            Enter (4) to Manage Bookings
            Enter (0) to Exit Menu""")

def subMenu(menuOption):
    if menuOption == 1:
        print(f"""
                Aircraft Management Menu
                Enter (1) to Create Aircrafts
                Enter (2) to Search Aircrafts
                Enter (3) to Update Aircrafts
                Enter (4) to Delete Aircrafts
                Enter (5) to Print All Aircrafts
                Enter (0) to Exit to Main-Menu""")
        menuOption = int(input("\t-->  "))
        aircraftMenu(menuOption)
    elif menuOption == 2:
        print(f"""
                Flight Management Menu
                Enter (1) to Create Flight
                Enter (2) to Search Flight
                Enter (3) to Update Flight
                Enter (4) to Delete Flight
                Enter (5) to Print All Flights
                Enter (0) to Exit Main-Menu""")
        menuOption = int(input("\t-->  "))
        flightMenu(menuOption)
    elif menuOption == 3:
        print(f"""
                Passenger Management Menu
                Enter (1) to Create Passenger
                Enter (2) to Search Passenger
                Enter (3) to Update Passenger
                Enter (4) to Delete Passenger
                Enter (5) to Print All Passengers
                Enter (0) to Exit Main-Menu""")
        menuOption = int(input("\t-->  "))
        passengerMenu(menuOption)
    elif menuOption == 4:
        print(f"""
                Booking Management Menu
                Enter (1) to Create Booking
                Enter (2) to Search Booking
                Enter (3) to Update Booking
                Enter (4) to Delete Booking
                Enter (5) to Print All Bookings
                Enter (0) to Exit Main-Menu""")
        menuOption = int(input("\t-->  "))
        bookingMenu(menuOption)

# Aircraft
def aircraftMenu(menuOption):
    if menuOption == 1:
        name = input("Enter The name of the Aircraft \n :")
        model = input("Enter the model of the Aircraft \n :")
        capacity = input("Enter the capacity of the Aircraft \n :")
        aircraftManager.createCraft(name, model, capacity)
    elif menuOption == 2:
        regNo = input("Enter the Registration Number of the Aircraft you're looking for \n :")
        aircraftManager.search(regNo)
    elif menuOption == 3:
        regNo = input("Enter the Registration Number of the Aircraft you want to Update \n :")
        name = input("Enter The  new name of the Aircraft \n :")
        model = input("Enter the new model of the Aircraft \n :")
        capacity = input("Enter the new capacity of the Aircraft \n :")
        aircraftManager.update(name, model, capacity, regNo)
    elif menuOption == 4:
        regNo = input("Enter the Registration Number of the Aircraft you want to Delete \n :")
        aircraftManager.delete(regNo)
    elif menuOption == 5:
        aircraftManager.printAll()
    elif menuOption == 0:
        main()
    else:
        print("Please enter a valid option")
        subMenu(1)
        
#Flight
def flightMenu(menuOption):
    if menuOption == 1:
        aircraft = input("Enter The aircraft of the Flight \n :")
        takeoffloc = input(
            "Enter the takeoffloc of the Flight \n :")
        destination = input(
            "Enter the destination of the Flight \n :")
        date = input("Enter the date \n :")
        time = input("Enter the time \n :")
        flightManager.createFlight(
            aircraft, takeoffloc, destination, date, time)
    elif menuOption == 2:
        flightNo = int(
            input("Enter the Flight Number of the Flight you're looking for \n :"))
        flightManager.search(flightNo)
    elif menuOption == 3:
        flightNo = input(
            "Enter the Flight Number of the Flight you want to Update \n :")
        aircraft = input("Enter The aircraft of the Flight \n :")
        takeoffloc = input(
            "Enter the takeoffloc of the Flight \n :")
        destination = input(
            "Enter the destination of the Flight \n :")
        date = input("Enter the date \n :")
        time = input("Enter the time \n :")
        flightManager.update(
            aircraft, takeoffloc, destination, date, time, flightNo)
    elif menuOption == 4:
        regNo = input(
            "Enter the Registration Number of the Flight you want to Delete \n :")
        flightManager.delete(regNo)
    elif menuOption == 5:
        flightManager.printAll()
    elif menuOption == 0:
        main()
    else:
        print("Please enter a valid option")
        subMenu(2)

#Passenger
def passengerMenu(menuOption):
    if menuOption == 1:
        name = input("Enter The name of the Passenger \n :")
        email = input("Enter the email of the Passenger \n :")
        address = input("Enter the address of the Passenger \n :")
        regNo = input("Enter the Registration Number \n :")
        passengerManager.createPassenger(name, email, address, regNo)
    elif menuOption == 2:
        regNo = input("Enter the Registration Number of the Passenger you're looking for \n :")
        passengerManager.search(regNo)
    elif menuOption == 3:
        regNo = input("Enter the Registration Number of the Passenger you want to Update \n :")
        name = input("Enter The  new name of the Passenger \n :")
        email = input("Enter the new email of the Passenger \n :")
        address = input("Enter the new address of the Passenger \n :")
        passengerManager.update(name, email, address, regNo)
    elif menuOption == 4:
        regNo = input("Enter the Registration Number of the Passenger you want to Delete \n :")
        passengerManager.delete(regNo)
    elif menuOption == 5:
        passengerManager.printAll()
    elif menuOption == 0:
        main()
    else:
        print("Please enter a valid option")
        subMenu(3)

#Booking        
def bookingMenu(menuOption):
    if menuOption == 1:
        passenger = input("Enter The name of the Passenger booking the flight \n : ")
        flightNo = input("Enter the Flight Number of the Flight you want to Book \n : ")
        ticktype = input("Which Ticket Type do you want to Book? \n (ONE-WAY) or (RETURN): ")
        tickclass = input("Which Ticket Class are you Booking? \n (FIRST CLASS), (BUSINESS CLASS), or (ECONOMY): ")
        regNo = input("Enter the Registration Number \n :")
        bookingManager.createBooking(
            passenger, flightNo, ticktype, tickclass, regNo)
    elif menuOption == 2:
        regNo = input("Enter the Registration Number of the Booking you're looking for \n : ")
        bookingManager.search(regNo)
    elif menuOption == 3:
        regNo = input("Enter the Registration Number of the Booking you want to Update \n :")
        passenger = input("Enter The  new passenger Booking the flight \n :")
        flight = input("Enter the Registration Number of the Flight you want to Book \n : ")
        ticktype = input("Which Ticket Type do you want to Book? \n (ONE-WAY) or (RETURN): ")
        tickclass = input("Which Ticket Class are you Booking? \n (FIRST CLASS), (BUSINESS CLASS), or (ECONOMY): ")
        bookingManager.update(passenger, flight, ticktype, tickclass, regNo)
    elif menuOption == 4:
        regNo = input("Enter the Registration Number of the Booking you want to Delete \n :")
        bookingManager.delete(regNo)
    elif menuOption == 5:
        bookingManager.printAll()
    elif menuOption == 0:
        main()
    else:
        print("Please enter a valid option")
        subMenu(4)

main()
