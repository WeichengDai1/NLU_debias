
import json
import random 
import os
import numpy as np

random.seed(1234)

base_data_saveto_dir = '/home/luoyao/1012/GLOVE_data/'

'''
split xxx-dev.txt into half/half
'''
dev_dir = os.path.join(base_data_saveto_dir, '2018-Valence-oc-En-dev-before.txt')
out = open(os.path.join(base_data_saveto_dir, 'test.jsonl'), 'w')
def choose_line(file_name): 
    '''
    split a .txt file into half/half using random
    '''
    file = open(file_name, 'r')
    lines = file.readlines() 
    total_num_lines = len(lines)
    print(f"total number of lines = {total_num_lines}")
    random_line = random.sample(lines, total_num_lines//2) 
    remain_line = list(set(lines) - set(random_line))

    return random_line, remain_line

test_lines, dev_lines = choose_line(dev_dir)
with open(os.path.join(base_data_saveto_dir, '2018-Valence-oc-En-test.txt'), 'w') as f:
    for line in test_lines:
        f.write(f"{line}")
with open(os.path.join(base_data_saveto_dir, '2018-Valence-oc-En-dev.txt'), 'w') as f:
    for line in dev_lines:
        f.write(f"{line}")
        
'''
tranform 3 files of .txt into .jsonl
'''
file_dir_lis = [os.path.join(base_data_saveto_dir, '2018-Valence-oc-En-dev.txt'),
                os.path.join(base_data_saveto_dir, '2018-Valence-oc-En-train.txt'),
                os.path.join(base_data_saveto_dir, '2018-Valence-oc-En-test.txt')
                ] 

for file_dir in file_dir_lis:
    f = open(file_dir, 'r')
    out = open(os.path.join(base_data_saveto_dir, f"{file_dir.strip('.txt').split('/')[-1]}.jsonl"), 'w')
    all_ratings = []
    for line in f.readlines():
        if line[:2] == '20': ## get rid of first line
            line = line.strip('\n').strip('\t').split('valence')
            # if file_dir.strip('.txt').split('-')[-1]!='test':
            try:
                rating = str(np.sign(int(line[1].strip().strip('\t').split(':')[0]))) ## eg. -2
            except:
                print(f"file_dir = {file_dir}, line = {line}")
                rating = 'None'
            all_ratings.append(rating)
            sentence = line[0].strip().strip('\t').split('\t')[-1]
            newline = {"label": rating,
                        "text": sentence}
            out.write(json.dumps(newline) + "\n")
            # print(f"sentence = {sentence}, rating = {rating}")
    print(f"Finished processing {file_dir}, unique ratings = {set(all_ratings)}")