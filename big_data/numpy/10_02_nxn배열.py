import numpy as np

class App():
    def __init__(self):
        self.SIZE = np.random.choice([8,12,16,20])
        self.random_list = np.arange(1, self.SIZE*self.SIZE+1)
        self.random_list = self.random_list.reshape(self.SIZE, self.SIZE)

    def run(self):
        print(self.random_list)

        self.half = self.SIZE//2
        self.list2 = self.random_list[self.half:, self.half:]

        print(self.list2)

if __name__=="__main__":
    app = App()
    app.run()
