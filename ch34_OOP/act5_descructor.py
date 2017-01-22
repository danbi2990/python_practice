class Robot():
    
    def __init__(self, name):
        self.name = name
        print(name + " has been created!")
        
    def __del__(self):
        print (self.name + " has been destroyed")
        
if __name__ == "__main__":
    x = Robot("X")
    y = Robot("Y")
    z = x

    print("Deleting x")
    del x

    print("Deleting z")
    del z
    
    del y
