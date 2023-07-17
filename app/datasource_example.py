blocklist = set()  # In-memory token blacklist

user_data = {
    'alan@mail.com': { # user mail address
        'password': 'P@ssw0rd1'
    },
    'john@mail.com': {
        'password': 'P@ssw0rd1'
    }
}

mail_data = {
    'mail1' : { # mail id
        'sender': 'alan@mail.com',
        'receiver': 'john@mail.com',
        'subject': 'Greeting from Alan',
        'body': 'Hello John'
    },
    'mail2': { # mail id
        'sender': 'john@mail.com',
        'receiver': 'alan@mail.com',
        'subject': 'Greeting reply from John',
        'body': 'Hi Alan, how are you?'
    },
    'mail3': { # mail id
        'sender': 'alan@mail.com',
        'receiver': 'john@mail.com',
        'subject': 'Informing my condition',
        'body': 'I am good and healthy'
    },
}