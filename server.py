import time
import grpc
from concurrent import futures
import sys

sys.path.append("/usr/app/autogen")
import helloworld_pb2
import helloworld_pb2_grpc

class GreeterServicer(helloworld_pb2_grpc.GreeterServicer):

    def SayHello(self, request, context):
        print('Receive new message! [name: {}]'.format(request.name))
        return helloworld_pb2.HelloReply(message='Nice to meet you!!! {}'.format(request.name))

def serve():
    print("Server launched...")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    helloworld_pb2_grpc.add_GreeterServicer_to_server(GreeterServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print('Starting gRPC sample server...')
    try:
        while True:
            time.sleep(3600)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()