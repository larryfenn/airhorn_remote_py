docker run -itd \
       --name=airhorn \
       -p 42069:42069/tcp \
       -v /root/airhorn:/airhorn \
       --restart unless-stopped \
       airhorn:latest
