from user import User
from admin import Admin, Privileges

my_user = Admin('dima','zhuravlev',26,'krasnodar',89183288814)

my_user.privileges.show_privileges()