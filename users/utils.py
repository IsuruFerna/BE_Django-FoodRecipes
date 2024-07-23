from faker import Faker

class ResponseUser():
    def __init__(self, id, username, first_name, last_name, email):
        self.id = id
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

# generates users
def user_generator():
    faker = Faker()
    return {
        'email': faker.email(),
        'first_name': faker.first_name(),
        'last_name': faker.last_name(),
        'username': faker.user_name(),
        'password': faker.password()
    }
