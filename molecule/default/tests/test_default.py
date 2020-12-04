import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


PACKAGE = 'saws'
PACKAGE_BINARY = '/usr/local/bin/saws'


def test_saws_binary_exists(host):
    """
    Tests if saws binary exists.
    """
    assert host.file(PACKAGE_BINARY).exists


def test_saws_binary_file(host):
    """
    Tests if saws binary is file type.
    """
    assert host.file(PACKAGE_BINARY).is_file


def test_saws_binary_which(host):
    """
    Tests the output to confirm saws's binary location.
    """
    assert host.check_output('which saws') == PACKAGE_BINARY
