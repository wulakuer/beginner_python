def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
       
    elif ':' in time_string:
        splitter = ':'
    else:
        return time_string
    (mins,secs)=time_string.split(splitter)
    return (mins+'.'+secs)

class AthleteList(list):
    def __init__(self,name,dob=None,time=[]):
        list.__init__([])
        self.name=name
        self.dob=dob
        self.extend(time)
        
    def top3(self):
        return (sorted(set([sanitize(each) for each in self])))[0:3]
    
