from random import randint

numbers=[0,0,0,0]

prev_bulls, prev_cows , bulls, cows = 0, 0 , 0 ,0 
def generate_number(n):
    #gen_num = 0
    gen_num = randint(0,9)
    #print(n,"th value")
    #print(gen_num,n)
    if numbers[(n+1)%4] != gen_num and numbers[(n+2)%4] != gen_num and numbers[(n+3)%4] != gen_num:
		changed_idx = n
		prev_numbers(n)=numbers(n)
		return gen_num       
    else:
        generate_number(n)

def get_user_input():
	prev_bulls = bulls
	prev_cows  = cows
	bulls = input("How many bulls")
	cows  = input("How many cows ")

def guess_the_number():
	prev_numbers = numbers
	if prev_bulls = bulls:
		continue
	
	if prev_cows = cows:
		continue
	
	if bulls < prev_bulls:
		numbers[changed_idx] = prev_numbers[changed_idx]
		do_not_change.append(changed_idx)
		
		if (changed_idx+1)%4 not in do_not_change:
			numbers[(changed_idx+1)%4] = generate_number((changed_idx+1)%4)
			changed_idx = (changed_idx + 1) % 4
		elif (changed_idx+2)%4 not in do_not_change:
			numbers[(changed_idx+2)%4] = generate_number((changed_idx+2)%4)
			changed_idx = (changed_idx + 2) % 4
		elif (changed_idx+3)%4 not in do_not_change:
			numbers[(changed_idx+3)%4] = generate_number((changed_idx+3)%4)
			changed_idx = (changed_idx + 3) % 4
	
	if bulls > prev_bulls:
		if changed_idx == null:
			numbers(0)=generate_number(0)
		else:
			do_not_change.append(changed_idx)
		
		if length(do_not_change) == 4:
			number_found = true
		
		if (changed_idx+1)%4 not in do_not_change:
			numbers[(changed_idx+1)%4] = generate_number((changed_idx+1)%4)
			changed_idx = (changed_idx + 1) % 4
		elif (changed_idx+2)%4 not in do_not_change:
			numbers[(changed_idx+2)%4] = generate_number((changed_idx+2)%4)
			changed_idx = (changed_idx + 2) % 4
		elif (changed_idx+3)%4 not in do_not_change:
			numbers[(changed_idx+3)%4] = generate_number((changed_idx+3)%4)
			changed_idx = (changed_idx + 3) % 4
			
	if prev_cows > cows:
		use_numbers.append(numbers(changed_idx))		
		
	if prev_cows < cows:
		use_numbers.append(numbers(changed_idx))
	
	print(numbers)
	
def main():
	prev_numbers = numbers
	print('Guess a 4-digit Number with no digits repeated')
	print("If the number I guess has your digits in exact position, increase the bulls!!")
	print("If the number I guess has your digits but in different position, increase the cows!!")
	
	numbers[0]=generate_number(0)
	numbers[1]=generate_number(1)
	numbers[2]=generate_number(2)
	numbers[3]=generate_number(3)
	
	print(numbers)
	while not number_found:
		get_user_input()
		guess_the_number()
	
main()

