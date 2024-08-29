import grpc
from grpc_robot import robot_pb2, robot_pb2_grpc


def client_test():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = robot_pb2_grpc.RobotStub(channel)
        # test connect
        response = stub.Connect(robot_pb2.ConnectRequest(ip="192.138.1.1"))
    print(f"Result: {response.state}")


if __name__ == '__main__':
    client_test()