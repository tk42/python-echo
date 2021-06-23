import time
import grpc
import sys

sys.path.append("/usr/app/autogen")
import helloworld_pb2
import helloworld_pb2_grpc


def run():
    name_list = ["violet", "iris", "cattleya", "erica", "rax"]

    channel = grpc.insecure_channel('server:50051')
    stub = helloworld_pb2_grpc.GreeterStub(channel)
        
    for name in name_list:
        message = helloworld_pb2.HelloRequest(name=name)
        response = stub.SayHello(message)
        print('Received message {}'.format(response.message))

        time.sleep(1)

    print('finished!')

if __name__ == '__main__':
    run()