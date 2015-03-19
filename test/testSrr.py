#!/usr/bin/env python

import unittest
import os
import shutil
import json
gitgot = __import__('git-got')

class Utility:
  def loadGotConfiguration(self, root):
    file = open('%s/.got/storage' % root, 'r')
    configuration = json.load(file)
    file.close()
    return configuration

class TestBase(unittest.TestCase):
  def setUp(self):
    self.class_name = type(self).__name__
    try:
      shutil.rmtree('TestSrr-%s' % self.class_name)
    except OSError as e:
      # Expecting to see this the first time a test is run since the
      # directory won't exist
      pass
    assert os.system('git init TestSrr-%s' % self.class_name) == 0
    self.utility = Utility()
    self.command = 'init'
    self.version = 1
    self.remote_type = 'srr'

class TestInit(TestBase):
  def setUp(self):
    super(TestInit, self).setUp()

class TestInitSuccess(TestInit):
  def runTest(self):
    print "D:%s" % os.getcwd()
    os.chdir('TestSrr-%s' % self.class_name)
    try:
      remote = 'http://hq-gnitools/srr/12345'
      gitgot.main(['git-got.py', self.command, self.remote_type, remote]) == 0, 'Did not receive successful return code'
      assert os.path.exists('.got'), 'Got directory does not exist'
      assert os.path.isfile('.got/storage'), 'Got parameters were not persisted'
      configuration = self.utility.loadGotConfiguration('./')
      assert configuration['remote_type'] == self.remote_type, 'Configuration remote_type(%s) != %s' % (configuration['remote_type'], self.remote_type)
      assert configuration['version'] == self.version, 'Configuration version(%s) != %s' % (configuration['version'], self.version)
      assert configuration['remote'] == remote, 'Configuration remote(%s) != %s' % (configuration['remote'], remote)
    finally:
      print "E:%s" % os.getcwd()
      os.chdir('..')
    print "F:%s" % os.getcwd()

class TestInitDoubleInit(TestInit):
  def runTest(self):
    print "G:%s" % os.getcwd()
    os.chdir('TestSrr-%s' % self.class_name)
    try:
      remote = 'http://hq-gnitools/srr/12345'
      gitgot.main(['git-got.py', self.command, self.remote_type, remote]) == 0, 'Did not receive successful return code'
      assert os.path.exists('.got'), 'Got directory does not exist'
      assert os.path.isfile('.got/storage'), 'Got parameters were not persisted'
      configuration = self.utility.loadGotConfiguration('./')
      assert configuration['remote_type'] == self.remote_type, 'Configuration remote_type(%s) != %s' % (configuration['remote_type'], self.remote_type)
      assert configuration['version'] == self.version, 'Configuration version(%s) != %s' % (configuration['version'], self.version)
      assert configuration['remote'] == remote, 'Configuration remote(%s) != %s' % (configuration['remote'], remote)
      remote = 'http://hq-gnitools/srr/123456'
      gitgot.main(['git-got.py', self.command, self.remote_type, remote]) == 0, 'Did not receive successful return code'
      configuration = self.utility.loadGotConfiguration('./')
      assert configuration['remote_type'] == self.remote_type, 'Configuration remote_type(%s) != %s' % (configuration['remote_type'], self.remote_type)
      assert configuration['version'] == self.version, 'Configuration version(%s) != %s' % (configuration['version'], self.version)
      assert configuration['remote'] == remote, 'Configuration remote(%s) != %s' % (configuration['remote'], remote)
    finally:
      print "H:%s" % os.getcwd()
      os.chdir('..')
    print "I:%s" % os.getcwd()

class TestInitTooFewArguments(TestInit):
  def runTest(self):
    os.chdir('TestSrr-%s' % self.class_name)
    try:
      self.remote_type = 'srr'
      remote = 'http://hq-gnitools/srr/12345'
      gitgot.main(['git-got.py', self.command, self.remote_type]) != 0, 'Received successful return code'
      assert not os.path.exists('.got'), 'Got directory exists'
    finally:
      os.chdir('..')

class TestInitTooManyArguments(TestInit):
  def runTest(self):
    os.chdir('TestSrr-%s' % self.class_name)
    try:
      self.remote_type = 'srr'
      remote = 'http://hq-gnitools/srr/12345'
      gitgot.main(['git-got.py', self.command, self.remote_type, remote, "extraarg"]) != 0, 'Received successful return code'
      assert not os.path.exists('.got'), 'Got directory exists'
    finally:
      os.chdir('..')

class TestInitInvalidRemoteType(TestInit):
  def runTest(self):
    print "A:%s" % os.getcwd()
    os.chdir('TestSrr-%s' % self.class_name)
    try:
      self.remote_type = 'bad_type'
      remote = 'http://hq-gnitools/srr/12345'
      gitgot.main(['git-got.py', self.command, self.remote_type, remote]) != 0, 'Received successful return code'
      assert not os.path.exists('.got'), 'Got directory exists'
    finally:
      print "B:%s" % os.getcwd()
      os.chdir('..')
    print "C:%s" % os.getcwd()

class TestAdd(TestBase):
  def setUp(self):
    super(TestAdd, self).setUp()
    remote = 'http://hq-gnitools/srr/12345'
    gitgot.main(['git-got.py', self.command, self.remote_type, remote]) == 0, 'Received unsuccessful return code'

class TestAddNoFile(TestAdd):
  def runTest(self):
    pass
    
if __name__ == "__main__":
  os.environ['PYTHONPATH'] = '../src:' + os.environ['PYTHONPATH']
  unittest.main()
