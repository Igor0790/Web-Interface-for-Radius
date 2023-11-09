# import psycopg2
# from psycopg2 import OperationalError
#
#
# class Database:
#
#     def __init__(self, db_name, db_user, db_password, db_host, db_port=5432):
#
#         try:
#             self.connect = psycopg2.connect(
#                 dbname=db_name,
#                 user=db_user,
#                 password=db_password,
#                 host=db_host,
#                 port=db_port,
#             )
#             print("Подключение к PostgresSQL серверу - успешно!")
#         except OperationalError as e:
#             print(f"Ошибка '{e}' нас настигла.")
#         self.cursor = self.connect.cursor()
#
#     def execute_query(self, query: str) -> None:
#         self.connect.autocommit = True
#         try:
#             self.cursor.execute(query)
#             print('Запрос SQL прошел успешно!')
#             #self.cursor.commit()
#         except OperationalError as e:
#             print(f"Ошибка '{e}' нас настигла.")
#
#
#     def get_lines(self, query: str) -> (None, int, list):
#         records = None
#         try:
#             self.cursor.execute(query)
#             records = self.cursor.fetchall()
#         except OperationalError as e:
#             print('Errors: ', e)
#         finally:
#             return records