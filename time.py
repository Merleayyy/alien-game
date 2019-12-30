import time
lo = time.localtime(time.time())
print(lo.tm_sec)
lol = time.localtime(time.time())
lol = time.strftime('%S', lol)
print(lol)
temp = int(lol)

print(temp)