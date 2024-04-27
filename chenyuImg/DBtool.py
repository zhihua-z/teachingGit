
import sqlite3


class Database:
    def __init__(self):
        self.conn = sqlite3.connect('app.db')
        self.cursor = self.conn.cursor()
    
    def login(self, username, password):
        queryset = self.cursor.execute(f'''
            
            select * from user where username = (?) and password = (?)
                            
                            ''', (username, password)).fetchall()
        
        return len(queryset) != 0
    
    def findProjectByUsername(self, username):
        queryset = self.cursor.execute('''
           select projectid, Project.name from Project
           inner join User on User.userid = Project.userid
           where User.username = (?)
        ''', (username,)).fetchall()
        
        return queryset

    
    
    
    
        
    def close(self):
        self.conn.close()
 