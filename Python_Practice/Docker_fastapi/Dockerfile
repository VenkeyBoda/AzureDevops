FROM python:3.11-alpine AS build
# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /apps
# COPY requirements.txt .
RUN pip pip install -r requirements.txt

FROM python:3.11-alpine AS RUN
LABEL org="lti" author="venkat"
ARG USERNAME=venkat
RUN adduser -D -h /apps -s /bin/bash ${USERNAME}
COPY --from=build --chown=${USERNAME}:${USERNAME} . /apps
WORKDIR /apps
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]