import csv

class App():
    def __init__(self):
        pass

    def run(self):
        with open("../10주차/singer.csv", "r") as in_file:
            with open("../10주차/singer3.csv", "w") as out_file:
                # header
                csv_reader = csv.reader(in_file)
                header_list = next(csv_reader)
                idx1 = header_list.index('이름')
                idx2 = header_list.index('유튜브 조회수')

                header_list = [header_list[idx1], header_list[idx2]]
                header_str = ','.join(header_list)
                out_file.writelines(header_str)
                out_file.write('\n')

                # body
                for row_list in csv_reader:
                    youtube = int(row_list[idx2].replace(',', ''))
                    row_list[idx2] = str(int(youtube/10000)) + "만"
                    row_list = [row_list[idx1], row_list[idx2]]
                    row_str = ','.join(row_list)

                    out_file.writelines(row_str)
                    out_file.write('\n')

    def print_list(self, list):
        pass

if __name__=="__main__":
    app = App()
    app.run()

