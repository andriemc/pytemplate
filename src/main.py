def sayHello(name: str):
	print('Hello, ' + name);

name = input('Name: ');
if name:
	sayHello(name);
else:
	print('You don\'t have a name, I guess?');
