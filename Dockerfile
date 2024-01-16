# base image
FROM python:3.10-slim-buster

# 환경변수 설정
ENV PYTHONUNBUFFERED=1
ENV ENVIRONMENT="dev"
ENV USER="admin"
ENV DB_HOST="bud-db-1.c6kvxbytk32d.ap-northeast-2.rds.amazonaws.com"
ENV HOST="52.78.44.118"

# 작업 디렉토리 생성 및 설정
RUN mkdir /app
WORKDIR /app

# requirements 파일 복사
COPY requirements.txt /app/


RUN apt-get update && \
    apt-get install -y default-libmysqlclient-dev pkg-config gcc

# requirements 설치
RUN pip install -r requirements.txt

# app 파일 복사
COPY . /app/

# 컨테이너 시작시 실행할 명령어
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000"]
