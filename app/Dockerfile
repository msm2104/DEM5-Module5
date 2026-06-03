FROM python:3.12-slim
WORKDIR /run
COPY . .
RUN pip install -r requirements.txt
ENTRYPOINT ["python3","my_lib_data_cleaning.py"]