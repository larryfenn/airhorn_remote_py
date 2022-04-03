import socket
from datetime import datetime
import time
while True:
    lastseen = time.time()
    curtime = time.time()
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.bind(('0.0.0.0', 42069))
            while True:
                s.listen(0)
                curtime = time.time()
                with s.accept()[0] as conn:
                    if curtime - lastseen >= 1:
                        # write to the log here
                        ip = conn.getpeername()[0]
                        log_string = f'{ip}\t{datetime.now().strftime("%m/%d/%Y %H:%M:%S")}'
                        print(log_string)
                        with open("airhornlog.txt", "a") as f:
                            f.write(log_string)
                            f.write("\n")
                            lastseen = curtime
    except Exception as e:
        print(e)
