
        
def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
       
    elif ':' in time_string:
        splitter = ':'
    else:
        return time_string
    (mins,secs)=time_string.split(splitter)
    return (mins+'.'+secs)

class Athlete:
    def __init__(self,name,dob=None,time=[]):
        self.name=name
        self.dob=dob
        self.time=time
    def top3(self):
        return (sorted(set(sanitize(each) for each in self.time)))[0:3]
    def add_time(self,new_time):
        self.time.append(new_time)

    
    def add_times(self,new_time_list):
        self.time.extend(new_time_list)
        return self
    
def split_coach_data(file_name):
    try:
        with open(file_name) as file_object:
            for each_line in file_object:
                a_list=each_line.strip().split(',')
                a=Athlete(a_list.pop(0),a_list.pop(0),a_list)
            return a
    
    except IOError as err:
        print(str(err))
        return(None) 


try:
    
    james=split_coach_data('james.txt ')
    james.add_time('1.01')
    james.add_times(['1.02','1.03'])
    print(james.name + "'s fast time are:" + str(james.top3()))
    julie=split_coach_data('julie.txt')
    print(julie.name + "'s fast time are:" + str(julie.top3()))
    mikey=split_coach_data('mikey.txt')
    print(mikey.name + "'s fast time are:" + str(mikey.top3()))
    sarah=split_coach_data('sarah.txt')
    print(sarah.name + "'s fast time are:" + str(sarah.top3()))
    vera=Athlete('vera vi')
    vera.add_time('2.22')
    print(vera.time)
except ValueError as err:
    print(str(err))
