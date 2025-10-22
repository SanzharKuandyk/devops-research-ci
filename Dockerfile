FROM python:3.9
WORKDIR /app
COPY . .
RUN pip install pandas
CMD ["python", "main.py"]
