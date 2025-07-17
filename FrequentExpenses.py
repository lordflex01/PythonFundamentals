from budget import Expense # import expense module
import collections # import collections
import matplotlib.pyplot as plt


expenses = Expense.Expenses() # set variable expenses to Expenses from Expense module
expenses.read_expenses('data/spending_data.csv') # read expenses on the csv 

spending_categories = [] # set spending list by category to an empty list
for expense in expenses.list: # for each spending category
    spending_categories.append(expense.category) # append category to spending list

spending_counter = collections.Counter(spending_categories) # create a counter for each spending category
print(spending_counter) # print the counter

top5 = spending_counter.most_common(5) # print the top 5 most common
print("Number of categories = " + str(spending_counter.__len__())) #len(spendingCounter)))
categories, count = zip(*top5) # zip the top 5 most common categories and their counts

fig, ax = plt.subplots() # to initialize fig as the Figure and ax as the Axes
ax.bar(categories, count) # plot the bar chart
ax.set_title('# Dépenses par catégorie') # set the title
plt.show() # show the plot

