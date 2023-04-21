import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="dish"
)

def registration(name,login, password, phone):
    cursor = mydb.cursor()
    query = "insert into users(Login,User_Password,Num_phone,Balance, Nickname, User_role)VALUES (%s,%s,%s, 15000, %s, 'user')"
    values = (login, password, phone, name)
    cursor.execute(query,values)
    mydb.commit()

def authorization(login,password):
    cursor = mydb.cursor()
    query = "select Id_user from Users where Login = %s and User_password = %s"
    values = (login,password)
    cursor.execute(query,values)
    result = cursor.fetchone()
    if result:
        query = "select User_role from Users where Id_user = %s"
        values = (result)
        cursor.execute(query,values)
        role = cursor.fetchone()[0]
        if(role == "user"):
            users_menu(result)
            mydb.commit()
        elif(role == "admin"):
            admins_menu(result)
        else:
            print("Что-то пошло не так")
    else:
        print("Неверный логин или пароль")
        mydb.commit()

def create_order(prod_list,price,users_id,count):
    cursor = mydb.cursor()
    query = "insert into Orders(Ingredients,Cost,Count,User_id)VALUES (%s,%s,%s,%s)"
    values = (prod_list,price,count,users_id[0])
    cursor.execute(query,values)
    print("Ваш заказ: " + prod_list+ str(price) +" "+ str(count))
    mydb.commit()

def get_orders(users_id):
    cursor = mydb.cursor()
    query = "select * from Orders where User_id = %s"
    values = (users_id)
    cursor.execute(query,values)
    result = cursor.fetchall()
    print(result)
    mydb.commit()

def get_users_data(users_id):
    cursor = mydb.cursor()
    query = "select Balance from Users where Id_user = %s"
    values = (users_id)
    cursor.execute(query,values)
    result = cursor.fetchone()[0]
    print("На балансе: " + str(result))
    mydb.commit()
    return result

def get_store():
    cursor = mydb.cursor()
    query = "select * from Sklad"
    cursor.execute(query)
    result = cursor.fetchone()
    return result

def get_data_for_admin(users_number):
    cursor = mydb.cursor()
    query = "select Id_user from Users where Num_phone = %s"
    values = (str(users_number))
    cursor.execute(query,values)
    ids = cursor.fetchone()
    print("На балансе: " + str(result))
    mydb.commit()
    cursor = mydb.cursor()
    query = "select * from Orders where User_id = %s"
    values = (ids)
    cursor.execute(query,values)
    result = cursor.fetchall()
    print("1 - Форель, 2 - картофель, 3 - морковь, 4 - лук репчатый, 5 - сливки, 6 - мука, 7 - масло сливочное, 8 - масло растительное, 9 - лавровый лист, 10 - перец душистый, 11 - перец черный, 12 - соль, 13 - укроп, 14 - вода: " + result)
    mydb.commit()

def users_menu(users_id):
    get_users_data(users_id)
    user = True
    while(user):
        print("Меню пользователя:")
        print("Выберите действие: 1 - Сделать заказ,  2 - Смотреть историю покупок")
        choose = input()
        if(choose == "1"):
                price = 0
                prod_list = ""
                print("Меню:")
                order=True
                while(order):
                    print("1 - Уха по фински, 2 - отменить заказ")
                    menu = int(input(""))
                    match menu:
                        case 1:
                            print("Ингредиенты: \n")
                            prod_list = "Форель, картофель, морковь, лук репчатый, сливки, мука, масло сливочное, масло растительное, лавровый лист, перец душистый, перец черный, соль, укроп, вода"
                            print(prod_list)
                            price=580
                            one= True
                            two = True
                            three = True
                            four = True
                            five = True
                            six = True
                            seven = True
                            eight = True
                            nine = True
                            print("Добавить ингредиенты или удалить: ")
                            print("1.Удалить")
                            print("2.Добавить")
                            print("3.Не изменять")
                            vvod=int(input(""))
                            match vvod:
                                case 1:
                                    print("Что вы хотите удалить")
                                    print("1.морковь, 2.лук репчатый, 3.сливки, 4.лавровый лист, 5.перец душистый, 6.перец черный, 7.соль, 8.укроп")
                                    ingredients = input()
                                    # if(ingredients == "1" or one):
                                    #     one=False
                                    #     prod_list-="морковь"
                                    #     price-=30
                                    #     print(prod_list)
                                    # if(ingredients == "2" or two):
                                    #     two=False
                                    #     prod_list-="лук репчатый"
                                    #     price-=20
                                    #     print(prod_list)
                                    # if(ingredients == "3" or three):
                                    #     three=False
                                    #     prod_list-="сливки"
                                    #     price-=60
                                    #     print(prod_list)
                                    # if(ingredients == "4" or four):
                                    #     four=False
                                    #     prod_list-="лавровый лист"
                                    #     price-=40
                                    #     print(prod_list)
                                    # if(ingredients == "5" or five):
                                    #     five=False
                                    #     prod_list-="перец душистый" 
                                    #     price-=20
                                    #     print(prod_list)
                                    # if(ingredients == "6" or six):
                                    #     six=False
                                    #     prod_list-="перец черный"
                                    #     price-=20
                                    #     print(prod_list)
                                    # if(ingredients == "7" or seven):
                                    #     seven=False
                                    #     prod_list-="соль"
                                    #     price-=10
                                    #     print(prod_list)
                                    # if(ingredients == "8" or eight):
                                    #     eight=False
                                    #     prod_list-="укроп"
                                    #     price-=20
                                    #     print(prod_list)
                                case 2:
                                    orders = True
                                    while(orders):
                                        print("Что вы хотите добавить")
                                        print("1.морковь, 2.лук репчатый, 3.сливки, 4.лавровый лист, 5.перец душистый, 6.перец черный, 7.соль, 8.укроп, 9.Закончить добавление ингредиентов")
                                        ingredients = input()
                                        if(ingredients == "1" and one):
                                            one=False
                                            prod_list+="морковь"
                                            price += 30
                                            print(prod_list)
                                        if(ingredients == "2" and two):
                                            two=False
                                            prod_list+="лук репчатый"
                                            price += 20
                                            print(prod_list)
                                        if(ingredients == "3" and three):
                                            three=False
                                            prod_list+="сливки"
                                            price += 60
                                            print(prod_list)
                                        if(ingredients == "4" and four):
                                            four=False
                                            prod_list+="лавровый лист"
                                            price += 40
                                            print(prod_list)
                                        if(ingredients == "5" and five):
                                            five=False
                                            prod_list+="перец душистый" 
                                            price += 20
                                            print(prod_list)
                                        if(ingredients == "6" and six):
                                            six=False
                                            prod_list+="перец черный"
                                            price += 20
                                            print(prod_list)
                                        if(ingredients == "7" and seven):
                                            seven=False
                                            prod_list+="соль"
                                            price += 10
                                            print(prod_list)
                                        if(ingredients == "8" and eight):
                                            eight=False
                                            prod_list+="укроп"
                                            price += 20
                                            print(prod_list)
                                        if(ingredients == "9"):
                                            orders = False
                                    
                                    count = int(input("Введите желаемое колическтво: "))
                                    if(count>=5):
                                        price=price*count-(count/100*15)
                                    else:
                                        price=price*count
                                    create_order(prod_list,price,users_id,count)
                                    print("Ингридиенты " +prod_list+ " Количество блюд-"+str(count)+" Цена-" + str(price))

                                case 3:
                                    one = False
                                    two = False
                                    three = False
                                    four = False
                                    five = False
                                    six = False
                                    seven = False
                                    eight = False
                                    price = price
                                    print(prod_list)
                                    order = False
                                    count = int(input("Введите желаемое колическтво: "))
                                    if(count>=5):
                                        price=price*count-(count/100*15)
                                    else:
                                        price=price*count
                                    create_order(prod_list,price,users_id,count)
                                    print("Ингридиенты " +prod_list+ " Количество блюд-"+str(count)+" Цена-" + str(price))
                        case 2:
                            order=False
                
                        
        elif(choose == "2"):
            get_orders(users_id)
        else:
            print("Неверный ввод данных")   
        
    # Функция ПриИзменении ПолучитьПользователя
    #     Если Элементы.Логин = Истина
    #         Тогда
    #             Сообщить "Ваня лох"
    #     КонецЕсли
    # КонецФункции

def admins_menu(user_id):
    get_users_data(user_id)
    admin = True
    while(admin):
        print("Меню администратора:")
        print("Выберите действие: 1 - На склад,  2 - Смотреть историю заказов, 3 - Закупка ингредиентов  q - Выход")
        choose = input()
        if(choose=="1"):
            print("Склад")
            get_store()
        elif(choose=="2"):
            cursor = mydb.cursor()
            query = "select * from Orders"
            cursor.execute(query)
            result = cursor.fetchall()
            print(result)
            phone= input("Введите номер пользователя: ")
            get_data_for_admin(phone)
        elif(choose=="3"):
            data = get_store()
            price = 0
            onecount = int(input("Сколько закупить рыбы? - "))
            price+=40*onecount
            twocount = int(input("Сколько закупить картошки? - "))
            price+=45*twocount
            threecount = int(input("Сколько закупить лука? - "))
            price+=45*threecount
            fourcount = int(input("Сколько закупить сливок? - "))
            price+=55*fourcount
            fivecount = int(input("Сколько закупить муки? - "))
            price+=60*fivecount
            sixcount = int(input("Сколько закупить сливочного масла? - "))
            price+=45*sixcount
            sevencount = int(input("Сколько закупить растительного масла? - "))
            price+=30*sevencount
            eightcount = int(input("Сколько закупить лаврового листа? - "))
            price+=10*eightcount
            ninecount = int(input("Сколько закупить душистого перца? - "))
            price+=10*ninecount
            tencount = int(input("Сколько закупить черного перца? - "))
            price+=10*tencount
            eightcount = int(input("Сколько закупить соли? - "))
            price+=10*eightcount
            twelvecount = int(input("Сколько закупить укропа? - "))
            price+=10*twelvecount
            thirtycount = int(input("Сколько закупить моркови? - "))
            price+=10*thirtycount
            onecount+=data[1]
            twocount+=data[2]
            threecount+=data[3]
            fourcount+=data[4]
            fivecount+=data[5]
            sixcount+=data[6]
            sevencount+=data[7]
            eightcount+=data[8]
            ninecount+=data[9]
            tencount+=data[10]
            twelvecount+=data[11]
            thirtycount+=data[12]
            print("Общая сумма закупки = " + str(price))
            yn = input("Продолжить? y/n ")
            if(yn == "y"):
                cursor = mydb.cursor()
                query = "update Sklad set count_one = %s, count_two = %s, count_three = %s, count_four = %s, count_five = %s, count_six = %s, count_seven = %s,  count_eight = %s, count_nine = %s, count_ten = %s, count_eleven = %s,  count_twelve = %s, count_thirty = %s where Id_sklad = 1"
                values = (onecount,twocount,threecount,fourcount,fivecount,sixcount,sevencount, eightcount, ninecount, tencount, eightcount, twelvecount, thirtycount)
                cursor.execute(query,values)
                mydb.commit()
                print("Спасибо за покупку!")
        elif(choose=="q"):
            admin=False
        else:
            print("Неверный ввод данных")
    
while(True):
    print("Выберите действие: 1 - Авторизация, 2 - Регистрация")
    choose = input()
    if(choose == "1"):
        print("Авторизация")
        login = input("Введите логин: ")
        password = input("Введите пароль: ")
        authorization(login,password)
    elif(choose == "2"):
        print("Регистрация")
        name = input("Введите имя: ")
        login = input("Введите логин: ")
        check=True
        while(check):
            password = input("Введите пароль: ")
            if(len(password)>=8):
                check=False
            else:
                print("Пароль должен содержать не менее восьми символов")
        phone = input("Введите номер телефона: ")

        registration(name,login,password,phone) 
    else:
        print("Неверный ввод данных")

