import os
import sys


TARGET_FILE_NAME = '___.py'


target_file_path = 'projects/{}'.format(TARGET_FILE_NAME)
print('SAVING {} AS {}...'.format(__file__, target_file_path))

# remove target file if it already exists
try:
    os.remove(target_file_path)
except:
    print('CREATING NEW {}...'.format(target_file_path))

# rename current file to target file
os.rename(
    __file__,
    target_file_path)

# remove file content after "# EOF"
with open(target_file_path, 'r') as f:
    file_content = f.read()
file_content = file_content.split('# EOF')[0]
with open(target_file_path, 'w') as f:
    f.write(file_content)

# list projects/ directory before exiting
print(os.listdir('projects'))
print('{} SAVED!'.format(target_file_path))
sys.exit()