import heapq

test_list = [10,20,30,40,25,30,5,4]
heapq.heapify(test_list)

print(test_list)

"""
for ith index

left child is at 2*i+1
right child is at 2*i+2 

"""

# to get data with the lowest priority

print(heapq.heappop(test_list)) # this also heapify the data

heapq.heappush(test_list, 20) # this insert the element to heap and maintain heap

print(test_list)


"""
heapq provides min heap. 

if we need to implement max heap then need to implement our own datastructure or 

make all element negative then heapify. 


"""