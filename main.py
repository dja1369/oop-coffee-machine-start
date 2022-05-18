from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menulist = Menu()
coffee_maker = CoffeeMaker()
lastOrder = True
while lastOrder == True:
    print(menulist.get_items())
    choice = input('먹고 싶은 커피의 종류를 입력하세요 : ')
    if choice == 'off':
        lastOrder = False
        print('coffe machine is Close')
        break
    elif choice == 'report':
        coffee_maker.report()
    else:
        menulist.find_drink(choice)
    # TODO : 메뉴를 주문받고 커피메이커의 리소스를 확인한뒤 부족하다면 제조불가를 가능하다면 메뉴를 제조해 제공 이때 리소스도 같이 감소하어야함.




