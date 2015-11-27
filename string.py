text = "X-DSPAM-Confidence:    0.8475";
dp=text.find('.');
num=text[23:]
fnum=float(num)
print fnum