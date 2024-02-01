import json
from datetime import datetime
from Classes import Transaction

def read_file():
    with open('operations.json', encoding="UTF-8") as json_file:
        profile = json.load(json_file)
    return profile


list_of_operations = read_file()
new_list_of_transactions = []
for item in list_of_operations:
    if item and item['state'] == 'EXECUTED':
        new_item = Transaction(transaction_id=item['id'],
                               state=item['state'],
                               transaction_date=datetime.strptime(item['date'],'%Y-%m-%dT%H:%M:%S.%f'),
                               operationAmount=item['operationAmount'],
                               description=item['description'],
                               transaction_from=item['from'] if 'from' in item else None,
                               transaction_to=item['to'])
        new_list_of_transactions.append(new_item)


new_list_of_transactions.sort(key=lambda x: x.transaction_date, reverse=True)
[print(item) for item in new_list_of_transactions[:5]]