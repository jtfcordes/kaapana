FROM python:3.9-alpine3.12

LABEL IMAGE="example-extract-study-id"
LABEL VERSION="0.1.0"
LABEL CI_IGNORE="True"

COPY files/requirements.txt /src/
RUN pip3 install -r /src/requirements.txt

COPY files/extract_study_id.py /

CMD ["python3","-u","/extract_study_id.py"]