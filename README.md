### Airbnb Clone : The console.

#### Description
> This is the first phase of the Airbnb Clone: the console.
> This repository holds a command interpreter and classes (i.e. BaseModel class
> and several other classes that inherit from it
> and a command interpreter.

#### How to Use Command Interpreter
---
| Commands  | Sample Usage                                  | Functionality                              |
| --------- | --------------------------------------------- | ------------------------------------------ |
| `help`    | `help`                                        | displays all commands available            |
| `create`  | `create <class>`                              | creates new object (ex. a new User, Place) |
| `update`  | `User.update('123', {'name' : 'Greg_n_Mel'})` | updates attribute of an object             |
| `destroy` | `User.destroy('123')`                         | destroys specified object                  |
| `show`    | `User.show('123')`                            | retrieve an object from a file, a database |
| `all`     | `User.all()`                                  | display all objects in class               |
| `count`   | `User.count()`                                | returns count of objects in specified class|
| `quit`    | `quit`                                        | exits                                      |

#### Installation
```
git clone git@github.com:gjdame/AirBnB_clone.git
cd AirBnB_clone
```
#### Usage
Interactive Mode
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$
```
Non-Interactive Mode
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
```


### Environment
* Language: Python 3.8.5 (and C )
* OS: Ubuntu 20.04 LTS
* Compiler: python3  (and gcc 9.3.0)
* Style guidelines: [Pycodestyle] (https://github.com/PyCQA/pycodestyle)

### Authors
SYLLA Yacouba [![M](https://fr.m.wikipedia.org/wiki/Fichier:LinkedIn_logo_initials.png)](https://www.linkedin.com/in/sylla-yacouba-a2115b64/)
Aminata Adja BOUNDI [![M](https://fr.m.wikipedia.org/wiki/Fichier:LinkedIn_logo_initials.png)](https://www.linkedin.com/in/aminata-adja-boundi-b22b526a/)