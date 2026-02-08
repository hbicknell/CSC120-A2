class Computer:

    # What attributes will it need?
    description: str = ""
    processor_type: str = ""
    hard_drive_capacity: int = 0
    memory: int = 0
    operating_system: str = ""
    year_made: int = 0
    price: int = 0 

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, description: str, processor: str, hard_drive: int,
                memory: int, OS: str, year: int, price: int):
        self.description = description 
        self.processor = processor
        self.hard_drive_capacity = hard_drive
        self.memory = memory 
        self.operating_system = OS
        self.year_made = year
        self.price = price

    # What methods will you need?

    def computer_info (self):
         return f"{self.description} -- Processor Type: {self.processor_type} Hard Drive Capacity: {self.hard_drive_capacity} Memory: {self.memory} Operating System: {self.operating_system} Made: {self.year_made} Price:  {self.price}"
    
    def refurbish(self, new_os: str):
        self.operating_system = new_os
        return self.operating_system
    
    def update_price(self, new_price: int):
        self.price = new_price
        return self.price


def main(): 
    myComputer:Computer = Computer("hi", "heya", 13, 23, "haydens", 2007, 0)
    print(myComputer.price)
    print(myComputer.computer_info())
    myComputer.update_price(30)
    print(myComputer.computer_info())

if __name__ == "__main__":
    main()