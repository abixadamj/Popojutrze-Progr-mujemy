class Dog:
    def __init__(self, breed: str):
        self.breed = breed
        self.age = 0
        self.mass = 1
        print(f"Object ID={id(self)} has been created")

    def __del__(self):
        print(f"Object ID={id(self)} has been deleted")

    def about(self):
        print(f"Hello, I am {self.age} years old and I weigh {self.mass}.")
        print(f"My breed is: {self.breed}")

    def update_age(self, new_age: int):
        data_type = type(new_age)
        if data_type is int:
            self.age = new_age
        else:
            print(f"Sorry, bad type of data: {data_type} for 'age' property.")


kunegunda = Dog("Ratonero")
bethoven = Dog("Hovawart")
print("--------------------------")

print("Properties of kunegunda")
print(dir(kunegunda))
print("--------------------------")
print("Properties of bethoven")
print(dir(bethoven))
print("--------------------------")
