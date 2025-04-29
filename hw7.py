shopping_bag={}
print('[구입]')
while True:
    item_name=input('상품명?')
    

    if item_name=="":
        print(f'>>>장바구니 보기:{shopping_bag}')
        break
    else:
        item_count=int(input('수량은?'))
        shopping_bag[item_name]=item_count
        print(f'장바구니에 {item_name} {item_count}개가 담겼습니다')

print('[검색]')
serch=input('장바구니에서 확인하고자 하는 상품은?')
if serch in shopping_bag:
    print(f'{serch}은(는) {shopping_bag.get(serch)}개 담겨 있습니다')
