import grpc
from concurrent import futures
from grpc_robot import robot_pb2_grpc
from robot import service_robot

def server_robot():
    # print("a")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    robot_pb2_grpc.add_RobotServicer_to_server(service_robot.RobotServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()
    