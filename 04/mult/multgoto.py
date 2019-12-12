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

@0
M=2
@1
M=5
@2
M=0
(LOOP)
@0
D=M
@END
D;JLE

@0
D=M
@2
M=M+D
@1
M=M-1
@LOOP
0;JMP
(END)
@END
0;JMP