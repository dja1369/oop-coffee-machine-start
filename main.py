import menu
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# 클래스 객체 선언
menulist = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
lastOrder = True

# 종료 신호 즉 False가 반환 될때 까지 반복
while lastOrder:
    # 메뉴 출력 및 메뉴 입력 받기
    option = menulist.get_items()
    choice = input(f'먹고 싶은 커피의 종류를 입력하세요 : {option}')
    # 커피 기계 작동 중지
    if choice == 'off':
        lastOrder = False
        print('coffe machine is Close')
        break
    # 리포트 출력.
    elif choice == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        # 메뉴 클래스 에서 음료 이름을 검색한후 조회하여 음료 아이템 반환
        drink = menulist.find_drink(choice)
        # 커피메이커에 리소스를 조회하여 제조가 가능한지 검증, 돈을 입력받아 코스트를 충분히 채웠는지 검증.
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            # 만약 모든 조건이 맞다면 음료 제조.
            coffee_maker.make_coffee(drink)







