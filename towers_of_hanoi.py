class TowerHanoi:
    """Class for Tower of Hanoi console-game."""

    def __init__(self):
        self.tower_a = [5, 4, 3, 2, 1]
        self.tower_b = []
        self.tower_c = []

        self.win = False

        print("\nTowers of Hanoi\nMove the whole stack of discs from A to B or C.\n")
        print("One disc per move, can only stack smaller discs on top of bigger ones.\nHit [q] to exit.\n")

    def play(self):
        # main game loop
        while not self.win:
            self.print_towers()
            self.from_tower = self.get_user_choice()
            self.to_tower = self.get_destination()
            self.make_move(self.from_tower, self.to_tower)          
            self.check_win()

    def get_user_choice(self):
        # get an userinput to chose a disc
        pool = ["a", "b", "c", "q"]
        choice = ""
       
        while not choice in pool:
            choice = input("\nPlease chose from a tower:\n> ")
            choice = choice.lower()
        if choice == "q":
            print("\nThanks for playing!")
            exit(0)

        empty_stack = self.check_empty(choice)

        if not empty_stack:          
            return choice
        elif empty_stack:
            print("Cannot chose from an empty stack!")
            return self.get_user_choice()

    def check_empty(self, choice):
        # check if the chosen list is empty
        if choice == "a" and len(self.tower_a) == 0:
            return True
        elif choice == "b" and len(self.tower_b) == 0:
            return True
        elif choice == "c" and len(self.tower_c) == 0:
            return True
        else:
            return False
        
    def get_destination(self):
        # get an userinput to set the destination
        pool = self.create_pool(self.from_tower)
        choice = input("Please chose the destination:\n> ")
        choice = choice.lower()
        while not choice in pool:
            choice = input("Please chose the destination:\n> ")
            choice = choice.lower() 
        if choice == "q":
            print("\nThanks for playing!")
            exit(0)
        return choice
        
    def create_pool(self, from_tower):
        # removes the startpoint from the possible choices
        pool = ["a", "b", "c", "q"]
        pool.remove(from_tower)
        return pool

    def check_move_possible(self, from_tower, to_tower):
        # checks if a move is possible  
        if from_tower == "a" and to_tower == "b":
            if not self.tower_b:
                return True
            elif self.tower_a[-1] < self.tower_b[-1]:
                return True
            elif self.tower_a[-1] > self.tower_b[-1]:
                print("Can't stack disc on top of smaller sized disc!")
                return False
        if from_tower == "a" and to_tower == "c":
            if not self.tower_c:
                return True
            elif self.tower_a[-1] < self.tower_c[-1]:
                return True
            elif self.tower_a[-1] > self.tower_c[-1]:
                print("Can't stack disc on top of smaller sized disc!")
                return False
        if from_tower == "b" and to_tower == "a":
            if not self.tower_a:
                return True
            elif self.tower_b[-1] < self.tower_a[-1]:
                return True
            elif self.tower_b[-1] > self.tower_a[-1]:
                print("Can't stack disc on top of smaller sized disc!")
                return False
        if from_tower == "b" and to_tower == "c":
            if not self.tower_c:
                return True
            elif self.tower_b[-1] < self.tower_c[-1]:
                return True
            elif self.tower_b[-1] > self.tower_c[-1]:
                print("Can't stack disc on top of smaller sized disc!")
                return False
        if from_tower == "c" and to_tower == "a":
            if not self.tower_a:
                return True
            elif self.tower_c[-1] < self.tower_a[-1]:
                return True
            elif self.tower_c[-1] > self.tower_a[-1]:
                print("Can't stack disc on top of smaller sized disc!")
                return False 
        if from_tower == "c" and to_tower == "b":
            if not self.tower_b:
                return True
            elif self.tower_c[-1] < self.tower_b[-1]:
                return True
            elif self.tower_c[-1] > self.tower_b[-1]:
                print("Can't stack disc on top of smaller sized disc!")
                return False    

    def make_move(self, from_tower, to_tower):
        # moves the disc if move is possible
        move_possible = self.check_move_possible(self.from_tower, 
                                                 self.to_tower)
              
        if move_possible:
            if from_tower == "a" and to_tower == "b":
                disc = self.tower_a.pop()
                self.tower_b.append(disc)            
            if from_tower == "a" and to_tower == "c":
                disc = self.tower_a.pop()
                self.tower_c.append(disc)
            if from_tower == "b" and to_tower == "a":
                disc = self.tower_b.pop()
                self.tower_a.append(disc)
            if from_tower == "b" and to_tower == "c":
                disc = self.tower_b.pop()
                self.tower_c.append(disc)
            if from_tower == "c" and to_tower == "a":
                disc = self.tower_c.pop()
                self.tower_a.append(disc)
            if from_tower == "c" and to_tower == "b":
                disc = self.tower_c.pop()
                self.tower_b.append(disc)

    def check_win(self):
        # checks if the game is finished
        if self.tower_b == [5, 4, 3, 2, 1] or self.tower_c == [5, 4, 3, 2, 1]:
            self.win = True
            self.ending()

    def print_towers(self):
        # prepare the printlayout with tower-lists and print to console
        print_list_tower_a = {
                            0 : "             ",
                            1 : "             ",
                            2 : "             ",
                            3 : "             ",
                            4 : "             ",
                            }
        print_list_tower_b = {
                            0 : "             ",
                            1 : "             ",
                            2 : "             ",
                            3 : "             ",
                            4 : "             ",
                            }
        print_list_tower_c = {
                            0 : "             ",
                            1 : "             ",
                            2 : "             ",
                            3 : "             ",
                            4 : "             ",
                            }
                                   
        if self.tower_a:
            counter = 0  
            for i in range(len(self.tower_a)):
                disc = self.create_disc(self.tower_a[i])
                print_list_tower_a[counter] = disc
                counter += 1 
        if self.tower_b:
            counter = 0  
            for i in range(len(self.tower_b)):
                disc = self.create_disc(self.tower_b[i])
                print_list_tower_b[counter] = disc 
                counter += 1
        if self.tower_c:
            counter = 0  
            for i in range(len(self.tower_c)):
                disc = self.create_disc(self.tower_c[i])
                print_list_tower_c[counter] = disc 
                counter += 1 

        print(f"""
        {print_list_tower_a[4]}    {print_list_tower_b[4]}    {print_list_tower_c[4]}
        {print_list_tower_a[3]}    {print_list_tower_b[3]}    {print_list_tower_c[3]}
        {print_list_tower_a[2]}    {print_list_tower_b[2]}    {print_list_tower_c[2]}
        {print_list_tower_a[1]}    {print_list_tower_b[1]}    {print_list_tower_c[1]}
        {print_list_tower_a[0]}    {print_list_tower_b[0]}    {print_list_tower_c[0]}
              {"^"}                {"^"}                {"^"}
              {"A"}                {"B"}                {"C"}""")

    def create_disc(self, disc_size):
        # returns the disc-layouts for printing
        if disc_size == 1:
            return "    [x1x]    "
        elif disc_size == 2:
            return "   [xx2xx]   "
        elif disc_size == 3:
            return "  [xxx3xxx]  "
        elif disc_size == 4:
            return " [xxxx4xxxx] "
        elif disc_size == 5:
            return "[xxxxx5xxxxx]"
        
    def ending(self):
        self.print_towers()
        print("\nCongratulations, you did it!\nThanks for playing!!")


if __name__ == "__main__":
    game = TowerHanoi()
    game.play()