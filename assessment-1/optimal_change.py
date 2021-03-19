import math
 


class ChangeMaker:

    def __init__(self, total_price, amount_paid):
        self.total_price = total_price
        self.amount_paid = amount_paid

    BillsAndCoinsList = [
            [10000, '$100 bill'],
            [5000, '$50 bill'],
            [2000, '$20 bill'],
            [1000, '$10 bill'],
            [500, '$5 bill'],
            [100, '$1 bill'],
            [25, 'quarter'],
            [10, 'dime'],
            [5, 'nickel'],
            [1, 'penny']
        ]


    def change_difference(self):
        difference = self.amount_paid - self.total_price
        return difference

    
    def bill_count(self):
        difference = math.ceil(self.change_difference() * 100)
        bills_and_coins = self.BillsAndCoinsList
        counter = 0
        bill_list = []

        for bill in bills_and_coins:
            counter = 0
            while difference >= bill[0]:
                difference -= bill[0]
                counter += 1
            bill_list.append(counter)

        return bill_list


    def optimal_change(self):
        if self.change_difference() < 0:
            return "You don't have enough money."
        bill_counter = 0
        bill_list = self.bill_count()
        count_change_type = 0
        change_type_position = 0

        for bill_type in bill_list:
            if bill_type > 0:
                count_change_type += 1

        bills_and_coins = self.BillsAndCoinsList
        result = f"The optimal change for an item that costs ${self.total_price} with an amount paid of ${self.amount_paid} is "

        for bill in bills_and_coins:
            if bill_list[bill_counter] > 0:
                change_type_position += 1
                result += str(bill_list[bill_counter]) + " " + bills_and_coins[bill_counter][1]
                if bill_list[bill_counter] > 1:
                    result += "s"
                if change_type_position < count_change_type - 1:
                    result += ", "
                elif change_type_position == count_change_type - 1:
                    result += " and "

            bill_counter += 1
        if "pennys" in result:
             result = result.replace("pennys", "pennies")
        result += "."
        return result
        

tester = ChangeMaker(62.13, 50)
tester.optimal_change()
print(tester.optimal_change())




