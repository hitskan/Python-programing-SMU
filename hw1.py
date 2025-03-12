def get_radius(prompt):
    r = int(input(prompt))
    return r


def get_circle_area(radius):
    s=radius*radius*3.14
    message='반지름이 '+ str(radius)+'인 원의 넓이 = '+str(radius)+" X "+str(radius)+" X 3.14 = "+str(s)
    return  message

#==================================================================
print('시작')
input_radius ="넓이를 구하고자 하는 원의 반지름은?"
r_result= get_radius(input_radius)
s_result=get_circle_area(r_result)
print(s_result)
print('끝')