import statistics
acc_list = []

with open('output', 'r') as f:
    lines = (line.strip() for line in f if (line and not line[0].islower()))
    acc_list = [float(line) for line in lines]

# file_in = open('output', 'r')
# for line in file_in.readlines():
#     if line:
#         print(line)
#         if line.isdigit():
#             acc_list.append(float(y))

print(len(acc_list))
# for acc in acc_list:
#     print(acc)

num_dataset = 15
num_trials = 5
num_grid_search = 4

for i in range(num_dataset):
    max_acc = 0
    std_dev = 0
    for j in range(num_grid_search):
        acc_now = []
        for k in range(num_trials):
            # print(i)
            # print(j)
            # print(k)
            # print(i*num_dataset*num_grid_search + j*num_grid_search + k)
            # print(acc_list[i*num_dataset + j*num_grid_search + k])
            acc_now.append(acc_list[i*num_trials*num_grid_search + j*num_grid_search + k])
        mean_acc = sum(acc_now) / len(acc_now)
        std = statistics.stdev(acc_now)
        if mean_acc > max_acc:
            max_acc = mean_acc
            std_dev = std
    max_acc = max_acc * 100
    std_dev = std_dev * 100
    # print(f"\\textbf{{{max_acc:.4f}±{std_dev:.4f}}}")
    print(f"{max_acc:.2f}±{std_dev:.2f}")

