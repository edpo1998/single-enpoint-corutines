FROM python:3.9
WORKDIR /app
COPY . .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r ./requirements/dev.txt
RUN pip install gunicorn
EXPOSE 8000
# CMD [ "gunicorn", "-w", "2", "--bind", "0.0.0.0:8000", "app:app" ]
CMD [ "python", "app.py" ]
