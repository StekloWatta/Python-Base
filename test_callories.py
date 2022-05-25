from main import CaloriesCalculator, Record

def test_caloriest_calculator():
    calories_calculator = CaloriesCalculator(1000)
    calories_calculator.add_record(Record(amount=200, comment='кофе с булкой'))     # дата должна добавиться автоматически

    calories_calculator.add_record(Record(amount=450, comment='обед'))     # тут пользователь указал дату, сохраняем её

    calories_calculator.add_record(Record(amount=300, comment='бургер', date='15.06.2021'))

    calories_remained = 1000 - 200 - 450
    assert calories_remained == calories_calculator.get_calories_remained()
