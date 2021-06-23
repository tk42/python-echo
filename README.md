# python-echo
This repository is a sample application implemented a gRPC echo-server with python

you can compare this repo to [golang-echo version](https://github.com/tk42/golang-echo)

## How to work
```
docker compose up server client
```
Then you can see...
```
Attaching to e7808aeb8bb4_python-echo-server, python-echo-client
python-echo-client               | Received message Nice to meet you!!! violet
python-echo-client               | Received message Nice to meet you!!! iris
python-echo-client               | Received message Nice to meet you!!! cattleya
python-echo-client               | Received message Nice to meet you!!! erica
python-echo-client               | Received message Nice to meet you!!! rax
python-echo-client               | finished!
python-echo-client exited with code 0
```

## How to rebuild from .proto file
```
docker compose up protoc
```

## Reference
 - [flavienbwk/gRPC-Python-Docker-Example](https://github.com/flavienbwk/gRPC-Python-Docker-Example)
 - [gRPCとProtocol Buffersによるアプリケーション間通信 / Python](https://note.com/npaka/n/n5c3263ad88ff#zpdTp)
 - [PythonでgRPCで双方向通信を試す。](https://qiita.com/ike_dai/items/1a28f6a42c4a0d3a49d0)