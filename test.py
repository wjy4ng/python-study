class App():
    def __init__(self):
        self.name = "양원준"
        self.age = 24
        self.job = "student_in_KNU대학이다"
    
    def print_test(self):
        print("test입니다")

    def introduction(self):
        print(f"제 이름은 {self.name}이고, 나이는 {self.age}입니다.")

    def myjob(self):
        print(f"제 직업은 {self.job}입니다.")


if __name__=="__main__":
    app = App()
    app.print_test()
    app.introduction()
    app.myjob