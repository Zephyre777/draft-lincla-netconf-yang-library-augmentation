#! /bin/bash

docker build --build-arg HTTP_PROXY=$HTTP_PROXY --build-arg HTTPS_PROXY=$HTTPS_PROXY --build-arg http_proxy=$http_proxy --build-arg https_proxy=$https_proxy --network host -t netopeer2-augmentedby .