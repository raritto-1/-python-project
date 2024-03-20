import time 
import random 
 
def sentence():
    subjects = ["Python", "Programming", "Artificial Intelligence", "Data Science", "Machine Learning"]
    verbs = ["is", "makes", "helps", "supports", "enhances"]
    adjectives = ["powerful", "flexible", "efficient", "amazing", "iAnnovative"]
    objects = ["code", "applications", "algorithms", "solutions", "models"]

    line_data = (f'{random.choice(subjects)} {random.choice(verbs)} {random.choice(adjectives)} {random.choice(objects)}')
    return line_data



def mistake (paratest ,usertest):
    error = 0 
    for i in range(len(paratest)):
        try:
            if paratest[i] != usertest[i]:
               error += 1
        except:
            error +=  1
    return error


def time_data(start_time , data_cal , end_time):
    cal_time = end_time - start_time
    if cal_time > 0:
        speed = len(data_cal) / cal_time
        return round(speed, 2)
    else:
        return 0
  

data = sentence()
print(data)

start_time = time.time()

data_cal = input ('')

end_time = time.time() 



print("speed:-",time_data(start_time , data_cal , end_time),'word/sec' )
print("Error :- " ,mistake(data_cal , data))

