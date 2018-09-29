"""code goes here"""
# CreditCard class
class CreditCard:
    # metodo constructor
    def __init__(self, name, number, expiration, cvc, status):
        self.__name = name
        self.__number = number
        self.__expiration = expiration
        self.__cvc = cvc
        self.__status = status
    # getter
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        raise AttributeError

    # getter
    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number):
        raise AttributeError

    # getter
    @property
    def expiration(self):
        return self.__expiration

    @expiration.setter
    def expiration(self, expiration):
        raise AttributeError

    # getter
    @property
    def cvc(self):
        return self.__cvc

    # getter
    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status):
        raise AttributeError

    def total_status(self):
        return sum(self.__status)


class Portfolio:

    def __init__(self, portfolio):
        self.__portfolio = portfolio

    # cuantas creditcard en portfolio
    def how_many_cards(self):
        return len(self.__portfolio)

    # Agrega una nueva credritcard
    # levanta una Exception si es diferente
    def add_creditcard(self, new_creditcard):
        return self.__portfolio.append(new_creditcard)
        raise Exception

    # return el balances de creditcard
    def sum_portfolio(self):
        return sum([sum(creditcard.status) for creditcard in self.__portfolio])
        #total = sum([sum(creditcard.status) for creditcard in self.__portfolio])
        #total = sum(self.__portfolio[0].status)
        # total = 0 ciclo for
        # for creditcard in self.__portfolio:
        #     total += sum(creditcard.status)
        #     #creditcard.name, sum(creditcard.status)
        #return total

    # Busacar en lista name
    def delete_creditcard(self, name):
        #del(self.__portfolio[[self.__portfolio.index(creditcard) for creditcard in self.__portfolio if creditcard.name == name][0]])
        self.__portfolio = [creditcard for creditcard in self.__portfolio if creditcard.name != name]

        # for creditcard in self.__portfolio: #iterar
        #     if creditcard.name == name: # encontrar name
        #         position = self.__portfolio.index(creditcard)
        #         del(self.__portfolio[position])
                     # obj
        #print(self.__portfolio)

                #print(creditcard.name) # traer

                #print("hola")

        #print(name)
        print(self.__portfolio)
        # raise Exception
