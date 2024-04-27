import sqlite3

conn = sqlite3.connect('app.db')
cursor = conn.cursor()

# if not exist user table create user table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS User (
        userid integer primary key autoincrement,
        username text not null, 
        password text not null
    );
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Project (
        projectid integer primary key autoincrement,
        userid integer not null,
        name text not null,
        foreign key (userid) references user(userid)
    );
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Image (
        imageid integer primary key autoincrement,
        projectid integer not null,
        path text not null,
        image_x integer not null,
        image_y integer not null,
        image_width integer not null,
        image_height integer not null,
        layer_id integer not null,
        brightness integer null,
        versionid integer not null,
        foreign key (projectid) references project(projectid)
    );
''')

cursor.execute('''
    INSERT INTO USER (username, password)
    values ('chenyu', '123456');
''')

cursor.execute('''
    INSERT INTO Project (userid, name)
    values (1, 'project mountain');     
''')

cursor.execute('''
    INSERT INTO Project (userid, name)
    values (1, 'project knight');     
''')

conn.commit()
conn.close()
