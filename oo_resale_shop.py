from computer import *
class ResaleShop:

    #attributes
    inventory: list = []

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, inventory: list):
       self.inventory = inventory
    

    def buy(self, name: str, description: str):
        
        if name in self.inventory: 
            return "You already own that!"
        else: 
            self.inventory.append(name)
            print("Buying:", description)
            return description

    def sell(self, number: int, name: str, description: str):
        
        if name in self.inventory: 
            number -= 1
            del self.inventory[number]
            del name
            print("Selling:", description )
            return f"{description} sold!"
        else: 
            return ("You don't own that!")
    
    def refurbish(self, computer, os: str, price: int):
        if computer in self.inventory: 
            computer.os_change(os)
            computer.update_price(price)
            print ("Refurbishing Computer")
            return computer.operating_system, computer.update_price
        else: 
            return "You don't own this!"




def main():
    theShop: ResaleShop = ResaleShop([])
    theComputer:Computer = Computer("hi", "heya", 13, 23, "haydens", 2007, 0)

if __name__ == "__main__":
    main()
