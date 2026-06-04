FROM python:3.12-slim
WORKDIR /app
COPY sender.py /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python3", "sender.py"]

# Task: Create new docker container using our calculator.py 
# to calculate 144/12 when the container runs.

# COMMANDS:
# docker build -t name .
# docker run name