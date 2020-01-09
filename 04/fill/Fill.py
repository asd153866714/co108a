arr = SCREEN
n = 8192
i = 0 

while i<n:

    if *KBD != 0:
        arr[i] = -1
    else:
        arr[i] = 0
    i += 1

