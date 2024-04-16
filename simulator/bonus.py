def rst():
    d=dict.fromkeys(d.keys(),"0"*32)
def halt():
    pass
    #jaldi banado
    
def reverse(rs,rd,d):
    d[rs]=d[rd][::-1]
def check(s,d,pc):
    if s[0:6]=='111111':
        rst()
    elif s[0:6]=='000000':
        halt()
    elif s[0:6]=='101010':
        d=reverse(s[7:12],s[12:17],d)
        return d
