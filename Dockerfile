FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

# Add user
#RUN useradd -ms /bin/bash ombori
#USER ombori
RUN mkdir /home/ombori
WORKDIR /home/ombori

# This fix: libGL error: No matching fbConfigs or visuals found
ENV LIBGL_ALWAYS_INDIRECT=1

# Install Python 3
RUN apt-get update && apt-get install -y python3

# Install pip3
RUN apt-get -y install python3-pip

#RUN pip3 install --upgrade pip

RUN apt-get update

#for ERR: ImportError: libGL.so.1: cannot open shared object file: No such file or directory
RUN apt-get install ffmpeg libsm6 libxext6  -y

# for ERR: missig qt platform libraries(found with ldd)
RUN apt-get install libxcb-icccm4 libxcb-image0 libxcb-util1 libxcb-keysyms1 libxcb-render-util0 libxcb-xinerama0 libxcb-xkb1 libxkbcommon-x11-0 -y

ENV XDG_RUNTIME_DIR=/tmp/runtime-root

# copy the dependencies file to the working directory
COPY requirements.txt .

# install dependencies
RUN pip install -r requirements.txt

RUN apt-get update

# copy the content of the local src directory to the working directory
COPY . /home/ombori

# command to run on container start
CMD [ "python3", "./app.py" ]