print("hello")

def lalchand():
    "function doc string"
    print("i want to learn python")
    print("i am doing it")
    return
lalchand()

print("__________")

lalchand()

def greetings( Name ):
    "function doc strting"
    print("Hello,", Name)
    return
greetings("lalchand")

# def user_creation(name, email, phone):
def user_creation(name, email, phone=0):
    print("Name: ", name)
    print("email: ", email)
    print("Mobile: ", phone)
    return
# user_creation("lalchand", "lalchandrajak03@gmail.com", 9082447475)
user_creation("lalchand", "lalchandrajak03@gmail.com", )
