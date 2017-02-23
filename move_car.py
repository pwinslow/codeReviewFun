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

directions = ['N','E','S','W']
movement = {'N': (0,1), 'E': (1,0), 'S': (0,-1), 'W':(-1,0)}
commands = {'L': 'turn_left', 'R': 'turn_right', 'M': 'move'}

GRID_MAX_X, GRID_MAX_Y = map(int, raw_input().split())

# You define first_vehicle_x/y here and then don't use them until you redefine them on lines 55+56.
# Why not just define them once on 55+56?
first_vehicle_x = None
first_vehicle_y = None

class Vehicle():
    def __init__(self, x, y, face):
        self.x = x
        self.y = y
        self.dir = face

    # The code in both turn_ methods is pretty bunched up and thus hard to read
    def turn_left(self):
        self.dir = directions[(directions.index(self.dir)-1)%len(directions)]

    def turn_right(self):
        self.dir = directions[(directions.index(self.dir)+1)%len(directions)]

    def move(self):
        new_x = self.x + movement[self.dir][0]
        new_y = self.y + movement[self.dir][1]

        # I can see my way through this but I kind of have to squint. This looks like the
        # "code smell" issue that AJ mentioned...
        if new_x != first_vehicle_x or new_y != first_vehicle_y:
            if new_x in xrange(GRID_MAX_X+1):
                self.x = new_x
            if new_y in xrange(GRID_MAX_Y+1):
                self.y = new_y

vehicle_one_pos = raw_input().split()
vehicle_one_commands = raw_input()

# Be more explicit in terms of what you're passing here, i.e., don't pass elements of a list, pass variables
# key-values pairs with a inputs** after making it clear what inputs is
vehicle_one = Vehicle(int(vehicle_one_pos[0]), int(vehicle_one_pos[1]), vehicle_one_pos[2])
for command in vehicle_one_commands:
    eval("vehicle_one.{0}()".format(commands[command]))

# These two variables are defined twice but never used
first_vehicle_x = vehicle_one.x
first_vehicle_y = vehicle_one.y


vehicle_two_pos = raw_input().split()
vehicle_two_commands = raw_input()

vehicle_two = Vehicle(int(vehicle_two_pos[0]), int(vehicle_two_pos[1]), vehicle_two_ps[2])
for command in vehicle_two_commands:
    eval("vehicle_two.{0}()".format(commands[command]))

# The last 25 lines or so contains an unnecessary repetition. Should design a function


# These print statements are also a repetition. Make a function...
print vehicle_one.x, vehicle_one.y, vehicle_one.dir
print vehicle_two.x, vehicle_two.y, vehicle_two.dir
