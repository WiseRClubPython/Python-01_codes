# -*- coding: utf-8 -*-
#!/usr/bin/env python
import sys, shelve

def storeperson(db):
	id = raw_input('Id:')
	person = {}
	person['name'] = raw_input('Name:')
	person['age'] = raw_input('Age:')
	person['mobile'] = raw_input('Mobile:')
	db[id] = person

def findperson(db):
	id = raw_input('Find by id:')
	field = raw_input('Field：')
	field = field.strip().lower()
	print field.capitalize() + ':' + db[id][field]

def entercommand():
	cmd = raw_input('Enter command:')
	cmd = cmd.strip().lower()
	return cmd

def main():
	db = shelve.open(r'E:\Project\Python\today\ex_file_store.dat')
	try:
		while True:
			cmd = entercommand()
			if cmd == 'store':
				storeperson(db)
			elif cmd == 'find':
				findperson(db)
			elif cmd == "quit":
				return
	finally:
		db.close()


if __name__ == '__main__': main()