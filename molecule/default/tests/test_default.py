import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_java_is_installed(host):
    package = host.package('java-1.8.0-openjdk')

    assert package.is_installed


def test_yacy_user(host):
    user = host.user('yacy')

    assert user.exists
    assert user.shell == '/usr/sbin/nologin'
    assert user.group == 'yacy'


def test_yacy_install_dir(host):
    f = host.file('/opt/yacy-1.92_20161226_9000')

    assert f.is_directory
    assert f.user == 'yacy'
    assert f.group == 'yacy'


def test_yacy_dir(host):
    f = host.file('/opt/yacy')

    assert f.is_symlink
    assert f.linked_to == '/opt/yacy-1.92_20161226_9000'
    assert f.user == 'yacy'
    assert f.group == 'yacy'


def test_yacy_systemd_unit_file(host):
    f = host.file('/etc/systemd/system/yacy.service')

    assert f.is_file


def test_yacy_running_and_enabled(host):
    yacy = host.service('yacy')

    assert yacy.is_running
    assert yacy.is_enabled
