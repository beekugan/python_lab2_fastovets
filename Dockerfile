FROM python:3.12-slim  

WORKDIR /app  

RUN pip install googletrans==3.1.0a0  

CMD ["bash"]
