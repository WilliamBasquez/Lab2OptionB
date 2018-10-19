"""
@author: William E Basquez
"""
class Node(object):
	password = ""
	count = -1
	next = None
	
	def __init__(self, password, count, next):
		self.password = password
		self.count = count
		self.next = next


#This function reads a hard coded text file and turns it into a 2D array
def reader():
	contents = []
	array = []
	lines = open("text.txt", 'r')
	
	for line in lines:
		contents.append(line.split('\t'))
	
	for i in range(len(contents)):
		array.append(contents[i][1].strip("\n"))
			
	return array
		

#This function fills the Linked list while it checks the list itself for repeating
#elements, if the search returns None, it means the item that wants to be added
#to the list is not in the list already, therefore it adds it, if it returns
#a node, it increments it's count + 1, but does not add it to the list	
def Node_List(arr):
	node_list = None
	
	if len(arr) > 0:
		node_list = Node(arr[0], 0, node_list)
		cur = node_list

		for i in range(len(arr)):
			temp = checker(node_list, arr[i])
			if temp == None:
				cur.next = Node(arr[i], 1, None)
				cur = cur.next
			else:
				temp.count+=1
		
	return node_list
	
	
#This function check if a value, k, is inside a list, if it's not, it returns None
#if the value is in the list, it returns a reference to that node
def checker(head, k):
	while head != None:
		if head.password == k:
			return head
		head = head.next
	return None
	
	
#This function makes a dictionary from an array
def dict_of_passwords(array):
	dictionary = {}
	
	if len(array) > 0:
		for i in range(len(array)):
			if array[i] in dictionary:
				dictionary[array[i]] += 1
			else:
				dictionary[array[i]] = 1 
	
	return dictionary
	

#This function turns a Linked list into an array of nodes, to make sorting better
#in the sense that sorting an array is more straight forward than sorting a list
def list_to_arr(head):
	temp = head
	arr = []
	
	if head == None:
		return None
		
	while temp != None:
		arr.append(temp)
		temp = temp.next
	
	return arr
	
	
#This function turns an array into a Linked list, this method is only called
#when the array of nodes is already sorted and is ready to be made into a list
def arr_to_list(a):
	new_list = None
	if len(a) == 0:
		return None
		
	n = len(a)
	
	for i in range(n-1, -1, -1):
		start_count = a[i].count
		start_password = a[i].password
		new_list = Node(start_password, start_count, new_list)
		
	return new_list
	

def bubble_sort(head):
	new_list = None
	arr = list_to_arr(head)
	
	if head == None:
		return None	
		
	limit = len(arr)
		
	for i in range(limit):
		for j in range(0, limit-i-1):
			if arr[j].count < arr[j+1].count:
				t = arr[j]
				arr[j] = arr[j+1]
				arr[j+1] = t
		
	new_list = arr_to_list(arr)
		
	return new_list
	

#This function helps the 'main method' merge_sort, by merging 2 arrays into one	
def merge(ls, rs, array):
	ls_size = len(ls)
	rs_size = len(rs)
	a,b,c = 0,0,0
	
	while a < ls_size and b < rs_size:
		if ls[a].count >= rs[b].count:
			array[c] = ls[a]
			a+=1
		else:
			array[c] = rs[b]
			b+=1
		c+=1
	
	while a < ls_size:
		array[c] = ls[a]
		a+=1
		c+=1
	
	while b < rs_size:
		array[c] = rs[b]
		b+=1
		c+=1
	
	return array
	
	
#This method keeps reducing an array into smaller arrays until the sizes of such arrays
#equals 1, then by definition, those arrays are sorted, then calls the method merge to
#combine these two subarrays
def merge_sort(array):
	arr_size = len(array)
	
	if arr_size < 2:
		return array
		
	mid = arr_size // 2
	
	left = [None] * mid
	right = [None] * (arr_size - mid)
	
	for i in range(mid):
		left[i] = array[i]
	
	for j in range(mid, arr_size):
		right[j-mid] = array[j]
		
	left_sorted = merge_sort(left)
	right_sorted = merge_sort(right)
	final_array = merge(left_sorted, right_sorted, array)	
	
	return final_array
		
	
def main():
	#List = Node_List(reader())
	#dic = dict_of_passwords(reader())
	
	#temp = List
	#temp2 = bubble_sort(temp)
	#ttt = arr_to_list(merge_sort(list_to_arr(temp2)))
	
	#print("The 20 most used passwords are:")
	#i = 0
	#while i < 20:
		#print(ttt.count, ttt.password)
		#ttt = ttt.next
		#i += 1
	
	
main()
