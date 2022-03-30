from . import Expense
import collections
import matplotlib.pyplot as plt

expenses = Expense.Expenses()
expenses.read_expenses('../data/spending_data.csv')

spending_categories = []

for expense in expenses.list:
    spending_counter = collections.Counter(spending_categories)
spending_categories.append(expense.category)

print(len(spending_counter))

top5 = spending_counter.most_common(5)

categories, count = zip(*top5)
fig, ax = plt.subplots()

ax.bar(categories, count)
ax.set_title('# of Purchases by Category')
plt.show()