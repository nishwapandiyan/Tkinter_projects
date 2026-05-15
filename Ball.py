class Ball:
    
    def __init__(self, canvas, x, y, diameter, xVelocity, yVelocity, color):
        self.canvas = canvas
        self.my_image = canvas.create_oval(x,y,diameter,diameter,fill=color)
        self.xVel = xVelocity
        self.yVel = yVelocity
        
    def move(self):
            
        coordinates = self.canvas.coords(self.my_image)
        # print(coordinates)
        
        if(coordinates[2] >=(self.canvas.winfo_width()) or coordinates[0] < 0):
            self.xVel = -self.xVel
            
        if(coordinates[3] >=(self.canvas.winfo_height()) or coordinates[1] < 0):
            self.yVel = -self.yVel            
            
        self.canvas.move(self.my_image,self.xVel,self.yVel)    