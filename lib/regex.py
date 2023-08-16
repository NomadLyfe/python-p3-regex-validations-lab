import re

# NOTE: There are only a few tests included, so multiple solutions will work.
# Feel free to encourage students to find oversights and add tests to this lab!

name = r"[A-Z][^0-9][\w|\W|0-9]{3}[^\s][\w|\W|0-9]{1,}"
name_regex = re.compile(name)

phone_number = r"[0-9|\W]{4}[^\-][0-9|\W]{5,}"
phone_regex = re.compile(phone_number)

email_address = r"(?=[^.]*\.)(?=[^$]*@[^$]*$)(?=[^@]*@[^@]*$)[^0-9][\w|\W|0-9]{1,}"
email_regex = re.compile(email_address)
