FROM python:3.9
WORKDIR /foodies-only
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
CMD [ "python", "src/app.py" ]