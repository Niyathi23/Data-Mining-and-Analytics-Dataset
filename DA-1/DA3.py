import pandas as pd
from itertools import combinations, chain
from collections import defaultdict

# Load data from CSV
data = pd.read_csv('Juice.csv')

# Preprocess the data
data['item'] = data['item'].apply(lambda x: set(x.split(',')))

def apriori(data, min_support):
    # Helper function to get frequent itemsets
    def get_frequent_itemsets(candidate_itemsets):
        itemset_count = defaultdict(int)
        for transaction in data['item']:
            for itemset in candidate_itemsets:
                if itemset.issubset(transaction):
                    itemset_count[itemset] += 1
        
        total_transactions = len(data)
        frequent_itemsets = []
        for itemset, count in itemset_count.items():
            support = count / total_transactions
            if support >= min_support:
                frequent_itemsets.append((itemset, support))
        
        return frequent_itemsets

    # Get all unique items
    all_items = set(item for transaction in data['item'] for item in transaction)
    
    # Generate candidate itemsets
    def generate_candidates(prev_itemsets, length):
        return set(frozenset(combo) for combo in combinations(prev_itemsets, length))

    # Initial candidates (single items)
    current_itemsets = generate_candidates(all_items, 1)
    frequent_itemsets = get_frequent_itemsets(current_itemsets)

    # Generate frequent itemsets iteratively
    k = 2
    while frequent_itemsets:
        prev_itemsets = set(chain.from_iterable(itemset for itemset, _ in frequent_itemsets))
        current_itemsets = generate_candidates(prev_itemsets, k)
        new_frequent_itemsets = get_frequent_itemsets(current_itemsets)
        if not new_frequent_itemsets:
            break
        frequent_itemsets.extend(new_frequent_itemsets)
        k += 1

    return frequent_itemsets

# Define the minimum support threshold
min_support = 0.2

# Run Apriori algorithm
frequent_itemsets = apriori(data, min_support)

# Print the frequent itemsets
print("Frequent Itemsets:")
for itemset, support in frequent_itemsets:
    print(f"{set(itemset)}: {support:.2f}")

