#!/usr/bin/python3

from ansible.module_utils.basic import AnsibleModule
import pymysql


class MysqlSecureInstallation:
    def __init__(self, login_user, login_password, new_root_password, bool_disable_remote_root_login,
                 bool_remove_anonymous_user, bool_remove_test_db, bool_reload_privilege_table):
        self.login_user = login_user
        self.login_password = login_password
        self.new_root_password = new_root_password
        self.bool_disable_remote_root_login = bool_disable_remote_root_login
        self.bool_remove_anonymous_user = bool_remove_anonymous_user
        self.bool_remove_test_db = bool_remove_test_db
        self.bool_reload_privilege_table = bool_reload_privilege_table

        conn = pymysql.connect(host='localhost', user=self.login_user, password=self.login_password)
        self.cursor = conn.cursor()
        self.main()

    def main(self):
        if self.new_root_password is not None:
            self.change_root_password()
        if self.bool_disable_remote_root_login:
            self.disable_remote_root_login()
        if self.bool_remove_anonymous_user:
            self.remove_anonymous_user()
        if self.bool_remove_test_db:
            self.remove_test_database()
        if self.bool_reload_privilege_table:
            self.reload_privilege_table()

    def change_root_password(self):
        self.cursor.execute(f"ALTER USER 'root'@'localhost' IDENTIFIED BY '{self.new_root_password}';")

    def disable_remote_root_login(self):
        self.cursor.execute(
            "DELETE FROM mysql.user WHERE User='root' AND Host NOT IN ('localhost', '127.0.0.1', '::1')")

    def remove_anonymous_user(self):
        self.cursor.execute("DELETE FROM mysql.user WHERE User=''")

    def remove_test_database(self):
        self.cursor.execute('DROP DATABASE IF EXISTS test')

    def reload_privilege_table(self):
        self.cursor.execute('FLUSH PRIVILEGES')


def main():
    fields = {
        'login_user': {'default': 'root', 'type': 'str'},
        'login_password': {'required': True, 'type': 'str', 'no_log': True},
        'new_root_password': {'default': None, 'type': 'str', 'no_log': True},
        'disable_remote_root_login': {'default': True, 'type': 'bool'},
        'remove_anonymous_user': {'default': True, 'type': 'bool'},
        'remove_test_db': {'default': True, 'type': 'bool'},
        'reload_privilege_table': {'default': True, 'type': 'bool'},
    }

    module = AnsibleModule(argument_spec=fields)

    run = MysqlSecureInstallation(login_user=module.params['login_user'],
                                  login_password=module.params['login_password'],
                                  new_root_password=module.params['new_root_password'],
                                  bool_disable_remote_root_login=module.params['disable_remote_root_login'],
                                  bool_remove_anonymous_user=module.params['remove_anonymous_user'],
                                  bool_remove_test_db=module.params['remove_test_db'],
                                  bool_reload_privilege_table=module.params['reload_privilege_table'])

    module.exit_json(changed=True)


if __name__ == '__main__':
    main()
