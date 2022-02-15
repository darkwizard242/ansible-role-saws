[![build-test](https://github.com/darkwizard242/ansible-role-saws/workflows/build-and-test/badge.svg?branch=master)](https://github.com/darkwizard242/ansible-role-saws/actions?query=workflow%3Abuild-and-test) [![release](https://github.com/darkwizard242/ansible-role-saws/workflows/release/badge.svg)](https://github.com/darkwizard242/ansible-role-saws/actions?query=workflow%3Arelease) ![Ansible Role](https://img.shields.io/ansible/role/49319?color=dark%20green%20) ![Ansible Role](https://img.shields.io/ansible/role/d/49319?label=role%20downloads) ![Ansible Quality Score](https://img.shields.io/ansible/quality/49319?label=ansible%20quality%20score) [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-saws&metric=alert_status)](https://sonarcloud.io/dashboard?id=ansible-role-saws) [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-saws&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=ansible-role-saws) [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-saws&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=ansible-role-saws) [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-saws&metric=security_rating)](https://sonarcloud.io/dashboard?id=ansible-role-saws) ![GitHub tag (latest SemVer)](https://img.shields.io/github/tag/darkwizard242/ansible-role-saws?label=release) ![GitHub repo size](https://img.shields.io/github/repo-size/darkwizard242/ansible-role-saws?color=orange&style=flat-square)

# Ansible Role: saws

Role to install [saws](https://github.com/donnemartin/saws) pip package on **Debian/Ubuntu** systems. **saws** is a supercharged AWS CLI.

## Requirements

None.

## Role Variables

Available variables are listed below (located in `defaults/main.yml`):

### Variables List:

```yaml
saws_debian_pre_reqs:
  - python3
  - python3-pip
saws_debian_pre_reqs_desired_state: present
saws_pip_executable: pip3
saws_app_debian_package: saws
saws_desired_state: present
```

### Variables table:

Variable                           | Description
---------------------------------- | ----------------------------------------------------------------------------------------------------------------
saws_debian_pre_reqs               | Packages required to install **saws** on Debian based systems. Using python3 as python2.x is EOL by end of 2020.
saws_debian_pre_reqs_desired_state | Desired state for **saws** pre-requisite apps on Debian systems.
saws_pip_executable                | The executable to utilize for installing **pip** package of `saws`.
saws_app_debian_package            | Name of saws application package require to be installed i.e. `saws` on Debian based systems.
saws_desired_state                 | Desired state for **saws**.

## Dependencies

None

## Example Playbook

For default behaviour of role (i.e. installation of **saws** package) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.saws
```

For customizing behavior of role (i.e. installation of latest **saws** package instead of ensure it is installed ) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.saws
  vars:
    saws_desired_state: latest
```

For customizing behavior of role (i.e. removal of **saws** package) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.saws
  vars:
    saws_desired_state: absent
```

## License

[MIT](https://github.com/darkwizard242/ansible-role-saws/blob/master/LICENSE)

## Author Information

This role was created by [Ali Muhammad](https://www.alimuhammad.dev/), a DevOps/CloudOps Engineer who loves to learn and contribute to Open Source community.
