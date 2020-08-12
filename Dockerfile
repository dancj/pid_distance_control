# this file sets up container to run my python app on an RPi,
# installing all the depencies and everything

# python base image for my RPi
# https://github.com/docker-library/official-images#architectures-other-than-amd64
FROM arm32v7/python

COPY src/ ./
COPY requirements.txt ./

# set up virtual environment and install dependencies
RUN source venv/bin/activate
RUN pip install -r requirements.txt


# run the Python script
CMD ["python", "./src/run.py"]
