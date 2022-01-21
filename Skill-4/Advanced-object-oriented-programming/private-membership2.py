from eddiemodule import CreateEmail

my_email = CreateEmail("eddie")
my_email.provider = ["spam.com", "spam.co.uk"]
print(my_email.generate())