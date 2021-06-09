class Workload():
    
    def __init__(self, ip, credentials, storage):
        if (type(ip) == str and type(credentials) == Credentials and 
            type(storage) == list and (True in [type(i) == MountPoint for i in storage])): 
            self.ip = ip                    # type str 
            self.credentials = credentials  # type Credentials
            self.storage = storage          # type list[MountPoint]
        else:
            raise ValueError
                
    def __repr__(self):
        return 'Workload(class): Ip - %s, Credentials - %s, Storage - %s ' % (self.ip, 
                                                                              self.credentials, 
                                                                              self.storage)
       

class Credentials(): 

    def __init__(self, username, password, domain):
        if (type(username) == str and type(password) == str and type(domain) == str): 
            self.username = username  # type str 
            self.password = password  # type str
            self.domain = domain      # type str
        else:
            raise ValueError
                
    def __repr__(self):
        return 'Credentials(class): Username - %s, Password - %s, Domain - %s ' % (self.username, 
                                                                                   self.password, 
                                                                                   self.domain)

class MountPoint():
    mp_list=[] # list of class instances
   
    def __init__(self, mp_name, total_size):
        if (type(mp_name) == str and type(total_size) == int): 
            MountPoint.mp_list.append(self) # adds an instance of the class to the list
            self.mp_name = mp_name  # type str 
            self.total_size = total_size  # type int
        else:
            raise ValueError
             
    def __repr__(self):
        return 'MountPoint(class): MountPoint_name - %s, Total_size - %s' % (self.mp_name, 
                                                                             self.total_size)

class Sourse(Workload,Credentials):
    def check_ip():
        if Workload.self.ip is '':
            raise ('У вас тут None')
        else:
            Workload.self.ip = ip



if __name__ == '__main__':
    #MP1 = MountPoint('c:/', 222)
    #print(MP1)
    MP2 = MountPoint('d:/', 111)
    #print(MP2)
    Cred = Credentials('John', 'passw', 'ru')
    #print(Cred)
    WL = Workload('192.0.0.1', Cred, MountPoint.mp_list)
    print(WL)
    Sour = Sourse('', Cred, MountPoint.mp_list)
    print(Sour)
    #print(MountPoint.mp_list)  