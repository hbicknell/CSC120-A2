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