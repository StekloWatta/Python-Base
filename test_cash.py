from main import Record, CashCalculator

cash_calculator = CashCalculator(1000)
cash_calculator.add_record(Record(amount=120, comment='кофе'))# дата должна добавиться автоматически

cash_calculator.add_record(Record(amount=300, comment='долг за обед')) # тут пользователь указал дату, сохраняем её

cash_calculator.add_record(Record(amount=3000,comment='поход в бар', date='17.06.2021'))

print(cash_calculator.get_today_cash_remained('rub'))