FROM python:3.11-alpine
LABEL org="qtdevops" author="venkat"
ARG USERNAME=venkat
RUN adduser -D -h /apps -s /bin/bash ${USERNAME}
COPY --chown=${USERNAME}:${USERNAME} . /apps
WORKDIR /apps
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]