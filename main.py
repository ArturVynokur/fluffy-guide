from UserClass import *

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # load_user = User.load_by_id(50)
    a = 1
    while a <= 10:

        load_user = User.load_by_id(a)

        if load_user:
            load_user.show_one()
        else:
            print('Пользователь не найден')
        a = a + 1