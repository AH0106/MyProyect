



def build_profile(first, last, **user_info): 
  """Build a dictionary containing everything we know about a user."""
  user_info['first_name'] = first
  user_info['last_name'] = last
  return user_info

user_profile = build_profile('albert', 'einstein',
                                  location = 'princeton',
                                  fiel = 'physics')

print(user_profile)

""" 
The definition of build_profile() expects a first and last name, and then 
it allows the user to pass in as many name-value pairs as they want.

the double asterisks before the parameter **user_info cause Python to create 
a dictionary called user_info containing all the extra name-value pairs the 
function receives. 


"""

