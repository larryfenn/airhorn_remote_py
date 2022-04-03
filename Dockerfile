FROM python:3.10.1
EXPOSE 42069/tcp
CMD ln -sf /usr/share/zoneinfo/America/New_York /etc/localtime && \
cd airhorn && \
python airhorn.py
