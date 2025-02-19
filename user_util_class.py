class UserUtil:
    @staticmethod
    def generate_user_id():
        year_prefix = str(datetime.date.today().year)[-2:]
        random_digits = ''.join(random.choices(string.digits, k=7))
        return int(year_prefix + random_digits)
    
    @staticmethod
    def generate_password():
        characters = (
            random.choice(string.ascii_uppercase) +
            random.choice(string.ascii_lowercase) +
            random.choice(string.digits) +
            random.choice(string.punctuation) +
            ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=4))
        )
        return ''.join(random.sample(characters, len(characters)))
    
    @staticmethod
    def is_strong_password(password):
        return (
            len(password) >= 8 and
            any(c.isupper() for c in password) and
            any(c.islower() for c in password) and
            any(c.isdigit() for c in password) and
            any(c in string.punctuation for c in password)
        )
    
    @staticmethod
    def generate_email(name, surname, domain):
        return f"{name.lower()}.{surname.lower()}@{domain}"
    
    @staticmethod
    def validate_email(email):
        pattern = r'^[a-z]+\.[a-z]+@[a-z]+\.[a-z]+$'
        return re.match(pattern, email) is not None