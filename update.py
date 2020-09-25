import pickle
dayname = "thursday"
from data import thursday as daydata
dayfile = open(f"class_list/{dayname}",'wb')
pickle.dump(daydata,dayfile)
dayfile.close()
import pickle
from data import numbers
file = open('numbers','wb')
pickle.dump(numbers,file)
file.close()