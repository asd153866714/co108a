from goto import with_goto
 
@with_goto

def test():
    r0 = 2
    r1 = 5
    r2 = 0
    label .LOOP
    if (r1<=0):
        goto .END
    r2 += r0
    r1 -= 1
    goto .LOOP 
    label .END
    print(r2)

test()

