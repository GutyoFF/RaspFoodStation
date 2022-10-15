from data_source import DataSourceInterface

try:
    import mariadb as sql
except ModuleNotFoundError:
    import mysql.connector as sql

host = 'localhost'
user = 'root'
pw = 'admin'
schema = 'rfs'


class LocalDataSource(DataSourceInterface):
    def __init__(self):
        try:
            connection = sql.connect(
                host=host,
                user=user,
                password=pw
            )
            self.db_cursor = connection.cursor()
        except sql.Error as e:
            print('Database error connection', e)

    def __del__(self):
        self.db_cursor.close()
