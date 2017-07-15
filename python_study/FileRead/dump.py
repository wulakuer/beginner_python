import pickle
man=[]
other=[]
try:
    with open('sketch.txt') as data:
        for each_line in data:
            if not each_line.find(':')==-1:
                (role,spoken)=each_line.split(':',1)
            """help(each_line.split)"""
            spoken=spoken.strip()
            if role=='Man':
                man.append(spoken)
            elif role=='Other Man':
                other.append(spoken)
                
    with open('man_data.txt','wb') as man_file, open('other_data.txt','wb') as other_file:
        pickle.dump(man,man_file)
        pickle.dump(other,other_file)
    with open('man_data.txt','rb') as man_file, open('other_data.txt','rb') as other_file:
        man=pickle.load(man_file)
        other=pickle.load(other_file)
    print(man)
    print(other)
except IOError as err:
        print(str(err))
except pickle.PickleError as perr:
    print(str(perr))
        
