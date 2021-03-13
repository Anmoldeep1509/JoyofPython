d = 'a'
op = 0
for i in range(2):
    # d = d + 1 
    # gives error, solve by
    d = ord(d) + 1 
    d = chr(d)
    print(d)