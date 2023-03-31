
# old version (cuda 11.0)
# FROM nvcr.io/nvidia/pytorch:20.09-py3
# RUN pip install --use-feature=2020-resolver torch==1.8.0 torchvision==0.9.0 torchaudio==0.8.0
# RUN pip install mxnet-cu110

# cuda 11.2
FROM nvcr.io/nvidia/pytorch:21.03-py3

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y tzdata

ENV TZ=Asia/Tokyo 

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y \
    git 

RUN apt-get update \
    && apt-get install -y g++ cmake libopencv-dev

# RUN pip install --use-feature=2020-resolver torch==1.8.0 torchvision==0.9.0 torchaudio==0.8.0
RUN pip install mediapipe
# RUN apt-get install python3-dev && python3-venv && apt install -y protobuf-compiler \
#     apt-get install cmake

