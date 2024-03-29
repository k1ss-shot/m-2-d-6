# def make_to_upper(func):
#     def wrapper():
#         result = func()
#         return result.upper()
#     return wrapper

# @make_to_upper
# def get_text():
#     return 'hello world'


# print(get_text())

# def cypher_phone_number(func):
    
#     def wrapper():
#         phone_number = func()
#         cypher_num = ''
        
#         for i, p in enumerate(phone_number):
#             if i in (0, 1 , 2):
#                 cypher_num += p
#             elif i in (10, 11):
#                 cypher_num += p
#             else:
#                 cypher_num += '#'
        
#         return cypher_num
#     return wrapper



# @cypher_phone_number
# def get_number():
    
#     return '996700007140'

# phone_number = get_number()
# print(phone_number)

# def greeting(func):
#     def wrapper():
#         print('Привет, сейчас я покажу номер телефона')
#         result = func()
        
#         return result
#     return wrapper


# @greeting
# def get_number():
    
#     return '996700007140'

# phone_number = get_number()
# print(phone_number)




# def double_salery(func):
#     def wrapper():
#         result = func()
#         return result * 2
#     return wrapper

# @double_salery
# def get_salery():
#     salary = 50000
#     return salary


# print(get_salery())


# def print_notifiacation(func):
#     def wrapper():
#         result = func()
#         print('Вам начислили зарплату')
        
#         return result
#     return wrapper

# @print_notifiacation
# def get_salery():
#     salary = 50000
#     return salary

# print(get_salery())


from time import time

def timer_decoration(func):
    def wrapper():
        start_time = time()
        func()
        end_time = time()
        print(f'Функия отправки пользователям заняло: {end_time - start_time:.2f} секунд')
        
    return wrapper

@timer_decoration
def send_message_to_user():
    users = range(1000)
    
    for user in users:
        print(f'Отправка сообщения пользователю {user}')
        
send_message_to_user()
