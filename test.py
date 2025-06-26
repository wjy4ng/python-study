class App():
    test_id = 1

    def __init__(self):
        self.id = App.test_id
        App.test_id += 1
    
    def print_test(self):
        print(f"test id : {self.id}")


if __name__=="__main__":
    app1 = App()
    app2 = App()

    app1.print_test()
    app2.print_test()

