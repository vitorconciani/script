#!/usr/bin/env python3
import pwd

#lista todos os usuários do sistema

for user in pwd.getpwall():
    print(user.pw_name)

    