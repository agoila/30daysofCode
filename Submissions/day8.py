num_entries = int(input())
name_dir = []
unk_dir = []
for _ in range(1, num_entries + 1):
    name_dir.append(input())
    
while True:
    try:
        unk_dir.append(input())
    except EOFError:
        break

name = [name_dir[i].split(' ')[0] for i in range(len(name_dir))]
ph_no = [name_dir[i].split(' ')[1] for i in range(len(name_dir))]

ph_dict = {n: p for n, p in zip(name, ph_no)}

for name in unk_dir:
    if name in ph_dict:
        print('{}={}'.format(name, ph_dict[name]))
    else:
        print('Not found')