from numpy import extract
import pandas as pd
import matplotlib.pyplot as plt

# this is a practice for an exam for adding to/improving an already existing system


def main_menu():
	flag = True
	while flag:
		print("#################################################")
		print("#### Welcome to Elanp Air Flight Data system ####")
		print("#################################################")
		print("")
		print("########### Please select an option #############")
		print("### 1. View passenger numbers")
		print("### 2. Avg customers for AM & PM filghts for 2 selected routes")
		print("### 'x' to Exit")

		choice = input('Enter your number selection here: ')
		choices = ['1', '2', '3', 'x']

		if choice not in choices:
			print('Enter a number selection from above.')
			flag = True
		else:    
			print('Choice accepted!')
			flag = False

	return choice


def get_airport(connection):
	flag = True
	while flag:
		print(f"########### Please select a {connection} airport #############")
		print("### 1. Dublin (DUB)")
		print("### 2. Edinburgh (EDI)")
		print("### 3. Glasgow (GLA")
		print("### 4. London Heathrow (LHR)")
		print("### 5. London Luton (LTN)")
		print("### 6. Manchester (MAN)")

		choice = input('Enter your selection here: ')
		choices = ['1', '2', '3', '4', '5', '6']

		if choice not in choices:
			print('Enter a selection from above.')
			flag = True
		else:    
			print('Choice accepted!')
			flag = False

	return choice

# makes sure they are not the same
def compare_airports(depart, dest):
	if depart == dest:
		return True
	else:
		return False


def get_number_days():
	flag = True
	while flag:

		print("########### Please enter the number of previous days of data you wish to see #############")
		choice = input('Enter your number selection here: ')
 
		try:
			int(choice)
		except:
			print("Sorry, you did not enter a valid number")
			flag = True
		else:    
			print(f"########### You have chosen to see data for the last {choice} days #############")
			flag = False
		

	return int(choice)

# coverts from number to airport abbrv.
def convert_airport_choice(choice):
	if choice == "1":
		conv_choice = "DUB"
		return conv_choice
	elif choice == "2":
		conv_choice =  "EDI"
		return conv_choice
	elif choice == "3":
		conv_choice =  "GLA"
		return conv_choice
	elif choice == "4":
		conv_choice =  "LHR"
		return conv_choice
	elif choice == "5":
		conv_choice =  "LTN"
		return conv_choice
	else:
		conv_choice =  "MAN"
		return conv_choice


def get_data_option1(depart, dest, days):
	df = pd.read_csv("Task4a_data.csv")
	extract = df.loc[(df['From'] == depart) & (df['To'] == dest)]
	extract_days = extract.iloc[: , -days: ]
	print("We have found these flights that match your criteria:")
	return extract_days


def get_data_option2(depart, dest, days):
	df = pd.read_csv('Task4a_data.csv')
	extract = df.loc[(df['From'] == depart) & (df['To'] == dest)]
	extract_days = extract.iloc[: , -days: ].mean()
	AM_extract = extract_days.loc[df['Time'] == 'AM']
	PM_extract = extract_days.loc[df['Time'] == 'PM']
	print("We have found these flights that match your criteria:")
	return AM_extract, PM_extract


def option1():
	flag = True
	while flag:
		depart_airport = get_airport('departure')
		destination_airport = get_airport('destination')
		comparison = compare_airports(depart_airport, destination_airport)
		if comparison:
			print("")
			print("")
			print("############### Data entry error ###################")
			print('Destination and departure airports must be different')
			print("")
			print("")
			flag = True
		else:
			flag = False
			
	dep_choice = convert_airport_choice(depart_airport)
	dest_choice = convert_airport_choice(destination_airport)

	days = get_number_days()

	print(f"You have selected departure from: {dep_choice}")
	print(f"You have selected destination as: {dest_choice}")

	extracted_data = get_data_option1(dep_choice, dest_choice, days) 
	if extracted_data.empty:
		print('There are no flights for the route you selected')
		return
	
	extract_no_index = extracted_data.to_string(index=False)
	print(extract_no_index)
	
	df = pd.DataFrame(extracted_data).reset_index(drop=True)	
	fig, ax = plt.subplots()
	for row in df.T:
		ax.plot(df.T[row], marker='x', label=f'Flight {row+1}')
	plt.xlabel('Dates')
	plt.ylabel('Number of Customers')
	plt.title('Passenger numbers of a route over time')
	plt.legend()
	plt.show()
	

def option2():
	print('### Route 1 ###')
	flag = True
	while flag:
		depart_airport1 = get_airport('departure')
		destination_airport1 = get_airport('destination')
		comparison1 = compare_airports(depart_airport1, destination_airport1)
		if comparison1:
			print("")
			print("")
			print("############### Data entry error ###################")
			print('Destination and departure airports must be different')
			print("")
			print("")
			flag = True
		else:
			flag = False

	print('### Route 2 ###')
	flag = True
	while flag:
		depart_airport2 = get_airport('departure')
		destination_airport2 = get_airport('destination')
		comparison2 = compare_airports(depart_airport2, destination_airport2)
		if comparison2:
			print("")
			print("")
			print("############### Data entry error ###################")
			print('Destination and departure airports must be different')
			print("")
			print("")
			flag = True
		else:
			flag = False

def main():
	flag = True
	while flag:
		main_menu_choice = main_menu()

		if main_menu_choice == '1':
			option1()

		elif main_menu_choice == '2':
			option2()

		elif main_menu_choice == 'x':
			print("Exiting...")
			flag = False


main()
