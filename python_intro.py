print('Hello Python')

if 3 > 2:
	print('It works!')
	
if 5 > 2:
    print('5 is indeed greater than 2')
else:
    print('5 is not greater than 2')

# function
def hi():
    print('Hi there!')
    print('How are you?')

hi()

def my(name):
    if name == 'Ola':
        print('Hi Ola!')
    elif name == 'Sonja':
        print('Hi Sonja!')
    else:
        print('Hi anonymous!')

my('Ola')
my("Sonja")

#list array
girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'You']

#loop for
for name in girls:
	my(name)
	print('Next girls')
	
for i in range(1, 6):
    print(i)