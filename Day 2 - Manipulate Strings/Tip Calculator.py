print("Welcome to the tip calculator!")
total_bill = input("What was the total bill?\n Bill in €:  ")
try:
    total_bill = float(total_bill)
    if total_bill < 0:
        print("Please insert a positive Numer.")
    else:
        tip_percentage = input("How much tip would you like to give? 10, 12 or 15 percentage?\n Tip percentage: ")
        try:
            tip_percentage = int(tip_percentage)
            if tip_percentage == 10 or tip_percentage == 12 or tip_percentage == 15:
                number_of_people = input("How many people to split the bill? \n Number of People: ")
                try:
                    number_of_people = int(number_of_people)
                    if number_of_people < 0:
                        print("Please insert a positive number of people.")
                    else:
                        total_bill_plus_tip = total_bill * tip_percentage / 100 + total_bill
                        single_payment = total_bill_plus_tip / number_of_people
                        single_payment= round(single_payment, 2)
                        print(f"Each person should pay: €{single_payment}")
                except:
                    print("Please insert a number of people.")
            else:
                print("Please choose one of the tips are given.")
        except ValueError:
            print("Please choose one of the tips are given.")
except ValueError:
    print("Please insert your bill in Numbers.")