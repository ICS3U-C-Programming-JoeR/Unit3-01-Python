#!/usr/bin/env python3
# Created By: Joe Rugezo
# Date: october 10, 2023
# This program asks the user for the subtotal and the tax percentage. It then calculates and displays the HST and the total.
import constants

def main():

    subtotal = float(input("Enter subtotal: $"))
    
    tax = subtotal * constants.TAX_RATE_ONTARIO / 100
    total = subtotal + tax

    print("")
    print("You entered a subtotal of ${:.2f}".format(subtotal))
    print("The HST is ${0:.2f} and the total is ${1:.2f}".format(tax, total))


if __name__ == "__main__":
  main()