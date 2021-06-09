import csv

with open('can_3days.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)
    for line in reader:
        with open('contact_can4.txt', 'a', ) as f:
            if len(line) > 3 and line[0] != 'Access':
                f.write('a contact' + ' ' +
                        line[1] + ' ' + line[2] + ' ' + '04' +' ' + '05' + ' ' + '160000' + ' ' + '0.1' + '\n')
                f.write('a contact' + ' ' +
                        line[1] + ' ' + line[2] + ' ' + '05' + ' ' + '04' + ' ' + '160000' + ' ' + '0.1')
            else: continue
            f.write('\n')
