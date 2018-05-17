##python strings exmaples and tips
singleQuotes = 'Hello World'

doubleQuotes = "Hello World"
doubleWithSingleInside = "Welcome to mother's day"

rawString = r'This is a raw string.\nIt ignores scape characters'

multiLine = """This can be used 
in various lines.
Awesome!"""

print (singleQuotes)
print(doubleQuotes)
print(doubleWithSingleInside)
print(rawString)
print(multiLine)

#String methods

spam = 'Hello World!'
spam = spam.upper()
print(spam)
print (str(spam.isupper()))
print(spam)
spam = spam.lower()
print(str(spam.islower()))

######Join and Split
joinEx = ', '.join(['cats', 'bats', 'rats'])
print(joinEx)
splitEx = 'My name is Mozart'.split()
print(splitEx)
emailsList = "mwsa@cin.ufpe.br,mozart.almeida@ati.pe.gov.br,josea@ati.pe.gov.br".split(',')
print(emailsList)

for i in range(0, len(emailsList)):
    login = emailsList[i].split('@')
    uo = login[1].split('.')
    print('Login: ' + login[0] + ' UO: ' + uo[0])

######rjust, ljust and center
name = 'mozart'
name = name.rjust(20)
print(name)
name = 'william'
name = name.ljust(20)
print(name)
print('mozart william'.center(20))

#####strip, rstrip and lstrip
print('mozart william'.center(20).strip())
print('mozart william'.center(20).rstrip())
print('mozart william'.center(20).lstrip())

#replace
spam = 'Hello there!'
print(spam.replace('e', 'XYZ'))

