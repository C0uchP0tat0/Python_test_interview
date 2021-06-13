import time
import pickle
import os

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
        return 'Workload(class):\n Ip - %s,\n Credentials - %s,\n Storage - %s ' % (self.ip, 
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
        return 'Credentials(class):\n Username - %s,\n Password - %s,\n Domain - %s ' % (self.username, 
                                                                                   self.password, 
                                                                                   self.domain)

class MountPoint():
       
    def __init__(self, mp_name, total_size):
        if (type(mp_name) == str and type(total_size) == int): 
            self.mp_name = mp_name  # type str 
            self.total_size = total_size  # type int
        else:
            raise ValueError
             
    def __repr__(self):
        return 'MountPoint(class):\n MountPoint_name - %s,\n Total_size - %s\n' % (self.mp_name, 
                                                                             self.total_size)

class Source():
    source_list_ip = []
    source_list_data = []

    def __init__(self, username, password, ip, change_ip_possible=True):
        if username is None or password is None or ip is None:
            raise ('You have None')
        else:
            self._username = username
            self._password = password
            self._ip = ip
            self._change_ip_possible = change_ip_possible
            self.source_list_ip.append(self._ip)
            self.source_list_data.append([self._username, self._password])

    def change_username(self, username):
        self._username = username
        return self._username

    def change_password(self, password):
        self._password = password
        return self._password

    def change_ip(self, ip):
        if self._change_ip_possible:
            self._ip = ip

    def get_username(self):
        return self._username

    def get_password(self):
        return self._password

    def get_ip(self):
        return self._ip

    def __repr__(self):
        return 'Sours(class):\n Username - %s,\n Password - %s,\n Ip - %s' % (self._username, 
                                                                              self._password,
                                                                              self._ip)

class MigrationTarget():

    _cloud_types = ['aws', 'azure', 'vsphere', 'vcloud']

    def __init__(self, cloud_type, cloud_credentials, target_vm):
        if (cloud_type in self._cloud_types and type(cloud_type) == str and
                type(cloud_credentials) == Credentials and
                type(target_vm) == Workload):
            self._cloud_type = cloud_type # type str and only from the types list
            self.cloud_credentials = cloud_credentials # type Credentials
            self.target_vm = target_vm # type Workload
        else:
            raise ValueError

    def __repr__(self):
        return 'MigrationTarget(class):\n Cloud_type - %s,\
                \n Cloud_credentials - %s,\n target_vm - %s' % (self._cloud_type, 
                                                                self.cloud_credentials,
                                                                self.target_vm)

class Migration(): 

    disk_c_allowed = True

    def __init__(self, select_mp, source, migration_target):
        if (type(select_mp) == list and (True in [type(i) == MountPoint for i in select_mp]) and
            type(source) == Workload and type(migration_target) == MigrationTarget):
            self.select_mp = select_mp               # type list[MountPoint]
            self.source = source                     # type Workload
            self.migration_target = migration_target # type MigrationTarget
            self.migration_state = 'not started'
        else:
            raise ValueError

    def run(self):
        self.migration_state = 'running'
        time.sleep(1)
        migration_target_mp = []
        for i in self.source.storage:
            if i.mp_name in [j.mp_name for j in self.select_mp]:
                migration_target_mp.append(i)
        if len(migration_target_mp) != 0 and self.disk_c_allowed:
            self.migration_state = "success"
            self.migration_target.target_vm.ip = self.source.ip
            self.migration_target.target_vm.credentials = self.source.credentials
            return self.migration_state, migration_target_mp, \
                   self.migration_target.target_vm.ip, \
                   self.migration_target.target_vm.credentials
        else:
            self.migration_state = 'error'
            return self.migration_state

    def __repr__(self):
        return 'Migration(class): Select_mp - %s, \n Source - %s,\
               \n Migration_target - %s, \n migration_state - %s' % (self.select_mp, 
                                                                     self.source,
                                                                     self.migration_target,
                                                                     self.migration_state)

class PersistenceLayer(Source):

    def __init__(self, obj_dict, file_storage):
        if type(obj_dict) == dict and type(file_storage) == str:
            self.obj_dict = obj_dict
            self.file_storage = file_storage
        else:
            raise ValueError

    def create(self, obj = {}):
        self.obj_dict == obj
        for k in Source.source_list_ip:
            for v in Source.source_list_data:
                self.obj_dict[k] = v
        with open(self.file_storage, 'wb') as file:
            pickle.dump(self.obj_dict, file)

    def read(self):
        with open(self.file_storage, 'rb') as file:
            self.obj_dict = pickle.load(file)
        return self.obj_dict

    def delete(self):
        os.remove(self.file_storage)



'''
if __name__ == '__main__':
    MP1 = [MountPoint('e:/', 333)]
    #MP2 = [MountPoint('d:/', 111)]
    #MP1 = [MountPoint('d:/', 111), MountPoint('e:/', 333)]
    #print(MP1)
    MP2 = [MountPoint('e:/', 333), MountPoint('c:/', 222), MountPoint('d:/', 111), ]
    #MP2 = []
    #print(MP2)

    Cred = Credentials('John', 'passw', 'ru')
    Cred2 = Credentials('Don', 'passwdon', 'com')
    #print(Cred)
    WL = Workload('192.0.0.1', Cred, MP1)
    WL2 = Workload('192.0.0.2', Cred2, MP2)
    #print(WL)
    Sour = Source('User', 'Pass', '192.0.0.2', )
    Sour2 = Source('User2', 'Pass2', '192.0.0.1')
    Sour3 = Source('User3', 'Pass3', '192.0.0.1')
    #Sour.change_ip('192.0.0.3')
    #print(Sour.get_ip())
    #print(Sour2.get_password())
    #Sour2.change_password('Pass_will_change')
    #print(Sour2.get_password())
    #Sour2 = Sourse('User', None, '192.0.0.2')
    #print(Sour)
    #print(MP1)
    MigTar = MigrationTarget('aws', Credentials('John', 'passw', 'ru'), \
        Workload('192.0.0.1', Credentials('John', 'passw', 'ru'), [MountPoint('e:/', 333)]))  
    Migrate = Migration( [MountPoint('c:/', 333), MountPoint('d:/', 333)], Workload('192.0.0.2', \
        Credentials('Don', 'passwdon', 'com'), [MountPoint('c:/', 333), MountPoint('e:/', 333)]), MigTar)
    #MigTar = MigrationTarget('aws', Cred, WL2)
    #print(MigTar)
    #Migrate = Migration(MP2, WL2, MigTar)
    print(Migrate.run())
    #print(Migrate)
    #print(PersistenceLayer.create(Sour))
    #print(PersistenceLayer.create(Sour2))
    #Sour.adds()
    #Sour2.adds()
    #Per = PersistenceLayer({}, 'File')
    #print(PersistenceLayer.create(Per))
    #print(PersistenceLayer.read(Per))
    #print(Sourсe.source_list_ip)
    #print(Sourсe.source_list_data)
    #PersistenceLayer.delete(Per)'''
    
    