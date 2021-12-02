import socket
try:
    myurl = input("Enter URL: ")
    if len(myurl) < 1: myurl = "http://data.pr4e.org/intro-short.txt"
    host = myurl.split('/')[2]

    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((host, 80))
    cmd = ('GET ' + myurl + ' HTTP/1.0\r\n\r\n').encode()
    mysock.send(cmd)

    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break
        print(data.decode(),end='')

    mysock.close()

except:
    print("Invalid URL")
    quit()
