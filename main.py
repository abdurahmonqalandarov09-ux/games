
# class Bank:


#     def __init__(self, owner, pin, balance):
#         self.owner = owner
#         self.__pin = pin
#         self._balance = balance

#     @property
#     def show_balance(self):
#         return f"owner: {self.owner}, Balance: {self._balance}"

#     @show_balance.setter
#     def show_balance(self, amount):
#         if amount > 0:
#             self._balance += amount
#             return f"New balance :{self._balance}"

# card = Bank("Abdurahmon", 1123581321, 10000000)


# print(card.show_balance)
# card.show_balance = 15000
# print(card.show_balance)



from datetime import *


# task_db = []
# user_db = []

# user_id = 0
# task_id = 0
# is_login = None

# def create_task(title, description, duration, user_id):
#     global task_id
#     task_id+=1
#     task = {
#         "task_id": task_id,
#         "title": title,
#         "description": description,
#         "duration": duration,
#         "status": False,
#         "user_id": user_id,
#         "create at": datetime.now()
#     }
#     task_db.append(task)

# def read_task(task_id, user_id):
#     for i in task_db:
#         if i ["task_id"] == task_id and i["user_id"] == user_id:
#             return f"""
# Your task: {i["task_id"]}
# Title: {i["title"]}
# Description: {i["description"]}
# Duration: {i["duration"]}
# Status: {i["status"]}
#                     """

#     else:
#         return False

# def update_task(task_id, title, descp, due, status):
#     for i in task_db:
#         if title:
#             i["title"] = title
#         if descp:
#             i["description"] = descp
#         if due:
#             i["duration"] = due
#         if status:
#             i["status"] = status


# def delete_task(task_id):
#     for i in task_db:
#         if i["task_id"] == task_id:
#             task_db.remove(i)
#             return True
#     else:
#         return False


# def registration(username, password, full_name, phone_number):
#     global user_id, is_login
#     user_id += 1
#     user = {
#         "user_id": user_id,
#         "username": username,
#         "password": password,
#         "full_name": full_name,
#         "phone_number": phone_number,
#         "created_at": datetime.now()
#     }
#     user_db.append(user)
#     is_login = user


# def login(username, password):
#     global is_login
#     for user in user_db:
#         if user["username"] == username and user["password"] == password:
#             is_login = user
#             return True
#     else:
#         return False


# def show_profile():
#     return f"""
# My profile: {is_login["user_id"]}
# Username: {is_login["username"]}
# Full name: {is_login["full_name"]}
# Phone number: {is_login["phone_number"]}
# Created at: {is_login["created_at"]}"""


# while True:
#     if is_login == None:
#         n = int(input("1)Registration\n2)Login\n0)Exit\nChoose one:"))
#         match n:
#             case 1:
#                 username = input("Username: ")
#                 password = input("Password: ")
#                 registration(username, password)
#             case 0:
#                 print("Good bye")
#                 break




#     else:
#         n = int(input("1)Create Task\n2)Read task\n3)Update Task\n4)Delete\n5)Show Profile\n6)Log out0)Exit\nChoose one:"))
#         match n :
#             case 1:
#                 print("Start create task")
#                 title = input("Title: ")
#                 descp = input("Description: ")
#                 durat = input("Duration: ")
#                 create_task(title, descp, durat, is_login["user_id"])
#                 print("Task created !!")
#             case 2:
#                 k = int(input("Enter id task: "))
#                 print(read_task(k, is_login["user_id"]))
#             case 3:
#                 print("Start update task")
#                 k = int(input("Enter id task: "))
#                 if read_task(k, is_login["user_id"]):
#                     title = input("Change or press enter to continue: ")
#                     descp = input("Description or press enter to continue: ")
#                     durat = input("Duration or press enter to continue: ")
#                     status = bool(input("Status or press enter to continue: "))
#                     update_task(k, title, descp, durat, status)
#                     print("Task updated !!")
#                 else:
#                     print("Task not found !!")
#             case 4:
#                 k = int(input("Enter id task: "))
#                 if delete_task(k):
#                     print("Task deleted !!")
#                 else:
#                     print("Task not found !!")
#             case 0:
#                 print("Exit")
#                 break
#             case _:
#                 print("Invalid input !!")


# 2
# from random import *

# class Hero:
#     def __init__(self, name):
#         self.name = name
#         self.health = 100
#         self.power = 10

#     def attack(self, other):
#         other.health -= self.power

#     def is_alive(self):
#         return self.health > 0

# class Warrior(Hero):
#     def __init__(self, name):
#         super().__init__(name)
#         self.power = 15

# class Mage(Hero):
#     def __init__(self, name):
#         super().__init__(name)
#         self.power = 20

#     def attack(self, other):               # свой метод вместо родительского
#         if random.random() < 0.5:
#             print(f"{self.name} промахнулся! ✨")
#         else:
#             super().attack(other)          # попал — бьём как обычный герой

# class Healer(Hero):
#     def __init__(self, name):
#         super().__init__(name)
#         self.power = 5

#     def heal(self):
#         self.health = min(100, self.health + 15)
#         print(f"{self.name} лечится 💚 (+15 HP)")

# def battle(hero1, hero2):
#     round_num = 1
#     while hero1.is_alive() and hero2.is_alive():
#         print(f"--- Раунд {round_num} ---")
#         hero1.attack(hero2)
#         if hero2.is_alive():          # зачем эта проверка — см. ниже
#             hero2.attack(hero1)
#         round_num += 1

#     if hero1.is_alive():
#         print(f"🏆 Победил {hero1.name}!")
#     else:
#         print(f"🏆 Победил {hero2.name}!")





# while True:
#     print("Menu:")
#     for k, v in products.items(): print(f"{k}) {v}")
    
#     choice = int(input("\n1)Buy product\n2)Remove product\n3)Check\n0)Exit\nYour choice: "))
#     match choice:
#         case 1:
#             which = int(input(f"Which product?(1-{len(products)}): "))
#             cart.add(products[int(which)])
#             print(f"Added: {products[int(which)].name}")
#         case 2:
#             name = input("Enter product name: ")
#             cart.remove(name)
#         case 3:
#             cart.checkout()
#             break
#         case 0:
#             print("Goodby!")
#             break
#         case _:
#             print("Invalid input!")






# 3

class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price

#     def __str__(self):
#         return f"{self.name} — {self.price} руб."

# class Cart:
#     def __init__(self):
#         self.items = []    # новая корзина всегда пустая
    
#     def add(self, product, quantity=1):
#         for _ in range(quantity):
#             self.items.append(product)

#     def total(self):
#         return sum(item.price for item in self.items)

#     def remove(self, name):
#         for item in self.items:
#             if item.name == name:
#                 self.items.remove(item)
#                 return                # нашли и удалили — сразу выходим!
#         print(f"Товара «{name}» нет в корзине")
    
#     def checkout(self):
#         print("===== ЧЕК =====")
#         for item in self.items:
#             print(item)               # сработает наш __str__!
#         print("---------------")
#         print(f"ИТОГО: {self.total()} руб.")

# products = {1: Product("Cola", 90), 2: Product("Lay's", 120), 3: Product("Snikers", 80)}
# cart = Cart()

# while True:
#     print("Menu:")
#     for k, v in products.items(): print(f"{k}) {v}")
    
#     choice = int(input("\n1)Buy product\n2)Remove product\n3)Check\n0)Exit\nYour choice: "))
#     match choice:
#         case 1:
#             which = int(input(f"Which product?(1-{len(products)}): "))
#             cart.add(products[int(which)])
#             print(f"Added: {products[int(which)].name}")
#         case 2:
#             name = input("Enter product name: ")
#             cart.remove(name)
#         case 3:
#             cart.checkout()
#             break
#         case 0:
#             print("Goodby!")
#             break
#         case _:
#             print("Invalid input!")
















