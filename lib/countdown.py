import time


def countdown(number):
    while number > 0:
        print(f'{number} SECOND(S)!')
        number -= 1
        print("HAPPY NEW YEAR!")
countdown(5)


def countdown_with_sleep(number):
    while number > 0:
        print(f'{number} SECOND(S)!')
        number -= 1
        time.sleep(1)
    print("HAPPY NEW YEAR!")


countdown_with_sleep(5)
