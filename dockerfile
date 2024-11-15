FROM ubuntu:latest

RUN apt-get update && \
    apt-get install -y python3 python3-pip python3-venv

RUN python3 -m venv /opt/venv

ENV PATH="/opt/venv/bin:$PATH"

RUN pip install --upgrade pip && \
    pip install pandas numpy seaborn matplotlib scikit-learn scipy

RUN mkdir -p /home/doc-bd-a1/


COPY SVMtrain.csv /home/doc-bd-a1/
COPY dpre.py /home/doc-bd-a1/
COPY eda.py /home/doc-bd-a1/
COPY load.py /home/doc-bd-a1/
COPY model.py /home/doc-bd-a1/
COPY vis.py /home/doc-bd-a1/
COPY final.sh /home/doc-bd-a1/


CMD ["bash"]