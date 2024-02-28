#def match_words(words):
    #counter = 0
    
    #for i in words:
        #if len(i) >=3 and i[0] == i[-2]:
            #counter = counter +1
    #return counter

#print(match_words(['sfsffsf', 'aba', '1212212', 'sd']))


#array = [[ [ '£' for col in range(5)]for col in range(3)]for row in range(2)]
#print (array)



#numlist = [71, 0, 118, 8, 89, 120, 99, 58, 28, 33]
#evenlist = []
#oddlist = []

#for i in numlist:
    #if (i%2) == 0:
        #evenlist.append(i)
    #else:
        #oddlist.append(i)

#print(oddlist)
#print(evenlist)



#l1 = [1, 2, 3, 5, 7, 10]
#l2 = [1, 2, 4, 5, 7, 8, 11]

#x = list(set(l2) - set(l1))
#y = list(set(l1) - set(l2))
#print (x)
#print (y)



#l1 = ["99", 11, "Hello", 77, True]
#x = enumerate(l1)
#print(list(x))



#l1 = ['hello' , 'good', 'true', '101', 'false' ]
#x = " & ".join(l1)
#print(x)



#index = [1, 2, 3, 4, 5]
#item = ['jeans', 'hat', 't-shirt', 'trainer', 'belt']
#for i, it in zip(index,item):
 #print(i,it)



#l1 = [[54,302,45], [400,7,2], [14,280,121], [80,180,99]]
#print(min(l1, key = sum))