import unittest
import classes
import time
import os

class TestWorkload(unittest.TestCase):
    def setUp(self):
        self.credentials = classes.Credentials('John', 'pass', 'ru')
        self.storage = [classes.MountPoint('c:/', 111), classes.MountPoint('d:/', 222)]

    def tests(self):
        #ip not str
        self.assertRaises(ValueError, classes.Workload, 192, 
                          self.credentials, self.storage)
        #credentials not credentials class
        self.assertRaises(ValueError, classes.Workload,'192.0.0.1',
                          'self.credentials', self.storage)
        #storage not list
        self.assertRaises(ValueError, classes.Workload,'192.0.0.1',
                          self.credentials, classes.MountPoint('d:/', 222))
        #storage not list of mountpoint class
        self.assertRaises(ValueError, classes.Workload,'192.0.0.1',
                          self.credentials, [1])
        #parameter matching test
        workload = classes.Workload('192.0.0.1', self.credentials, self.storage)
        self.assertEqual(workload.ip, '192.0.0.1')
        self.assertEqual(workload.credentials, self.credentials)
        self.assertEqual(workload.storage, self.storage)

class TestCredentials(unittest.TestCase):
    def tests(self):
        #username not str
        self.assertRaises(ValueError, classes.Credentials, 111, 'pass', 'ru')
        #password not str
        self.assertRaises(ValueError, classes.Credentials, 'John', (), 'ru')
        #domain not str
        self.assertRaises(ValueError, classes.Credentials, 'John', 'pass', 111)
        #parameter matching test
        credentials = classes.Credentials('John', 'pass', 'ru')
        self.assertEqual(credentials.username, 'John')
        self.assertEqual(credentials.password, 'pass')
        self.assertEqual(credentials.domain, 'ru')

class TestMountPoint(unittest.TestCase):
    def tests(self):
        #mp_name not str
        self.assertRaises(ValueError, classes.MountPoint, 0, 111)
        #total_size not int
        self.assertRaises(ValueError, classes.MountPoint, 'c:/', '111')
        #parameter matching test
        mountpoint = classes.MountPoint('c:/', 111)
        self.assertEqual(mountpoint.mp_name, 'c:/')
        self.assertEqual(mountpoint.total_size, 111)

class TestSource(unittest.TestCase):
    def setUp(self):
        self.sour = classes.Source('John', 'pass', '192.0.0.1', False)
    def tests(self):   
        #ip cannot change
        self.sour.change_ip('192.0.0.2')
        self.assertEqual(self.sour.get_ip(), '192.0.0.1')
        #parameter matching test
        self.assertEqual(self.sour.get_ip(), '192.0.0.1')
        self.assertEqual(self.sour.get_username(), 'John')
        self.assertEqual(self.sour.get_password(), 'pass')

if __name__ == "__main__":
    unittest.main()