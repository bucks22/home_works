import multiprocessing
from datetime import datetime

def read_info(name):

    with open(name, 'r') as file:
        all_data = []
        for line in file:
            file.readline()
            all_data.append(line)


filenames = [f'./file {number}.txt' for number in range(1, 5)]

start = datetime.now()
for file in filenames:
    read_info(file)
stop = datetime.now()
print(stop - start)

# if __name__ == '__main__':
#     start = datetime.now()
#     with multiprocessing.Pool(processes=4) as pool:
#         pool.map(read_info, filenames)
#
#     stop = datetime.now()
#     print(stop - start)


