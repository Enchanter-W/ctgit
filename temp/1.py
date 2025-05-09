import csv

# 输入txt文件路径
input_txt_file = 'E:\\Study\\Transformer_module\\6Vision\\temp\\res0.txt'
# 输出csv文件路径
output_csv_file = 'output.csv'

# 打开txt文件进行读取
with open(input_txt_file, 'r') as txt_file:
    # 打开csv文件进行写入
    with open(output_csv_file, 'w', newline='') as csv_file:
        # 创建csv写入对象
        csv_writer = csv.writer(csv_file)
        # 逐行读取txt文件内容
        for line in txt_file:
            # 去除每行的首尾空白字符（包括换行符等）
            line = line.strip()
            # 将处理后的行写入csv文件
            csv_writer.writerow([line])

print(f'已将{input_txt_file}转换为{output_csv_file}')