
import csv
def read(path):
    with open(path,'r') as csvfile:
      reader=csv.reader(csvfile,delimiter=',')
      header=next(reader)
      DATA=[]
      for row in reader:
         interable=zip(header,row)
         country_dict={key:value for key,value in interable}
         DATA.append(country_dict)
         return DATA
       
if __name__=='__main__':
    data=read('./paquetes/world_population.csv')
    print(data)
    