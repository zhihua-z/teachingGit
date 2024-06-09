
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

    def findImageByProjectId(self, projectId):
        queryset = self.cursor.execute('''
            select projectid, 
                   path,
                   image_x,
                   image_y,
                   image_width,
                   image_height,
                   layer_id,
                   brightness,
                   versionid
            from Image
            where projectid = ?
        ''', (projectId,)).fetchall()
        
        return queryset
    
    
    
    
        
    def close(self):
        self.conn.close()
    
    # if successful return Ok
    # if user already exists return error_exist
    def determine_username(self, username, password):
        
        querystr1 = '''
        select userid from user
        where username = ?
        '''
        result = self.cursor.execute(querystr1, (username,)).fetchall()
        
        if len(result) != 0:
            return 'error_exist'
        
        # insert into db
        querystr = '''
        insert into user (username, password)
        values (?, ?)
        '''
        self.cursor.execute(querystr, (username, password))
        self.conn.commit()
        return 'Ok'
    
    def insertImageByProjectId(self, image_info, projectid):
        image_size = image_info[0]
        image_position = image_info[1]
        layer_id = image_info[2]
        path = image_info[3]
        brightness = image_info[4]
        username = image_info[5]
        versionId = image_info[6]
        
        querystr = '''
        
        insert into Image (projectid, path, image_x, image_y, image_width, image_height, layer_id, brightness, versionid)
        values (?, ?, ?, ?, ?, ?, ?, ?, ?)
        '''
        
        self.cursor.execute(querystr, (projectid, 
                                       path, 
                                       image_position[0],
                                       image_position[1],
                                       image_size[0],
                                       image_size[1],
                                       layer_id,
                                       brightness,
                                       versionId))
        
        self.conn.commit()
