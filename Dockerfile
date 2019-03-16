FROM python:3

ADD  CNN/predict.py /
ADD  CNN/predict.py /
ADD  AMAZON_REKOGNITION/amazon_rekog.py /
ADD  MICROSOFT_VISION/azure_object_detect.py /
ADD  MICROSOFT_VISION/ObjectAPIConfig.py /

RUN pip install Pillow
RUN pip install boto3
RUN pip install matplotlib
RUN pip install opencv_python
RUN pip install requests
RUN pip install tensorflow



#CMD [ "python", "GUI.PY" ]
#Successfully built f48f8cff9806