#random number generator file for a secret santa project

import random

# creating lists for dataframe
family = ['wife', 'Me', 'Dad', 'Mom', 'sibling3', 'sibling4', 'sibling2']
family_emails = ['wifeemail@gmail.com', 'myemail@gmail.com', 'dademail@gmail.com', 'momemail@gmail.com', 'sibling3email@gmail.com', 'sibling4email@gmail.com', 'sibling2email@gmail.com']
number_list = [num for num in range(0,len(family))]

# creating empty dict
family_dict = {}

#populating dict w/ emails + numbers which will be used
for number in number_list: 
  family_dict[family[number]] = {'email': family_emails[number], 'number': number_list[number]+1, 'new_num': None}

# while loop which first assigns a random number from the number list over to the people in the family dict. If the number is the same then it'll fail the test at the bottom to break the loop
while True:
  helper_number = len(family) - 1
  new_num_list = [num for num in range(0,len(family))]
  for number in number_list:
    random_num = random.randint(0,helper_number)
    family_dict[family[number]]['new_num'] = new_num_list.pop(random_num) + 1
    helper_number = helper_number - 1
  if all(v["number"] != v["new_num"] for v in family_dict.values()):
    break

# prints out succesful assignments for secret santa, could theoretically use these + emails to assign people their person
for k, v in family_dict.items():
  print(f"{k} key {v} value")
