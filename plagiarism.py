import difflib
from difflib import SequenceMatcher
data= ['file1.txt','file2.txt','file3.txt','file4.txt']
 

for y in range(len(data)):   
    for x in range(y+1,len(data)):
        with open(data[y]) as file_1,open(data[x]) as file_2:
            file1_data = file_1.read()
            file2_data = file_2.read()
            similarity_ratio = SequenceMatcher(None,file1_data,file2_data).ratio()
            if(similarity_ratio > 0.85):
                print ( '{} {} {}'.format('plagiarism detected in files', y+1,x+1))
            else:
                print('{} {} {}'.format('No Plagiarism in files', y+1,x+1))
           
            
            
            
            
  
    


