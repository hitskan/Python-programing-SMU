#사용자 함수 정의
def get_integer(prompt):
    res=int(input(prompt))
    return res

def exchange(cash):

    c500=cash // 500  #500원 개수 계산&저장
    cash %= 500

    c100=cash // 100  #100원 개수 계산&저장
    cash %= 100

    c50=cash // 50    #50원 개수 계산&저장
    cash %= 50

    c10=cash // 10    #10원 개수 계산&저장
    cash %= 10

    print("500원 동전의 개수:",c500)
    print("100원 동전의 개수:",c100)
    print("50원 동전의 개수:",c50)
    print("10원 동전의 개수:",c10)
    


#주 프로그램부=====================================

money=get_integer("동전으로 교환하고자 하는 금액은?:")
exchange(money)