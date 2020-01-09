from goto import with_goto

@with_goto

def test():
    arr = SCREEN
    n = 8192
    i = 0 

    label .FOREVER
    label .LOOP
    if (i == n): 
        goto .END

    if (*KBD !=0 ):
        RAM[arr + i] = -1
    else:
        RAM[arr + i] = 0

    i += 1

    goto .LOOP
    
    label .END:
    goto .FOREVER
