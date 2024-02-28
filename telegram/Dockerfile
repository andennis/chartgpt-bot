FROM python:3.10
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
COPY chatgpt_bot.py /app
CMD ["python", "./chatgpt_bot.py"]