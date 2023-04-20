# base image
FROM python:3.9-alpine

RUN apk add --no-cache gcc musl-dev linux-headers

# put requirements from /app/requirements.txt and install it as well
COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

# copy the code from local machine to container as well
COPY receive.py /app/receive.py
COPY send.py /app/send.py

# CMD ["python", "/app/receive.py"]
CMD python /app/receive.py && python /app/send.py
