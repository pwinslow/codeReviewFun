'''
- No Title describing the overall point of the code
- No comments anywhere in the code
- Looks like turn_left and turn_right could be combined into one function with a direction flag...
- I like that a class was used but it's a little weird to me to have it directly embedded with other code
- I normally like to have code that defines functions/classes/etc separated from code that runs these things
  with a if __name__ == "__main__": statement
- The GRID_MAX_X/Y variables are taken in in one line by parsing a string but the vehicle position and cmd variables
  are taken in in a mess from all over the code... If you're asking the user to input multiple lines, is it possible
  to just ask them to write it all down on multiple lines and then parse the whole thing in one fell swoop?
- The GRID_MAX_X/Y variables are defined globally but then used locally within Vehicle class methods.
  This setup prevents me from putting the Vehicle class in a separate file and then importing. Fix this by requiring
  these variables at instantiation of the class. Same thing with movement!
- There's some code repetition involved in taking in positions and cmds for vehicle_one/two


- Break README explanation of user input up into a more readable list.
- Add punctuation!!!

- Variable/function names seem pretty readable (to me)
'''





first_vehicle_x = None
first_vehicle_y = None

class Vehicle():

    directions = ['N','E','S','W']
    movement = {'N': (0,1), 'E': (1,0), 'S': (0,-1), 'W':(-1,0)}

    def __init__(self, x, y, face, boundaries):
        self.x = x
        self.y = y
        self.dir = face
        self.grid_max_x, self.grid_max_y = boundaries

    def turn_left(self):
        self.dir = self.directions[ ( self.directions.index(self.dir) - 1 ) % len(self.directions) ]

    def turn_right(self):
        self.dir = self.directions[ ( self.directions.index(self.dir) + 1 ) % len(self.directions) ]

    def turn_around(self):
        self.dir = self.directions[ ( self.directions.index(self.dir) + 2 ) % len(self.directions) ]

    def move(self):
        new_x = self.x + self.movement[self.dir][0]
        new_y = self.y + self.movement[self.dir][1]

        if new_x != first_vehicle_x or new_y != first_vehicle_y:
            if new_x in xrange(self.grid_max_x+1):
                self.x = new_x
            if new_y in xrange(self.grid_max_y+1):
                self.y = new_y

def collect_user_info():

    GRID_MAX_X, GRID_MAX_Y = map(int, raw_input().split())

    vehicle_one_pos = raw_input().split()
    vehicle_one_commands = raw_input()

    vehicle_two_pos = raw_input().split()
    vehicle_two_commands = raw_input()

    return GRID_MAX_X, GRID_MAX_Y, vehicle_one_pos, vehicle_one_commands, vehicle_two_pos, vehicle_two_commands

def main():

    commands = {'L': 'turn_left', 'R': 'turn_right', 'M': 'move', 'T': 'turn_around'}

    (GRID_MAX_X,
    GRID_MAX_Y,
    vehicle_one_pos,
    vehicle_one_commands,
    vehicle_two_pos,
    vehicle_two_commands) = collect_user_info()

    # The next few lines are repeats and should be fixed but ... reasons ...
    vehicle_one = Vehicle(int(vehicle_one_pos[0]), int(vehicle_one_pos[1]), vehicle_one_pos[2], (GRID_MAX_X, GRID_MAX_Y))
    for command in vehicle_one_commands:
        eval("vehicle_one.{0}()".format(commands[command]))

    vehicle_two = Vehicle(int(vehicle_two_pos[0]), int(vehicle_two_pos[1]), vehicle_two_pos[2], (GRID_MAX_X, GRID_MAX_Y))
    for command in vehicle_two_commands:
        eval("vehicle_two.{0}()".format(commands[command]))

    print vehicle_one.x, vehicle_one.y, vehicle_one.dir
    print vehicle_two.x, vehicle_two.y, vehicle_two.dir

if __name__ == "__main__":
    main()
