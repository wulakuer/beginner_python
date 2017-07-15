from AthleteList import AthleteList
def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
       
    elif ':' in time_string:
        splitter = ':'
    else:
        return time_string
    (mins,secs)=time_string.split(splitter)
    return (mins+'.'+secs)

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


try:
    
    james=split_coach_data('james.txt ')
    print(james.name + "'s fast time are:" + str(james.top3()))
    james.append('1.01')
    james.extend(['1.02','1.03'])
    print(james.name + "'s fast time are:" + str(james.top3()))
    #julie=split_coach_data('julie.txt')
    #print(julie.name + "'s fast time are:" + str(julie.top3()))
    #mikey=split_coach_data('mikey.txt')
    #print(mikey.name + "'s fast time are:" + str(mikey.top3()))
    #sarah=split_coach_data('sarah.txt')
    #print(sarah.name + "'s fast time are:" + str(sarah.top3()))
    #vera=Athlete('vera vi')
    #vera.add_time('2.22')
    #print(vera.time)
except ValueError as err:
    print(str(err))
