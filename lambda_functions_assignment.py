from functools import reduce
def add_tuples(output_list):
	user_input = input("Enter ordernumber,book title, quantity and cost separated by ','")
	input_list = (user_input.split(','))
	li=[int(input_list[2]),float(input_list[3])]
	(product_cost) = reduce((lambda x,y: x*y  if x*y>=100 else (x+10)*y),li)
	output_tuple = tuple((input_list[0],product_cost))
	output_list.append(output_tuple)
	return output_list

def second_function():
	ch = 1
	input_list = []
	output_list = []
	count = 0
	while(ch == 1):
		count = count + 1
		user_list = []
		user_list.append(count)
		chin = 1
		while(chin==1):
			user_orders = input('Enter book number, quantity and price separated by commas')
			input_tuple = list(user_orders.split(','))
			input_tuple[1] = int(input_tuple[1])
			input_tuple[2] = float(input_tuple[2])
			input_tuple = tuple(input_tuple)
			user_list.append(input_tuple)
			chin = int(input('Continnue?(1/0)'))
		input_list.append(user_list)
		ch = int(input('Continue?(1/0)'))
	for element in input_list:
		l2 = []
		print(element)
		for tuples in element:
			if(isinstance(tuples,tuple)):
				print(tuples)
				l1 = reduce((lambda x,y: tuples[1]*tuples[2]),tuples)
				l2.append(l1)
		print(l2)
		l1 = reduce((lambda x,y: x + y),l2)
		print(l1)
		t1 = []
		t1.append(element[0])
		t1.append(l1)
		output_list.append(t1)
	print (output_list)

def main():
	output_list = []
	ch = 1
	while(ch == 1):
		output_list = add_tuples(output_list)
		ch = int(input("continue?(1/0)"))
	print (output_list)
	second_function()
	

main()
	