from computer import *
class ResaleShop:

    # What attributes will it need?
    inventory: list = []
    name_inventory:list = []

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, inventory: list, name: list):
       self.inventory = inventory
       self.name_inventory = name

    # What methods will you need?
    #def buy(self)
        #call compuer() constructor 
        #to create a new computer instance 

        #call inventory.append to add the 
        #new computer instance ot the inventory

    def buy(self, description: str, processor: str, hard_drive: int,
                memory: int, OS: str, year: int, price: int):
        new_computer:Computer = Computer( description, processor , hard_drive, memory, OS , year, price)
        self.name_inventory.append(f"{description}")
        self.inventory.append(new_computer)
        print("Buying:", description)
        return self.name_inventory

    def sell(self, computer_number_in_list: int):
        computer_number_in_list -= 1
        print("Selling:",self.name_inventory[computer_number_in_list] )
        del self.name_inventory[computer_number_in_list]
        del self.inventory[computer_number_in_list]
        return self.name_inventory
    
    def refurbish(self, )

def main():
    TheShop: ResaleShop = ResaleShop([],[])
    print(TheShop.inventory)
    print(TheShop.buy("Mac Pro","Del", 30, 23, "haydens", 2007, 20))
    print(TheShop.buy("Windows","hello", 30, 23, "hayden", 2008, 20))
    print(TheShop.sell(1))
    print(TheShop.inventory)

main()

