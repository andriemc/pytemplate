def sayHello(name: str):
	print('Hello, ' + name);

name = input('Name: ');
if name:
	sayHello(name);
else:
	print('You don\' have a name, I guess?');