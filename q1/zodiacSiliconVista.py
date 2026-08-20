birth_year = int(input("Enter your birth year: "))
if birth_year < 1900:
    print("Invalid Year, it should not be earlier than 1900")
else:
    zodiac_number = (birth_year - 1900) % 12
    if zodiac_number == 0:
        zodiac_sign = "Rat (鼠 / Shǔ)"
    elif zodiac_number == 1:
        zodiac_sign = "Ox (牛 / Niú)"
    elif zodiac_number == 2:
        zodiac_sign = "Tiger (虎 / Hǔ)"
    elif zodiac_number == 3:
        zodiac_sign = "Rabbit (兔 / Tù)"
    elif zodiac_number == 4:
        zodiac_sign = "Dragon (龙 / Lóng)"
    elif zodiac_number == 5:
        zodiac_sign = "Snake (蛇 / Shé)"
    elif zodiac_number == 6:
        zodiac_sign = "Horse (马 / Mǎ)"
    elif zodiac_number == 7:
        zodiac_sign = "Goat (羊 / Yáng)"
    elif zodiac_number == 8:
        zodiac_sign = "Monkey (猴 / Hóu)"
    elif zodiac_number == 9:
        zodiac_sign = "Rooster (鸡 / Jī)"
    elif zodiac_number == 10:
        zodiac_sign = "Dog (狗 / Gǒu)"
    elif zodiac_number == 11:
        zodiac_sign = "Pig (猪 / Zhū)"
    print("Your Chinese Zodiac Sign is: ", zodiac_sign)