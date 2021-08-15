class Atm(object):
    def __init__(self,color,name_of_the_bank,material,typeofvolt,cardnumber):
        self.color = color
        self.name_of_the_bank = name_of_the_bank
        self.material = material
        self.typeofvolt= typeofvolt
        self.cardnumber = cardnumber

    def accountbalances(self):
        print("your account balances is: 10000000rs")

    def withdraw(self):
        print("money withdrawed")

    def deposit(self):
        print("money added to your account")

    def transfer(self):
        print("your money has been transfered")

account1=Atm("black","Bank of India","matel","600v","4024007103939509")
account1.accountbalances()
account1.withdraw()
account1.deposit()
account1.transfer()
print("color: ",account1.color)
print("name_of_the_bank: ",account1.name_of_the_bank)
print("material: ",account1.material)
print("typeofvolt: ",account1.typeofvolt)
print("cardnumber: ",account1.cardnumber)