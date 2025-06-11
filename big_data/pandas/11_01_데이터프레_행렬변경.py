import pandas as pd

class App():
    def __init__(self):
        data = {'이름': ['여자친구','소녀시대','레드벨벳','에이핑크','마마무'],
                '인원': [6,8,4,6,4],
                '데뷔 일자': ['2015.01.15','2007.08.02','2014.08.01','2011.02.10','2014.06.19']}
        
        self.data_list = pd.DataFrame(data, index=['WMN','GRL','RED','APN','MMU'])

    def run(self):
        print(self.data_list)
        print("---------------------------")
        self.result = self.data_list.drop(['GRL','RED','APN'], axis=0)
        self.result = self.result.drop(['이름'], axis=1)
        self.result.loc['ABC'] = {'인원':1, '데뷔 일자': '2023.03.03'}
        print(self.result)

if __name__=="__main__":
    app = App()
    app.run()
