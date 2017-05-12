#!/usr/bin/python3
#written by oostkust@protonmail.com
#

from string import printable
from itertools import product
import crypt
import sys

found = False
count = 0

hash_field = input("Copy and paste the encrypted password field from your /etc/shadow file")
split_field = hash_field.split("$")
salt_field = "$" + split_field[1] + "$" + split_field[2]

for length in range(10, 16):
	password_to_attempt = product(printable, repeat=length)

	for attempt in password_to_attempt:

		attempt = ''.join(attempt)
		hash_user = crypt.crypt(attempt, salt_field)

		if hash_field == hash_user:
			print("\nYour password is: " + attempt)
			break

		count += 1
		sys.stdout.write("Attempt: %d   \r" % (count))
		sys.stdout.flush()

	if hash_field == hash_user:
		break

