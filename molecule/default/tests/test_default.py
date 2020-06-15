import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_saws_binary_exists(host):
    assert host.file('/usr/local/bin/saws').exists


def test_saws_binary_file(host):
    assert host.file('/usr/local/bin/saws').is_file


def test_saws_binary_which(host):
    assert host.check_output('which saws') == '/usr/local/bin/saws'
