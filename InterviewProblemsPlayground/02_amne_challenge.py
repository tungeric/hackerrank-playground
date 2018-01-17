# Sample Input
# 5 3
# 188930 194123 201345 154243 154243

# Sample Output
# 3
# 0
# -1


def run_challenge(filepath, output_filepath):
  input_file = open(filepath, 'r')
  input = input_file.read().split('\n')
  output_file = open(output_filepath, 'w')
  first_row = input[0].split()
  n, k = int(first_row[0]), int(first_row[1])
  prices = input[1].split()

  for idx in range(0, (n - k + 1)):
    set = prices[idx:idx + k]
    subs = subsets(set)
    net = 0
    for list in subs:
      net += check_set_net(list)
    output_file.write(f"{str(net)}\n")
  input_file.close()
  output_file.close()


def subsets(arr):
  results = []
  length = len(arr)
  for l in range(2, length + 1):
    for idx in range(0, (len(arr) - l + 1)):
      results.append(arr[idx:(idx + l)])
  return results


def check_set_net(arr):
  # +1 for increasing
  # -1 for decreasing
  # 0 for both or no change
  # 2 is a placeholder
  net = 2
  prev_num = int(arr[0])
  for idx in range(1, len(arr)):
    num = int(arr[idx])
    if (net == 1 and prev_num >= num) or (net == -1 and num >= prev_num):
      return 0
    elif ((net == 1 or net == 2) and prev_num < num):
      net = 1
    elif ((net == -1 or net == 2) and num < prev_num):
      net = -1
    elif ((net == 0 or net == 2) and num == prev_num):
      net = 0
    prev_num = num
  return net
