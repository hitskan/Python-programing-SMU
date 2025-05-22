import pickle
import os

filepath='score.bin'
def input_scores():
    n=1
    list=[]
    while True:
        score=int(input(f'#{n}?'))
        if score < 0:
            break

        list.append(score)          
        n+=1
    return list
                  


def get_average(list):
    total_sum=0
    for i in list:
        total_sum += i
    average= total_sum/(len(list))
    return average

def show_scores(list):
    
    grade=''
    for j in list:
        grade += (f'{j} ')
        
    return (f'[점수 출력]\n개인점수:{grade}\n평균:{result_average:.1f}')
    

def save_data(filepath):
    with open(filepath,'wb') as file:
        pickle.dump(show_scores(result_list),file)

def load_data(filepath):
    with open(filepath,'rb') as file:
        return pickle.load(file)
    
    
if os.path.exists(filepath):
    print('[파일 읽기]')
    print()
    print(load_data(filepath))

else:
    result_list=input_scores()
    result_average=get_average(result_list)
    print(show_scores(result_list))
    save_data(filepath)

    

