class Bandmate():
    """Создаём участника рок-группы"""

    def __init__(self, name, instrument):
        """Инициализация атрибутов участника группы"""
        self.name = name
        self.instrument = instrument
        print('Bandmate exists!')

    def play(self):
        """Получение информации, на чём играет в группе"""
        if self.name == 'Valeria':
            print(self.name + ' does the ' + self.instrument)
        else:
            print(self.name + ' plays the ' + self.instrument)

    def mood(self):
        """Узнать, что любит"""
        if self.name == 'Vanya':
            print(self.name + ' loves shooting video')
        elif self.name == 'Danya':
            print(self.name + ' loves Scala')
        elif self.name == 'Lesha':
            print(self.name + ' loves music')
        elif self.name == 'Elf':
            print(self.name + ' loves eating')
        elif self.name == 'Valeria':
            print(self.name + ' having troubles')
        elif self.name == 'Shmelev':
            print(self.name + ' loves Epidemia')
        else:
            print(self.name + " Oops, I don't know that person O_o")

class Multiinstrumentalist(Bandmate):
    """Создаём человека-мультиинструменталиста, наследуя от класса Bandmate"""
    def __init__(self, name, instrument, add_instrument):
        """Инициализация атрибутов класса родителя"""
        super().__init__(name, instrument)
        self.add_instrument = add_instrument

    def get_instrument(self):
        print(self.name + ' also plays ' + self.add_instrument)