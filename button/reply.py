from aiogram.types import KeyboardButton,ReplyKeyboardMarkup

def reply_button():
    btn1=KeyboardButton(text="📍Filial")
    btn2 = KeyboardButton(text="✅Start")
    btn3 = KeyboardButton(text="👨🏻‍💻Admin")

    design=[[btn1,btn2],
            [btn3]]

    return ReplyKeyboardMarkup(keyboard=design,resize_keyboard=True)

def start_button():
    btn1 = KeyboardButton(text="Woman 🧍‍♀️")
    btn2 = KeyboardButton(text="Men 🧍‍♂️")
    btn3 = KeyboardButton(text="👨🔙 back")

    design = [[btn1, btn2],
              [btn3]]

    return ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True)

def women_button():

        btn1 = KeyboardButton(text="1-oy")
        btn2 = KeyboardButton(text="2-oy")
        btn3 = KeyboardButton(text="3-oy")
        btn4 = KeyboardButton(text="4-oy")
        btn = KeyboardButton(text="🔙 back")

        design = [[btn1, btn2],
                  [btn3,btn4],
                  [btn]]

        return ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True)


def week_button():
    btn1 = KeyboardButton(text="Dushanba")
    btn2 = KeyboardButton(text="Seshanba")
    btn3 = KeyboardButton(text="Chorshanba")
    btn4 = KeyboardButton(text="Payshanba")
    btn5 = KeyboardButton(text="Juma")
    btn6 = KeyboardButton(text="Shanba")

    btn = KeyboardButton(text="🔙 back")

    design = [[btn1, btn2,btn3],
              [btn4,btn5,btn6],
              [btn]]

    return ReplyKeyboardMarkup(keyboard=design,one_time_keyboard=True ,resize_keyboard=True)
