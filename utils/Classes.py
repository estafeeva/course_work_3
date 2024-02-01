from datetime import datetime

class Transaction:
    def __init__(self, transaction_id, state, transaction_date, operationAmount, description, transaction_from, transaction_to):
        self.transaction_id = transaction_id
        self.state = state
        self.transaction_date = transaction_date
        self.operationAmount = operationAmount
        self.description = description
        self.transaction_from = transaction_from
        self.transaction_to = transaction_to


    def stars_account(self, word):
        """Маскирует номер карты или номер счета"""
        if "Счет" in str(word):
            return "Счет " + '*' * 2 + word[-4:]
        elif "Maestro" in str(word):
            return "Maestro " + word[-16:-12] + " " + word[-12:-10] + '** **** ' + word[-4:]
        elif "Visa Classic" in str(word):
            return "Visa Classic " + word[-16:-12] + " " + word[-12:-10] + '** **** ' + word[-4:]
        elif "MasterCard" in str(word):
            return "MasterCard " + word[-16:-12] + " " + word[-12:-10] + '** **** ' + word[-4:]
        else:
            return " "

    def __repr__(self):
        return f"""
{self.transaction_date.strftime('%d.%m.%Y')} {self.description}
{self.stars_account(self.transaction_from)} -> {self.stars_account(self.transaction_to)}
{self.operationAmount['amount']} {self.operationAmount['currency']['name']} 
                    """


