import unittest
import testinfra
import pytest

#hosts = "docker://test_instance"
@pytest.mark.usefixtures("server")
class TestUser(unittest.TestCase):

    def setUp(self):
        #self.host = testinfra.get_host(hosts)
        pass

    def test_user(self):
        assert self.host.user("hello").exists

    def test_ssh_bash_profile(self):
        assert self.host.file("/home/hello/.bash_profile").exists

    def test_ssh_public_key(self):
        assert self.host.file("/home/hello/.ssh/id_rsa.pub").exists
        assert self.host.file("/home/hello/.ssh/id_rsa.pub").mode == 0o644
#if __name__ == "__main__":
#    unittest.main()
