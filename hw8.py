shopping_bag={}

def buy(shopping_bag):
    
        item_name=input('상품명?')
        
        if item_name=='':
            return False
        
        item_count=int(input('수량은?'))   
        shopping_bag[item_name]=item_count
        print(f'장바구니에 {item_name} {item_count}개가 담겼습니다')


def show(dic):
    print(f'장바구니 보기: {dic}')

def find(shopping_bag):
    while True:
        serch=input('장바구니에서 확인하고자 하는 상품은?')

        if serch in shopping_bag:
            print(f'{serch}은(는) {shopping_bag.get(serch)}개 담겨 있습니다')

        else:
            print(f'장바구니에 {serch}은(는) 없습니다')

        if serch=="":
            break



#==================================================

while True:
    if buy(shopping_bag) == False:
        break
show(shopping_bag)
find(shopping_bag)
