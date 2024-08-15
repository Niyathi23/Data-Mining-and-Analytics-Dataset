import pandas as pd
from mlxtend.frequent_patterns import fpgrowth, association_rules
from mlxtend.preprocessing import TransactionEncoder

# Load data from CSV
data = pd.read_csv('Sales.csv')

# Preprocess the data: Convert each item column into a list of items
transactions = data['item'].apply(lambda x: x.split(', ')).tolist()

# Convert transaction data to one-hot encoded DataFrame
te = TransactionEncoder()
te_ary = te.fit(transactions).transform(transactions)
df = pd.DataFrame(te_ary, columns=te.columns_)

# Define the minimum support threshold
min_support = 0.2

# Run FP-Growth algorithm
frequent_itemsets = fpgrowth(df, min_support=min_support, use_colnames=True)

# Print the frequent itemsets
print("Frequent Itemsets:")
print(frequent_itemsets)

# If you want to generate and print association rules
rules = association_rules(frequent_itemsets, metric="support", min_threshold=min_support)
print("\nAssociation Rules:")
print(rules)
