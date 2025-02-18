import re
def search_transactions(transactions: list, criteria: str) -> list:
    founded_transactions = re.findall(criteria, transactions, flags=re.IGNORECASE)
    return founded_transactions

print(search_transactions())