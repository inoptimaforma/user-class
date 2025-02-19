if __name__ == "__main__":
    name = input("Write your name: ")
    surname = input("Write your surname: ")
    birth_year = int(input("Write birth year: "))
    birth_month = int(input("Write birth month: "))
    birth_day = int(input("Write birth day: "))
    birthday = datetime.date(birth_year, birth_month, birth_day)
    
    email = input("Write email: ")
    password = input("Write password: ")
    while not UserUtil.is_strong_password(password):
        print("Password is not strong.")    
    
    user_id = UserUtil.generate_user_id()
    new_user = User(user_id, name, surname, email, password, birthday)
    UserService.add_user(new_user)
    
    print("Your ID was successfully created!")
    print(new_user.get_details())
