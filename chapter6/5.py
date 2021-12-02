strung ='X-DSPAM-Confidence:0.8475'
slicenum = strung.find(":")
print(float(strung[slicenum+1:]))
