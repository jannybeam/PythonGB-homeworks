result = {}
with open('test_six.txt') as file:
    file_lines = file.readlines()
    for line in file_lines:
        data = line.split()
        hours = 0
        for sth in data[1:]:
            if sth != '-':
                num = '0'
                for a in sth:
                    if a.isdigit():
                        num += a
                    else:
                        break
                hours += int(num)
        result.update({data[0].strip(':'): hours})
print(result)


