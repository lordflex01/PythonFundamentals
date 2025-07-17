import csv
from datetime import datetime

class Expense():
    def __init__(self, date_str, vendor, category, amount):
        self.date_time = datetime.strptime(date_str, '%d/%m/%Y')
        self.vendor = vendor
        self.category = category
        self.amount = amount


class Expenses():
    def __init__(self):
        self.list = []
        self.sum = 0

    # Read in the December spending data, row[2] is the $$, and need to format $$
    def read_expenses(self,filename):
        with open(filename, newline='') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',')
            for row in csvreader:
                if '-' not in row[3]:
                    continue
                amount = float((row[3][2:]).replace(',',''))
                self.list.append(Expense(row[0],row[1], row[2], amount))
                self.sum += amount
                print(self.sum)


    def categorize_for_loop(self):
            necessary_expenses2 = set()
            food_expenses2 = set()
            unnecessary_expenses2 = set()
            for i in self.list:
                if (i.category == 'Abonnements et telephonie'      or i.category == 'Voyages et Transports' or 
                    i.category == 'Cadeaux et solidarite'  or i.category == 'Logement' or 
                    i.category == 'Virements emis'): 
                    necessary_expenses2.add(i)
                elif(i.category == 'Vie quotidienne' or i.category == 'Loisirs'):
                    food_expenses2.add(i)
                else:
                    unnecessary_expenses2.add(i)
            
            return [necessary_expenses2, food_expenses2, unnecessary_expenses2]

    def categorize_set_comprehension(self):
        necessary_expenses = {x for x in self.list 
                            if x.category == 'Abonnements et telephonie' or x.category == 'Voyages et Transports' or 
                                x.category == 'Cadeaux et solidarite'  or x.category == 'Logement' or 
                                x.category == 'Virements emis'}

        food_expenses = {x for x in self.list 
                            if x.category == 'Vie quotidienne' or x.category == 'Loisirs'}

        unnecessary_expenses = set(self.list) - necessary_expenses - food_expenses
        
        return [necessary_expenses, food_expenses, unnecessary_expenses]
