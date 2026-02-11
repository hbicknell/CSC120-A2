class Computer:

    #attributes
    description: str = ""
    processor_type: str = ""
    hard_drive_capacity: int = 0
    memory: int = 0
    operating_system: str = ""
    year_made: int = 0
    price: int = 0 

    #The computer constructor
    def __init__(self, description: str, processor: str, hard_drive: int,
                memory: int, OS: str, year: int, price: int):
        self.description = description 
        self.processor_type = processor
        self.hard_drive_capacity = hard_drive
        self.memory = memory 
        self.operating_system = OS
        self.year_made = year
        self.price = price

    #The methods use: computer info, os change, price change

    def computer_info (self):
        if self == None: 
             print("no!")
        else:
            return f"{self.description} -- Processor Type: {self.processor_type} Hard Drive Capacity: {self.hard_drive_capacity} Memory: {self.memory} Operating System: {self.operating_system} Made: {self.year_made} Price:  {self.price}"
    
    def os_change(self, new_os: str):
        self.operating_system = new_os
        return self.operating_system
    
    def update_price(self, new_price: int):
        self.price = new_price
        return self.price

#the main part of the code
def main(): 
    myComputer:Computer = Computer("hi", "heya", 13, 23, "haydens", 2007, 0)
    print(myComputer.price)
    print(myComputer.computer_info())
    myComputer.update_price(30)
    print(myComputer.computer_info())

if __name__ == "__main__":
    main()