class Workload():
    #ip - str, credentials - Credentials, storage - List
    def __init__(self, ip, credentials, storage):
        if (type(ip) == str and type(credentials) == str and type(storage) == str): 
            self.ip = ip
            self.credentials = credentials
            self.storage = storage
        else:
            raise ValueError
                
    def __repr__(self):
        try:
            return '[ip - %s, credentials - %s, storage - %s ]' % (self.ip, 
                                                               self.credentials, 
                                                               self.storage)
        except TypeError:
            print('and')
        except AttributeError:
            print('and')


class Credentials(): pass
    #username - str, password - str, domain - str


if __name__ == '__main__':
    user1 = Workload('111', 11, 'fsfs')
    print(user1)       