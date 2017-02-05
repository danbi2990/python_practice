# class Robot:
#     __counter = 0
    
#     def __init__(self):
#         type(self).__counter += 1
        
#     def RobotInstances():     We can't call it via an instance.
#         return Robot.__counter



class Robot:
    __counter = 0
    
    def __init__(self):
        type(self).__counter += 1
        
    @staticmethod
    def RobotInstances():
        return Robot.__counter
        

if __name__ == "__main__":
    print(Robot.RobotInstances())
    x = Robot()
    print(x.RobotInstances())
    y = Robot()
    print(x.RobotInstances())
    print(Robot.RobotInstances())
