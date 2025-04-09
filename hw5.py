def read_single_digit(n):
    intiger_korean=['영','일','이','삼','사','오','육','칠','팔','구']
    print(intiger_korean[n],end='',sep=" ")

def read_number(inti):
    length=len(inti)
    
    if length==3:
        read_single_digit(int(inti[0]))
        read_single_digit(int(inti[1]))
        read_single_digit(int(inti[2]))
    elif length==2:
        read_single_digit(int(inti[0]))
        read_single_digit(int(inti[1]))
    elif length==1:
        read_single_digit(int(inti[0]))

    else:
        print('세 자리수 이하의 10진 정수만 입력해주세요')
        



num=input('세자리 정수 입력:')
read_number(num)