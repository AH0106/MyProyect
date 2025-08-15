

first_name = "ada"
last_name = "lovelace"

full_name = f"{first_name} {last_name}"

""" To insert a variable's value into a string, place the letter f before the 
opening quotation mark """


print(full_name)

print(f"Hello, {full_name.title()}!")
message = {'color': 'red',
            'points': '4'
          }

message = f"Hello, {full_name.title()}!"

print(message)


print("\tPython whit tab")

print("Newline in a string: \nLine1\nLine2\nLine3")


print("Newline with tabs: \n\tnewline with tab\n\tsecond line with tab")

""" Whitespaces """

string_whitespace_right = 'whitespace_in_right_side '

print(string_whitespace_right)


print("Print string without spaces")
print(string_whitespace_right.rstrip())


print("Eliminate whitespace permanently")

string = 'python'

string = string.rstrip()

print(string)

""" left side """

word = ' python '

word = word.rstrip()
word = word.lstrip()

""" Eliminate prefix """


url_example = 'https://eliminate_prefix.com'

print('\nurl_example')

url_example.removeprefix('https://')
print(url_example)




