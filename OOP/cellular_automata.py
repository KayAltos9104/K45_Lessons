class CellularAutomata():
    def __init__(self, width):
        self.initialize_field(width)
        self.width = width
        self.iteration = 1

    def initialize_field(self, width):    
        self.field = [[0]*width]*1
        self.field[0][width//2] = 1

    def update_field(self):
        self.field.append([0]*self.width)
        for x in range (len(self.field[self.iteration])):

            if (x-1<0):
                left  = 0
            else:
                left = self.field[self.iteration-1][x-1]
            if x+1 >=len(self.field[self.iteration]):
                right = 0
            else:
                right = self.field[self.iteration-1][x+1]           

            center = self.field[self.iteration-1][x]
            self.field[self.iteration][x] = self.calc_state(left, center, right)
        self.iteration +=1

    def calc_state(self, left, center, right):    
        if left == 1 and center == 1 and right == 1:
            return 0
        if left == 1 and center == 1 and right == 0:
            return 0
        if left == 1 and center == 0 and right == 1:
            return 0
        if left == 1 and center == 0 and right == 0:
            return 1
        if left == 0 and center == 1 and right == 1:
            return 1
        if left == 0 and center == 1 and right == 0:
            return 1
        if left == 0 and center == 0 and right == 1:
            return 1
        if left == 0 and center == 0 and right == 0:
            return 0
  
    
   
    
    











