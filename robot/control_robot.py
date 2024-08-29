from robot.libjaka import jkrc
import math
import time

scale = math.pi/180

STOP = 0
RUN = 1
PAUSE = 2

# return values
ERR_SUCC              = 0   #Success
ERR_INVALID_HANDLER   = -1  #An invalid handle
ERR_INVALID_PARAMETER = -2  #An invalid argument
ERR_COMMUNICATION_ERR = -3  #There was a communication error
ERR_KINE_INVERSE_ERR  = -4  #The reverse solution failed
ERR_EMERGENCY_PRESSED = -5  #The emergency stop key has not been releasedERR_NOT_POWERED -6 The robot is not powered on
ERR_NOT_ENABLED       = -7  #The robot is not enabled
ERR_DISABLE_SERVOMODE = -8  #SERVOMODE mode is not entered
ERR_NOT_OFF_ENABLE    = -9  #The power is not lowered before power is turnedoffERR_PROGRAM_IS_RUNNING -10 The program is running
ERR_CANNOT_OPEN_FILE  = -11 #Opening the file failed


class ControlRobot:
    def __init__(self):
        self.robot_ip = None
        self.robot_connect = False
        self.flag_maigiay = False
        self.flag_pause = False
        self.Zrobot = -25.0
        
        self.program_right = "FULL_RIGHT_NO_BUT"
        self.program_left = "FULL_LEFT_NO_BUT"
        
    def powerOn(self):
        robot = jkrc.RC(self.robot_ip)
        robot.login()
        ret,_ = robot.power_on()
        robot.logout()
        return ret

    def powerOff(self):
        robot = jkrc.RC(self.robot_ip)
        robot.login()
        ret,_ =robot.power_off()
        robot.logout()
        return ret

    def enableRobot(self):
        robot = jkrc.RC(self.robot_ip)
        robot.login()
        ret,_ = robot.enable_robot()
        robot.logout()
        return ret  
        
    def disableRobot(self):
        robot = jkrc.RC(self.robot_ip)
        robot.login()
        ret,_ = robot.disable_robot()
        robot.logout()
        return ret

    def shutdown(self):
        # Shutdown  nguồn tủ điện
        self.robot.login()
        ret = self.robot.shut_down()
        self.robot.logout()
        return ret

    def pauseMove(self):
        # Pause robot
        robot = jkrc.RC(self.robot_ip)
        robot.login()
        ret = robot.program_pause()
        robot.logout()
        print("Robot pause!")
        return ret

    def resumeMove(self):
        # Resume robot
        robot = jkrc.RC(self.robot_ip)
        robot.login()
        ret = robot.program_resume()
        robot.logout()
        print("Robot resume!")
        return ret

    def stopMove(self):
        # Stop robot
        self.robot.login()
        self.robot.program_abort() 
        self.robot.logout()

    def loadProgram(self, program):
        robot = jkrc.RC(self.robot_ip)
        robot.login()
        ret0 = robot.program_load(program)
        ret1 = robot.get_loaded_program()
        print("the loaded program is:",ret1[1])
        strCoffe = str(program)+".jks"
        if ret1[1] == strCoffe:
            print("Load Done!")
        else:
            print("Load Failed!")
        robot.logout()
        return ret0, ret1
        
    def runProgram(self):
        robot = jkrc.RC(self.robot_ip)
        # Start chương trình
        robot.login()
        ret = robot.program_run() # câu lệnh này sẽ start chương trình vừa được load ở trên 
        robot.logout()
        print("Robot run!")
        return ret
    
    def moveJoint(self,pos, vel):
        robot = jkrc.RC(self.robot_ip)
        # Điều khiển robot chuyển động theo dạng Joint Move
        # joint_angle = [0,0,0,0,0,0] # giá trị góc của 6 khớp quay mà mình muốn nó đạt được, đơn vị là rad
        # vel = 0.5 # đơn vị của tốc độ vel là rad/s
        robot.login()
        print("a")
        robot.joint_move(joint_pos=pos, move_mode=0,is_block=False, speed=vel)
        robot.get_joint_position()
        print("b")
        robot.logout()

    def moveTCP(self,end_pos,vel):
        robot = jkrc.RC(self.robot_ip)
        robot.login()
        ret = robot.get_tcp_position() 
        ret_end_pos = ret[1]
        ret = robot.linear_move(end_pos = end_pos ,move_mode = 0,is_block =False,speed = vel)
        print("the return value is:",ret)
        robot.logout()
        return ret
        
    def setIO(self,index, val):
        # Điều khiển IO Cabinet
        robot = jkrc.RC(self.robot_ip)
        robot.login()
        ret = robot.set_digital_output(iotype = 0, index = index, value = val)
        robot.logout()
        return ret
            
    def setTCP(self):
        # Set TCP
        self.robot.login()
        self.robot.set_tool_id(0)
        self.robot.logout()
        
    def rb_connect(self):
        
        ret_on = 1
        ret_en = 1
        while True:
            if ret_on != 0:
                try:
                    # print("11")
                    ret_on = self.powerOn()
                    print(ret_on)
                except ValueError as e:
                    print(f"Error: {e}")
                    # ret_on = 0

            if ret_en != 0 and ret_on == 0:
                try:
                    # print("22")
                    ret_en = self.enableRobot()
                    print(ret_en)
                except ValueError as a:
                    print(f"Error: {a}")
                    # ret_en = 0
                    
            if ret_on == 0 and ret_en == 0:
                ret = self.set_user_coordinate(10)
                print("Connected Robot!")
                self.robot_connect = True
                # break
                return ret
            
    def get_program_state(self):
        robot = jkrc.RC(self.robot_ip)
        robot.login()
        ret = robot.get_program_state()
        robot.logout()
        return ret
    
    def program_abort(self):
        robot = jkrc.RC(self.robot_ip)
        robot.login()
        ret = robot.program_abort()
        robot.logout()
        return ret
        
    def currentPos(self):
        robot = jkrc.RC(self.robot_ip)
        robot.login()
        ret = robot.get_tcp_position() 
        if ret[0] == 0:
            print("the tcp position is:",ret[1]) 
        else:
            print("some things happend,the errcode is: ",ret[0]) 
        robot.logout()
        return ret[1]
                        
    def set_user_coordinate(self, id):
        robot = jkrc.RC(self.robot_ip)
        robot.login()
        ret = robot.set_user_frame_id(id)
        robot.logout()
        return ret
        
    def is_in_pos(self): 
        robot = jkrc.RC(self.robot_ip)
        robot.login()
        _,ret = robot.is_in_pos()
        robot.logout()
        return ret
        
    def rb_disconnect(self):
        ret_dis = 1
        ret_off = 1
        while True:
            if ret_dis != 0:
                try:
                    print("11")
                    ret_dis = self.disableRobot()
                    print(ret_dis)
                except ValueError as e:
                    print(f"Error: {e}")
                    # ret_dis = 0

            if ret_off != 0:
                try:
                    print("22")
                    ret_off = self.powerOff()
                    print(ret_off)
                except ValueError as a:
                    print(f"Error: {a}")
                    # ret_off = 0
                    
            if ret_off == 0 and ret_dis == 0:
                print("Disconnect Robot!")
                self.robot_connect = False
                # break
                return 0

    def robot_home(self):
        home_pos = [-97.805, -433.033, 313.095, -179.511*scale, -2.120*scale, 1.350*scale]
        ret = self.moveTCP(home_pos,50)
        return ret

    def get_user_coordinate_id(self):
        robot = jkrc.RC(self.robot_ip)
        robot.login()
        ret = robot.get_user_frame_id()
        robot.logout()
        return ret[1]

    def get_tool_id(self):
        robot = jkrc.RC(self.robot_ip)
        robot.login()
        ret = robot.get_tool_id()
        robot.logout()
        return ret[1]
    
    def set_tool_id(self,id):
        robot = jkrc.RC(self.robot_ip)
        robot.login()
        ret = robot.set_tool_id(id)
        robot.logout()
        return ret[1]
    
    def set_user_coordinate_id(self,id):
        robot = jkrc.RC(self.robot_ip)
        robot.login()
        ret = robot.set_user_frame_id(id)
        robot.logout()
        return ret[1]

    def runBuffMidsole(self, pos,dir):
        (x,y) = pos[0]
        float(x)
        float(y)
        angle = float(pos[1])
        print(type(angle))
        end_pos = [float(x), float(y),float(self.Zrobot), float(180*scale), float(0*scale), float(angle*scale)]
        # if dir ==1:
        #     end_pos = [float(x), float(y),float(-25.9), float(180*scale), float(0*scale), float(angle*scale)]
        # else:
        #     end_pos = [float(x), float(y),float(-24), float(180*scale), float(0*scale), float(angle*scale)]
            
        mid_pos = [float(x), float(y),float(30.0), float(180*scale), float(0*scale), float(angle*scale)]
        home_pos = [-97.805, -433.033, 313.095, -179.511*scale, -2.120*scale, 1.350*scale]
        median_pos = [39.844, -174.340, 70.610, 180*scale, 0*scale, 0*scale]
        # if self.flag_maigiay:
        self.moveTCP(mid_pos,400)
        self.moveTCP(end_pos,50)

        while True:
            ret = self.currentPos()
            if ret[2] < float(self.Zrobot)+1:
                self.setIO(0,1)
                time.sleep(0.7)
                break

        self.moveTCP(mid_pos,200)
        self.moveTCP(median_pos,400)
        
        while True:
            ret = self.currentPos()
            print(ret[2])
            if ret[2] > 20:
                self.setIO(3,1)
                time.sleep(1.5)
                self.setIO(3,0)
                break
        
        if dir == 1:
            self.loadProgram(self.program_right)
        else:
            self.loadProgram(self.program_left)
        self.runProgram()
        while True:
            state_robot = self.get_program_state()# 0 stop, 1 run, 2 pause
            if state_robot == RUN and self.flag_pause:
                self.pauseMove()
            if state_robot == PAUSE and not self.flag_pause:
                self.resumeMove()
            if state_robot == STOP or  not self.flag_maigiay:
                # self.program_abort()
                # print("Chạy xong chương trình.")
                break
        self.program_abort()
        print("Chạy xong chương trình.")
        