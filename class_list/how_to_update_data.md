## update database
To update the schedule of a  specific day in the code update the list of dictonaries in the file data.py
then in the update.py file replace the import day
for example if you update monday
the 1st line of update.py
write that as `from data import  monday as day`
## update numbers 
run the code 
`import pickle`
`from data import numbers`
`file = open('numbers','wb')`
`pickle.dump(numbers,file)`
`file.close()`
<b> The code's are in the update.py file comment out one part to use another</b>
