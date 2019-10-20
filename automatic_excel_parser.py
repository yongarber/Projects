import pandas as pd
import numpy as np
import glob
import xlrd
import os
from openpyxl import load_workbook
from openpyxl.workbook import Workbook
# import pyexcel as p

# for filename in os.listdir('/Users/yongarber/Documents/RA_Sanati'):
# 	if filename.endswith('.XLS'):
# 		p.save_book_as(file_name=str(filename)+'.XLS',dest_file_name=str(filename)+'.xlsx')
# comman1= 'for %%x in (*.xls) do "/Applications/LibreOffice.app/Contents/MacOS/soffice" --headless --convert-to xlsx "%%x"'
# command="/Applications/LibreOffice.app/Contents/MacOS/soffice -- convert for file in *.xls; do soffice --to xlsx file --headless;done"
# os.system("gnome-terminal -e 'bash -c \""+comman1+";bash\"'")


 
locations = []
msas = []
tots = []         
aoas= []
bobs = []
cocs = []
dods =[]
eoes = []
fofs= []
gogs= []

for id_num, filename in enumerate([filename for filename in os.listdir('/Users/yongarber/Documents/RA_Sanati') if filename.endswith('.xlsx') and not 'Write' in filename]):
         #print(id_num,filename) 
         data1 = pd.read_excel(filename, 'Sheet1', usecols = "A", userows= "10") #, header =None)#, encoding_override="utf_8")
         location = data1['2017 CRA MSA Aggregate Report - Table 1-1'].iloc[2]
         locations.append(location)
         data2 = pd.read_excel(filename, 'Sheet1', usecols = "V", userows= "3")
         msa = data2[data2.columns[0]].iloc[0]
         msas.append(msa)
         df = pd.read_excel(filename)
         data3 =df.loc[df['Unnamed: 1'] == 'County Total']
         tot= np.array(data3)[0][6]
         tots.append(tot)
         aoa= np.array(data3)[0][9]
         aoas.append(aoa)
         bob= np.array(data3)[0][12]
         bobs.append(bob)
         coc= np.array(data3)[0][15]
         cocs.append(coc)
         dod= np.array(data3)[0][18]
         dods.append(dod)
         eoe= np.array(data3)[0][22]
         eoes.append(eoe)
         fof= np.array(data3)[0][26]
         fofs.append(fof)
         gog= np.array(data3)[0][32]
         gogs.append(gog)
         

datadf= {'County': locations, 'MSA': msas, 'num_b100':tots, 'value_b100':aoas, 'num_a100_b250':bobs, 'value_a100_b250':cocs, 'num_a250':dods, 'value_a250':eoes, 'num_b1000':fofs, 'value_b1000':gogs }
dataf = pd.DataFrame(datadf)

df_write = pd.ExcelWriter('Write_to_here.xlsx', engine='openpyxl')
dataf.to_excel(df_write, "Sheet1")
df_write.save()
   
