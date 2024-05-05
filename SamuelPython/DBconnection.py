import sqlite3


class DBconnection:
    
    def __init__(self, dbfilename):
        self.connection = sqlite3.connect(dbfilename)
        self.cursor = self.connection.cursor()
    
    # return all columns from book
    def retrieveUserBooksByUsername(self, username): 
        querystr = '''
        select * from book 
        where userid = (select id from user where name = ?)
        '''
        self.cursor.execute(querystr, (username,))
        userBooks = self.cursor.fetchall()
        return userBooks
    
    def retrieveRecentBooks(self, limit = 5):
        querystr = '''
        select name, created_time, id from book
        order by created_time DESC
        limit ?
        '''
        self.cursor.execute(querystr, (limit,))
        recentBooks = self.cursor.fetchall()
        return recentBooks

    def retrieveUserByUsername(self, username):
        # ensure no such user exist
        querystr1 = '''
        select id from user
        where name = ?
        '''
        result = self.cursor.execute(querystr1, (username,)).fetchall()
        return result
    
    def saveUser(self, username, password):
        querystr = '''
        insert into user (name, password)
        values (?, ?)
        '''
        self.cursor.execute(querystr, (username, password))
        self.connection.commit()
        
    def verifyPassword(self, username, password):
        querystr2 = '''
        select id from user
        where name = ? and password = ?
        '''
        return self.cursor.execute(querystr2, (username, password)).fetchall()
        
    def retrieveBookInfoByBookId(self, id):
        querystr = '''
        select id, name, userid, created_time from book
        where id = ?
        '''
        self.cursor.execute(querystr, (id,))
        
        return self.cursor.fetchall()
    
    def retrieveChaptersByBookId(self, id):
        querystr = '''
        select id, title, content, bookid, created_time from chapter
        where bookid = ? and status = 1
        '''
        self.cursor.execute(querystr, (id,))
        
        return self.cursor.fetchall()

    def createBook(self, bookname, userid, createdTime):
        querystr = '''
        insert into book (name, userid, created_time)
        values (?, ?, ?)
        '''
        result = self.cursor.execute(querystr, (bookname, userid, createdTime)).fetchall()
        self.connection.commit()
        return result
    
    def createChapter(self, title, content, bookid, createdTime):
        querystr = '''
        insert into chapter (title, content, bookid, created_time)
        values (?, ?, ?, ?)
        '''
        result = self.cursor.execute(querystr, (title, content, bookid, createdTime)).fetchall()
        self.connection.commit()
        return result
        
    def retrieveBookByCreatedTime(self, createdTime):
        querystr = '''
        select id, name, userid, created_time from book
        where created_time = ?
        '''
        
        return self.cursor.execute(querystr, (createdTime,)).fetchall()
    
    def retrieveChapterByCreatedTime(self, createdTime):
        querystr = '''
        select id, title, content, bookid, created_time from chapter
        where created_time = ? and status = 1
        '''
        
        return self.cursor.execute(querystr, (createdTime,)).fetchall()
    
    def updateChapter(self, title, content, id):
        querystr = '''
        update chapter
        set title = ?, content = ?
        where id = ? and status = 1
        '''
        
        self.cursor.execute(querystr, (title, content, id))
        self.connection.commit()