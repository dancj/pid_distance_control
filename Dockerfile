# this file sets up container to run my python app on an RPi,
# installing all the depencies and everything

# python base image for my RPi
# model name	: ARMv6-compatible processor rev 7 (v6l)
# https://github.com/docker-library/official-images#architectures-other-than-amd64
FROM arm32v6/python:3

COPY src/ .
COPY requirements.txt .

# set up virtual environment and install dependencies
RUN sudo apt install python3-venv -Y
RUN python3 -m venv venv
RUN source venv/bin/activate
RUN pip install --no-cache-dir -r requirements.txt
RUN sudo apt install pigpiod -Y

# run the Python script
CMD ["python", "./src/run.py"]
