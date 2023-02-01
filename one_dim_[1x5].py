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

# We track all percepts given as sensory data in a memory list
memory = []

# The agent can perform the following actions
# 1 - move forward
# 2 - move backward
# 3 - climb out (conclude)

# The percepts passed will be as such
# [0,0,0,0] -> [Position (Location), Safe (State), Target (State), Wall (State)]

# Position -> [0,4]
# Safe -> [0,1]
# Target -> [0,1]
# Wall -> [0,2]

# The percept class that reads the environment around the agent
class FormPercept():
    def __init__(self):
        self.pos = 0
        self.target_status = 0
        self.wall_status = 0
        self.safe_status = 0
        self.create_percept()

    def create_percept(self):
        if value_board[self.pos][0] == 0:
            self.safe_status = 1
            self.target_status = 0
        elif value_board[self.pos][0] == 1:
            self.safe_status = 0
            self.target_status = 0
        elif value_board[self.pos][0] == 2:
            self.safe_status = 1
            self.target_status = 1

        if self.pos + 1 == 5:
            self.wall_status = 1
        elif self.pos - 1 == -1:
            self.wall_status = 2
        else:
            self.wall_status = 0
        self.percept = [self.pos, self.safe_status, self.target_status, self.wall_status]
        memory.append(self.percept)

        print("-------------------------------------------------")
        print("Agent's percept memory: " + str(memory))

    def get_precept(self):
        self.create_percept()
        return self.percept

    def change_position(self, action):
        if action == 1:
            if self.wall_status != 1:
                self.pos = self.pos + 1
        elif action == 2:
            if self.wall_status != 2:
                self.pos = self.pos - 1

# The agent class where the behaviors of the agent are defined. Board representation also allocated here
class Agent():
    def __init__(self, memory):
        self.percept_memory = memory
        self.curr_percept = self.percept_memory.percept
        self.position = self.curr_percept[0]
        curr_pos_board[self.position].append("~")
        visited_board[self.position].append("X")
        safe_board[self.position].append(0)
        self.get_boards()
        self.check_safety()

    def check_safety(self):
        if (self.curr_percept[1] == 1):
            try:
                if not safe_board[self.position]:
                    safe_board[self.position].append(0)
                self.action = int(input("Enter a move: "))
                self.percept_memory.change_position(self.action)
                self.curr_percept = self.percept_memory.get_precept()
                self.move(self.action, self.curr_percept)
            except:
                self.action = int(input("Enter a move: "))
                self.percept_memory.change_position(self.action)
                self.curr_percept = self.percept_memory.get_precept()
                self.move(self.action, self.curr_percept)
        else:
            print("Not Safe, Mission Failed")

    def move(self, action, percept):
        if action == 1:
            try:
                curr_pos_board[self.position].clear()
                self.position = self.position + 1
                curr_pos_board[self.position].append("~")
                if not visited_board[self.position]:
                    visited_board[self.position].append("X")
                self.get_boards()
                self.check_safety()
                self.percept_memory.change_position(action)
            except:
                print("Right bound reached. Cannot move forward")
                self.check_safety()

        elif action == 2:
            try:
                if self.position < 0:
                    curr_pos_board[self.position].clear()
                    self.position = self.position - 1
                    curr_pos_board[self.position].append("~")
                    if not visited_board[self.position]:
                        visited_board[self.position].append("X")
                self.get_boards()
                self.check_safety()
                self.percept_memory.change_position(action)
            except:
                print("Right bound reached. Cannot move backward")
                self.check_safety()

        elif action == 3:
            if percept[2] == 1:
                print("Climbed out at target")
            else:
                print("Climbed out at wrong position")
            self.percept_memory.change_position(action)


    def get_boards(self):
        print("-------------------------------------------------")
        print("Current Position: " + str(curr_pos_board))
        print("Visited Board: " + str(visited_board))
        print("Safe Board: " + str(safe_board))
        print("-------------------------------------------------")

D_agent_memory = FormPercept()
D_agent = Agent(D_agent_memory)

# Improvements to be made:
# 1. Not input based
# 2. Passing a function of actions to the agent behavior class
# 3. Cleaner representation of the board and corresponding moves
# 4. Simple reflex agent to a different agent model?


