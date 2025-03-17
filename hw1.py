def get_radius(prompt):
    r = int(input(prompt))
    return r


def get_circle_area(radius):
    s=radius*radius*3.14
    return s

#==================================================================
print('시작')
input_radius ="넓이를 구하고자 하는 원의 반지름은?"
r_result= get_radius(input_radius)
s_result=get_circle_area(r_result)
print('반지름이',r_result,'인 원의넓이는=3.14 X',r_result,'X',r_result,'=',s_result)
print('끝')