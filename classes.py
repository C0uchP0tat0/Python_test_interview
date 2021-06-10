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
    def __init__(self, username, password, ip):
        if username is None or password is None or ip is None:
            raise ('You have None')
        else:
            self._username = username
            self._password = password
            self._ip = ip

    def change_username(self, username):
        self._username = username
        return self._username

    def change_password(self, password):
        self._password = password
        return self._password

    @property  # changing the IP is not possible
    def change_ip(self, ip):
        self._ip = ip
        return self._ip

    def get_username(self):
        return self._username

    def get_password(self):
        return self._password

    def get_ip(self):
        return self._ip

    def __repr__(self):
        return 'Sours(class): Username - %s, Password - %s, Ip - %s' % (self._username, 
                                                                        self._password,
                                                                        self._ip)

class MigrationTarget():

    _cloud_types = ['aws', 'azure', 'vsphere', 'vcloud']

    def __init__(self, cloud_type, cloud_credentials, vm_target):
        if (cloud_type in self._cloud_types and type(cloud_type) == str and
                type(cloud_credentials) == Credentials and
                type(vm_target) == Workload):
            self._cloud_type = cloud_type # type str and only from the types list
            self.cloud_credentials = cloud_credentials # type Credentials
            self.vm_target = vm_target # type Workload
        else:
            raise ValueError

    def __repr__(self):
        return 'MigrationTarget(class): Cloud_type - %s, Cloud_credentials - %s, vm_target - %s' % (self._cloud_type, 
                                                                                                self.cloud_credentials,
                                                                                                self.vm_target)

class Migration(): pass




if __name__ == '__main__':
    #MP1 = MountPoint('c:/', 222)
    #print(MP1)
    MP2 = MountPoint('d:/', 111)
    #print(MP2)
    Cred = Credentials('John', 'passw', 'ru')
    #print(Cred)
    WL = Workload('192.0.0.1', Cred, MountPoint.mp_list)
    #print(WL)
    Sour = Sourse('User', 'Pass', '192.0.0.2')
    #Sour.change_ip('192.0.0.3')
    #print(Sour.get_ip())
    #print(Sour.get_password())
    #Sour.change_password('Pass_will_change')
    #Sour2 = Sourse('User', None, '192.0.0.2')
    #print(Sour)
    #print(MountPoint.mp_list)  
    MigTar = MigrationTarget('aws', Cred, WL)
    print(MigTar)