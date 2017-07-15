import pickle
from Athlete import AthleteList

def split_coach_data(file_name):
    try:
        with open(file_name) as file_object:
            for each_line in file_object:
                a_list=each_line.strip().split(',')
                a=AthleteList(a_list.pop(0),a_list.pop(0),a_list)
            return a
    
    except IOError as err:
        print(str(err))
        return(None) 
file_list=['james.txt','julie.txt','sarah.txt','mikey.txt']
def put_to_store(file_list):
    all_athlete={}
    for each in file_list:
        ath=split_coach_data(each)
        all_athlete[ath.name]=ath
       
    try:
        with open('pickle.txt','wb') as pickle_save:
            pickle.dump(all_athlete,pickle_save)
    except pickle.PickleError as err:
        print(str(err))

    #print(all_athlete)
    return (all_athlete)


def get_from_store():
    try:
        with open('pickle.txt','rb') as pickle_store:
            all_athlete=pickle.load(pickle_store)
    except pickle.PickleError as err:
        print(str(err))
    return (all_athlete)
