FROM python:3.7.9
LABEL maintainer_name="Omar Magdy"
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
EXPOSE 80
CMD ["python", "app.py"]