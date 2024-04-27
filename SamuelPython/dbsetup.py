import sqlite3

# connection object
connection = sqlite3.connect('mydb.db')

# execute your query and get result
cursor = connection.cursor()

# create some tables
create_table_user_query = '''

create table if not exists user(
    id integer primary key autoincrement,
    name text,
    password text
)

'''

create_table_book_query = '''
create table if not exists book(
    id integer primary key,
    name text,
    userid int,
    created_time timestamp default current_timestamp,
    foreign key(userid) references user(id)
)

'''

create_table_chapter_query = '''
create table if not exists chapter(
    id integer primary key,
    title text,
    content text,
    bookid int,
    created_time timestamp default current_timestamp,
    foreign key(bookid) references book(id)
)
'''

create_user_query = '''
insert into user (name, password)
values ('sam', '123')
'''

cursor.execute(create_table_user_query)
cursor.execute(create_table_book_query)
cursor.execute(create_table_chapter_query)
cursor.execute(create_user_query)



connection.commit()
connection.close()