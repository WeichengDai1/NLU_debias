
import json
file_dir_lis = ['/home/luoyao/1012/GLOVE_data/2018-Valence-oc-En-dev.txt',
                '/home/luoyao/1012/GLOVE_data/2018-Valence-oc-En-train.txt',
                '/home/luoyao/1012/GLOVE_data/2018-Valence-oc-En-test.txt'
                ] 

for file_dir in file_dir_lis:
    f = open(file_dir, 'r')
    out = open(f"/home/luoyao/1012/GLOVE_data/{file_dir.strip('.txt').split('/')[-1]}.jsonl", 'w')
    all_ratings = []
    for line in f.readlines():
        if line[:2] == '20': ## get rid of first line
            line = line.strip('\n').strip('\t').split('valence')
            # if file_dir.strip('.txt').split('-')[-1]!='test':
            try:
                rating = line[1].strip().strip('\t').split(':')[0] ## eg. -2
            except:
                # print(f"file_dir = {file_dir}, line = {line}")
                rating = 'None'
            all_ratings.append(rating)
            sentence = line[0].strip().strip('\t').split('\t')[-1]
            newline = {"label": rating,
                        "text": sentence}
            out.write(json.dumps(newline) + "\n")
            # print(f"sentence = {sentence}, rating = {rating}")
    print(f"Finished processing {file_dir}, unique ratings = {set(all_ratings)}")
            