class Router:
    def __init__(self, name):
        self.name = name
        self.routing_table = []
        self.on = False
        self.password = None
        self.connection = {}
        
    def switch(self, state):
        self.on = state
        
    def isPoweredOn(self):
        return self.on
    
    def setPassword(self, password):
        self.password = password

    def connect(self, device, password):
        if password == self.password:
            self.connection[device.ip] = device
            return self
        else:
            return None
        
    def print_info(self):
        print(self.name)
        print(self.password)
        print(self.connection)
  
class Device:
    def __init__(self, name, ip):
        self.name = name
        self.ip = ip
        self.router = None
        self.received_message = []
    
    def connect(self, router, password):
        self.router = router.connect(self, password)
        
    def send_info(self, data, dest):
        self.router.send(data, dest)
        
    def print_info(self):
        print(self.name)
        if self.router:
            print('connected to', self.router.name)
        else:
            print('not connected')
        print('received info:', str(self.received_message))

      
r1 = Router('Router1')
r1.setPassword('88888888')
r1.switch(True)

# r1.routing_table.append(['192.168.x.x', 'LAN'])
# r1.routing_table.append(['127.0.0.1', 'SOURCE_DEVICE'])
# r1.routing_table.append(['x.x.x.x', 'OUTSIDE'])

r1.print_info()
        
myphone = Device('my phone', '192.168.0.1')
myphone.connect(r1, '88888888')
myphone.print_info()

r1.print_info()

# mylaptop = Device('my laptop', '192.168.50.50')


'''
myphone.send('11001100', '192.168.50.50')

# 设备把信息和ip地址发送到路由器
# 路由器查看自己有没有连接这个ip地址，如果有的话，把这个信息转发到那个ip地址上
# 接到信息的设备，在print_info的时候，要能够打印出是谁发来的什么信息

mylaptop.print_info()
'''
