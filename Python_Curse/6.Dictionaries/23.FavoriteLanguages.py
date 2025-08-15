
favorite_languages = {
  'jen': 'python',
  'sarah': 'c',
  'edward': 'rust',
  'phil': 'python',
  }

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

for name, language in favorite_languages.items():
  print(f"{name.title()}'s favorite language is {language.title()}")


for name in favorite_languages.keys():
  print(name.title())


friends = ['phil', 'sarah']
for name in favorite_languages.keys():
  print(f"Hi {name.title()}")

  if name in friends:
    language = favorite_languages[name].title()
    print(f"\t{name.title()}, I see you love {language}!")
    
if 'erin' not in favorite_languages.keys():
  print("Erin, please take our poll!")


for name in sorted(favorite_languages.keys()):
  print(f"{name.title()}, thank you for taking the poll.")

#values() method to return a sequence of values without any keys.
print("The following languages have been mentioned:")
for language in favorite_languages.values():
  print(language.title())


#A set is a collection in which each item must be unique
""" 
When you wrap set() around a collection of values that contains duplicate items, Python identifies the unique items in the collection and builds a 
set from those items.

"""
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
  print(language.title())

# sets do not retain items in any specific order.


#A list in a Dictionary

  favorite_languages = {
  'jen': ['python', 'rust'],
  'sarah': ['c'],
  'edward': ['rust', 'go'],
  'phil': ['python', 'haskell'],
  }

for name, languages in favorite_languages.items():
  print(f"\n{name.title()}'s favorite language are:")
  for language in languages:
    print(f"\t{language.title()}")