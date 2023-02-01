
# Let us define a one dimensional board in which an agent must reach the end. This board will contain no obstructions
# and will always have a solution. The count of actions will determine the strength of success. We begin with a 1x5
# initialized with values as such (this will be randomized later):

# Board values
# 0 - clear
# 1 - obstruction
# 2 - target

value_board = [[0],[0],[0],[2],[0]]
safe_board = [[],[],[],[],[]]
visited_board = [[],[],[],[],[]]
curr_pos_board = [[],[],[],[],[]]

# The agent can perform the following actions
# 1 - move forward
# 2 - move backward
# 3 - climb out (conclude)

# The percepts passed will be as such
# [0,0,0,0] -> [Position (Location), Safe (State), Target (State), Wall (State]

class Agent():
    def __init__(self, initial_percept):
        self.curr_percept = initial_percept
        self.position = self.curr_percept[0]
        curr_pos_board[self.position].append("~")
        visited_board[self.position].append("X")
        self.get_boards()
        self.check_safety()

    def check_safety(self):
        if (self.curr_percept[1] == 1):
            if not safe_board[self.position]:
                safe_board[self.position].append(0)
            self.action = int(input("Enter a move: "))
            self.curr_percept = [int(item) for item in input("Enter the list items: ").split()]
            self.move(self.action, self.curr_percept)
        else:
            print("Not Safe")

    def move(self, action, percept):
        if action == 1:
            curr_pos_board[self.position].clear()
            self.position = self.position + 1
            curr_pos_board[self.position].append("~")
            if not visited_board[self.position]:
                visited_board[self.position].append("X")
            self.get_boards()
            self.check_safety()
        elif action == 2:
            curr_pos_board[self.position].clear()
            self.position = self.position - 1
            curr_pos_board[self.position].append("~")
            if not visited_board[self.position]:
                visited_board[self.position].append("X")
            self.get_boards()
            self.check_safety()
        elif action == 3:
            if percept[3] == 1:
                print("Climbed out at target")
            else:
                print("Climbed out at wrong position")

    def get_boards(self):
        print("Current Position: " + str(curr_pos_board))
        print("Visited Board: " + str(visited_board))
        print("Safe Board: " + str(safe_board))


D_agent = Agent([0,1,0,0])

