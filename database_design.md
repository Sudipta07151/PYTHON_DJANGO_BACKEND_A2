------------
ModelLists
------------
id: INT
author: INT(FOREIGN KEY [User])
title: STR
description: STR
data: DATE
snippet:BOOL[false]
snippet:STR['']

__________________________________________________

-------
User
-------
id:INT
email: STR
user:STR
password:STR
photo:STR


