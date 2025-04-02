#사용자정의 함수
def rep_char(c,n):
    print(c*n)


def draw_line_string(prompt):
    msg1=f'Hello {prompt},'
    msg2=('Welcome to Seoul.')
    nstr = len(msg1) if (len(msg1) > len(msg2)) else len(msg2)
    rep_char('-',nstr+1)
    print(msg1)
    print(msg2)
    rep_char('-',nstr+1)

#주프로그램부===================================

name=input('Input his/her name:')
draw_line_string(name)