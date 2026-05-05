def extract_lines_from_file(line_numbers_file, target_file, output_file):
    # 读取行号文件
    with open(line_numbers_file, 'r') as f:
        line_numbers = [int(line.strip()) for line in f.readlines()]

    # 读取目标文件
    with open(target_file, 'r') as f:
        target_lines = f.readlines()

    # 提取对应行
    extracted_lines = [target_lines[line_num - 1].strip() for line_num in line_numbers if
                       0 < line_num <= len(target_lines)]

    # 将结果写入输出文件
    with open(output_file, 'w') as f:
        for line in extracted_lines:
            f.write(line + '\n')


def main():
    line_numbers_file = './annotation/2'
    target_file = './annotation/WildDeepfake_test.txt'
    output_file = './annotation/4.txt'

    extract_lines_from_file(line_numbers_file, target_file, output_file)


if __name__ == '__main__':
    main()