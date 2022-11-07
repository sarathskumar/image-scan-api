FROM python:3.8-alpine
RUN apk add curl
RUN curl -sfL https://raw.githubusercontent.com/aquasecurity/trivy/main/contrib/install.sh | sh -s -- -b /usr/local/bin v0.32.1
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
COPY . /app
RUN chmod +x /app/start.sh
EXPOSE 5000
CMD ["sh","/app/start.sh" ]

