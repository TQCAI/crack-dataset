import os

if __name__ == '__main__':
    for root, dirs, files in os.walk('./'):
        for file in files:
            if file.find('.jpg')>=0:
                new_file=file.replace('.jpg','_gt.jpg')
                os.system(f'mv {file} {new_file}')
        break