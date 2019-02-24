# parental-controls
Control what programs your kids can and can't access  
To install run `python3 install.py`  
To add rules
```bash
# parent {-a/--add} {user} {program}
```  
For example:  
`# parent -a joe mars-shooter`  
To remove rules
```bash
# parent {-r/--remove} {user} {program}
```  
For example:  
`# parent -r sally endless-sky`  
** Note if program is omitted then all entries for the given user will be deleted **  
Now you can what your child's frustration with such joy as they try to access these programs
