import os
import re
import shutil
import pandas as pd

directory = 'weratedogs'
new_directory = 'data'

if not os.path.exists(new_directory):
        os.makedirs(new_directory)

df = pd.DataFrame(columns=['doggo_index','doggo_rating', 'comment'])
i = 0
for filename in os.listdir(directory):
    if filename.endswith('.txt'):
        root = filename[:-4]
        f = open(f'{directory}/{filename}', "r")
        txt = f.read()
        txt_og = txt
        txt_og = txt_og.replace('\n', ' ')
        txt_og = txt_og.replace('\t', ' ')
        matches = re.findall(' ([0-9]*)\/10', txt)
        print(txt)
        if matches != []:
            rating = matches[0].split('/')[0]
            im_no_suffix = root + '.jpg'
            if os.path.isfile(f'{directory}/{im_no_suffix}'):
                shutil.copy(f'{directory}/{im_no_suffix}', f'{new_directory}/{i:05d}.jpg')
                row = pd.DataFrame([[f'{i:05d}', rating, txt_og]], columns=df.columns)
                df = pd.concat([row,df], ignore_index=True)
                i += 1
            else:
                im_suffix = root + '_1.jpg'
                if os.path.isfile(f'{directory}/{im_suffix}'):
                        shutil.copy(f'{directory}/{im_suffix}', f'{new_directory}/{i:05d}.jpg')
                        row = pd.DataFrame([[f'{i:05d}', rating, txt_og]], columns=df.columns)
                        df = pd.concat([row,df], ignore_index=True)
                        i += 1
                else:
                    print('image file could not be found for: {root}')
        else:
             print(txt)
            
print(f'{i} good doggos found')
print(df)
df.to_csv('doggo_ratings.tsv', sep="\t", index=False)