from grpc_robot import robot_pb2_grpc, robot_pb2
from robot.control_robot import ControlRobot 


class RobotServicer(robot_pb2_grpc.RobotServicer, ControlRobot):
    def __init__(self):
        super().__init__()
        
    def Connect(self, request, context):
        self.robot_ip = request.ip
        return robot_pb2.StateResponse(state=self.rb_connect())
    
    def Disconnect(self, request, context):
        return robot_pb2.StateResponse(state=self.rb_disconnect())
    
    def RunBuffMidsole(self, request, context):
        return robot_pb2.StateResponse(state=self.runBuffMidsole(request.pos, request.dir))
    
    def PowerOn(self, request, context):
        return robot_pb2.StateResponse(state=self.powerOn())

    def PowerOff(self, request, context):
        return robot_pb2.StateResponse(state=self.powerOff())
    
    def Enable(self, request, context):
        return robot_pb2.StateResponse(state=self.enableRobot())
    
    def Disable(self, request, context):
        return robot_pb2.StateResponse(state=self.disableRobot())
    
    def Shutdown(self, request, context):
        return robot_pb2.StateResponse(state=self.shutdown())
    
    def Pause(self, request, context):
        return robot_pb2.StateResponse(state=self.pauseMove())
    
    def Resume(self, request, context):
        return robot_pb2.StateResponse(state=self.resumeMove())
    
    def Stop(self, request, context):
        return robot_pb2.StateResponse(state=self.stopMove())
    
    def MoveHome(self, request, context):
        return robot_pb2.StateResponse(state=self.robot_home())
    
    def Shutdown(self, request, context):
        return robot_pb2.StateResponse(state=self.shutdown())
    
    def LoadProgram(self, request, context):
        state, nameProgram = self.loadProgram(request.nameProgram)
        return robot_pb2.LoadProgramResponse(state=state, nameProgram= nameProgram)
    
    def RunProgram(self, request, context):
        return robot_pb2.StateResponse(state=self.runProgram())
    
    def MoveTCP(self, request, context):
        return robot_pb2.StateResponse(state=self.moveTCP(request.pos))
    
    def SetIO(self, request, context):
        return robot_pb2.StateResponse(state=self.setIO(request.pin, request.ioState))
    
    def GetProgramState(self, request, context):
        state, programState = self.get_program_state()
        return robot_pb2.ProgramStateResponse(state=state, programState= programState)
    
    def Abortprogram(self, request, context):
        return robot_pb2.StateResponse(state=self.program_abort())
    
    def GetPos(self, request, context):
        state, pos = self.currentPos()
        return robot_pb2.PosResponse(state=state, pos=pos)
    
    def SetToolId(self, request, context):
        return robot_pb2.StateResponse(state= self.set_tool_id(request.toolId))
    
    def GetToolId(self, request, context):
        state, toolId = self.get_tool_id()
        return robot_pb2.ToolIdResponse(state=state, toolId=toolId)
    
    def SetCoordinateId(self, request, context):
        return robot_pb2.StateResponse(state= self.set_user_coordinate_id(request.coordinateId))
    
    def GetCoordinateId(self, request, context):
        state, coordinateId = self.get_user_coordinate_id()
        return robot_pb2.ToolIdResponse(state=state, toolId=coordinateId)