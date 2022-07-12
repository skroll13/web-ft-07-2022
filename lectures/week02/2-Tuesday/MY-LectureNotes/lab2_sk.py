import corona 
corona_data = corona.data



# State
# cases
# recovered 
# active 

#find the sum of all recovered

#Get the name of the state for every item in 'data'
#Get the address of every item in 'data'
#get the 'recovered' of every item in 'data'
##add 'recovered' to 'sum of all recovered'
sum=0
for i in corona_data:
    print('State:',i['state'])
    print('Cases: ',i['cases'])
    print('Recovered: ',i['recovered'])
    print('Active: ',i['active'])
    print()
    sum=sum+i['recovered']
    
print('Sum of all recovered =',sum)