with open('test_two.txt') as file:
    file_lines = file.readlines()
    s_count = 0
    for num, line in enumerate(file_lines):
        w_count = len(line.split())
        s_count += 1
        print(f'#{num + 1} - {w_count} words')