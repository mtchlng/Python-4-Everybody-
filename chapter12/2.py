# Exercise 2: Change your socket program so that it
#counts the number of characters it has received
#stops displaying any text after it has shown 3000 characters.
#retrieve the entire document
#count the total number of characters and display the count at the end of the document.

import socket
try:
    myurl = input("Enter URL: ")
    if len(myurl) < 1: myurl = "http://data.pr4e.org/intro-short.txt"
    host = myurl.split('/')[2]

    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((host, 80))
    cmd = ('GET ' + myurl + ' HTTP/1.0\r\n\r\n').encode()
    mysock.send(cmd)

    received = b""
    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break
        received += data #Adds data to received


    received = received.decode() #Decodes received, prepares is for our device
    print(received[:3000]) #Prints the first 3000 characters of received
    print(len(received)) #Counts and displays the count 


    mysock.close()

except:
    print("Invalid URL")
    quit()
