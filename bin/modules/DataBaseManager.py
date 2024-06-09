import sqlite3
import os
import platform


class DBMRoutine():
    def __init__(self):
        self.dbpath = os.path.abspath("../O-HandDatabase.db")
        with sqlite3.connect(self.dbpath) as db:
            cursor = db.cursor()
            #Создание таблиц, если их нет
            cursor.executescript("""
                create table if not exists users(
                userId integer primary key autoincrement,
                userName nvarchar(100),
                OS nvarchar(200)
                );
                create table if not exists userActions(
                actionId integer primary key autoincrement,
                userId integer references users(userId),
                action nvarchar(1)
                );
                create table if not exists userChange(
                changeId integer primary key autoincrement,
                actionId integer references userActions(actionId),
                original nvarchar(1),
                updated nvarchar(1)
                )
                """)
            #Существует ли текущий пользователь в бд?
            cursor.execute(f"""
                select * from users where userName = '{os.getlogin()}' and OS = '{platform.system()} {platform.version()}'
                """)
            #Если нет, то добавляем его в бд
            if cursor.fetchone() is None:
                cursor.executescript(f"""
                    insert into users(userName, OS) values('{os.getlogin()}','{platform.system()} {platform.version()}')
                    """)
            #Задаём айди текущего пользователя
            cursor.execute(f"""
                select userId from users where userName = '{os.getlogin()}' and OS = '{platform.system()} {platform.version()}'
                """)
            self.currentUserId = int(cursor.fetchone()[0])
    #запись действий пользователя
    def action(self, text):
        with sqlite3.connect(self.dbpath) as db:
            cursor = db.cursor()
            cursor.executescript(f"""
                insert into userActions(userId, action) values('{self.currentUserId}','{text}')
                """)
    #Запись изменений скрипта пользователем, запись старой и новой версии скрипта
    def change(self, target, original, updated):
        with sqlite3.connect(self.dbpath) as db:
            cursor = db.cursor()
            cursor.executescript(f"""
                insert into userActions(userId, action) values('{self.currentUserId}','Изменил {target}')
                """)
            cursor.execute("select last_insert_rowid()")
            lastid = int(cursor.fetchone()[0])
            cursor.executescript(f"""
                insert into userChange(actionId, original, updated) values('{lastid}','{original}','{updated}')   
                """)


