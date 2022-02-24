RUN clone https://github.com/WorkerUB001/WorkerUB002.git /root/userbot

WORKDIR /root/userbot

RUN pip3 install -U -r requirements.txt

ENV PATH="/home/userbot/bin:$PATH"

CMD ["python3", "-m", "userbot"]
