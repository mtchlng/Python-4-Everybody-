# Exercise 3: Use urllib to replicate the previous exercise of
#(1) retrieving the document from a URL,
#(2) displaying up to 3000 characters, and
#(3) counting the overall number of characters in the document.
#Don’t worry about the headers for this exercise, simply show the first 3000 characters of the document contents.


import urllib.request, urllib.parse, urllib.error

try:
    myurl = input("Enter URL: ")
    if len(myurl) < 1: myurl = "http://data.pr4e.org/intro-short.txt"

    fhand = urllib.request.urlopen(myurl).read()
    fhand = fhand.decode()

    print(fhand[:3000])
    print(len(content))



except:
    print("Invalid URL")
    quit()
