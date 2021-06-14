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

class TestMigration(unittest.TestCase):
    def setUp(self):
        self.selected_mount_points = [classes.MountPoint('c:/', 333)]
        self.selected_absent_mount_points = [classes.MountPoint('d:/', 333)]
        self.source_credentials = classes.Credentials('Don', 'passwdon', 'com')
        self.source_storage_mount_points = [classes.MountPoint('c:/', 333), 
                                            classes.MountPoint('e:/', 333)]
        self.source = classes.Workload('192.0.0.2', self.source_credentials, 
                                                    self.source_storage_mount_points)
        self.cloud_credentials = classes.Credentials('cloudJohn', 'passw', 'ru')
        self.target_credentials = classes.Credentials('John', 'passw', 'ru')
        self.target_storage = [classes.MountPoint('e:/', 333)]
        self.target_vm = classes.Workload('192.0.0.1', self.target_credentials, 
                                                       self.target_storage)
        self.migration_target = classes.MigrationTarget("vcloud", self.cloud_credentials, 
                                                                  self.target_vm)
        self.migration = classes.Migration(self.selected_mount_points, 
                                           self.source, self.migration_target)

    def test_run_error_migration_volume_c_is_not_allowed(self):
        self.migration.disk_c_allowed = False
        self.migration.run()
        self.assertEqual(self.migration.migration_state, "error")

    def test_run_error_migration_selected_storages_are_absent(self):
        self.migration_abs = classes.Migration(self.selected_absent_mount_points, 
                                               self.source, self.migration_target)
        self.migration_abs.run()
        self.assertEqual(self.migration_abs.migration_state, "error")

    def parameter_matching_test(self):
        self.migration_abs = classes.Migration(self.selected_mount_points, 
                                               self.source, self.migration_target)
        self.migration_abs.run()
        self.assertEqual(self.migration_abs.migration_state, "success")
        self.assertEqual(self.target_vm.ip, self.source.ip)
        self.assertEqual(self.target_vm.credentials, self.source.credentials)
        self.assertEqual(self.migration_target.target_vm.credentials, self.selected_mount_points)

if __name__ == "__main__":
    unittest.main()