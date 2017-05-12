from __future__ import print_function
from string import printable
from itertools import product
import crypt
import sys

found = False
count = 0

salt = raw_input("Enter string up to(not including the third '$'  like so:($.$.........):")

user_hash = raw_input("Enter the remaining random string(your hashed password):")

for length in range(10, 16):
    password_to_attempt = product(printable, repeat=length)

    for attempt in password_to_attempt:
        
        attempt = ''.join(attempt)
        hash_user = crypt.crypt(attempt, salt)
        salted_hash = (salt + "$" + user_hash)
        if salted_hash == hash_user:
            print("Your password is: " + attempt)
            break
        
        
        count += 1
        
        sys.stdout.write("Attempt: %d   \r" % (count))
        sys.stdout.flush()
        

    if salted_hash == hash_user:
        break