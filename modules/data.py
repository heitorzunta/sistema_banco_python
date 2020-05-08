from datetime import date

# Classe Data

class Data():
    def __init__(self, data):
        self.data = date.fromisoformat(self.armazenar_data(data))

    def armazenar_data(self, data_nascimento):
        data = (data_nascimento.split('/'))
        return f'{data[2]}-{data[1]}-{data[0]}'

    def __str__(self):
        return self.data.strftime('%d/%m/%y')