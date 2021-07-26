from tasks import reverse

response = reverse.delay("hello world")
print(response)
print(response.get())
