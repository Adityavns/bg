FROM ubuntu:20.04


FROM python:3.9
COPY . /app
WORKDIR /app
RUN pip install --upgrade pip
# RUN pip install torch===1.4.0 torchvision===0.5.0 -f https://download.pytorch.org/whl/torch_stable.html
RUN pip install -r requirements.txt
EXPOSE 5000
ENTRYPOINT [ "python" ]
CMD [ "main.py" ]