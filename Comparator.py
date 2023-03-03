##### Libraries ################################################
import csv
from unidecode import unidecode
##### Dictionary ###############################################
low_dict = {ord(i): None for i in '"/-_,!?+()'}
##### Correlation function #####################################
def corr(a,b):
    if a == b:
        return 1
    else:
        a = set(unidecode(a).lower().translate(low_dict).split())
        b = set(unidecode(b).lower().translate(low_dict).split())
        corr = float(len(a.intersection(b)))/(float(max(len(a),len(b))))
        return corr
##### Opening file #############################################
df = open("items_titles_test.csv", "r")
file = df.readlines()
##### Iterating and computing ##################################
c_ab = []
for i in range(1,len(file)-1):
    a = file[i]
    for j in range(i+1, len(file)):
        b = file[j]
        c_ab.append([a,b,corr(a,b)])
##### Printing output ##########################################
with open("out.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(c_ab)
##### Closing file #############################################
df.close()
