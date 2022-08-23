import os
gitClone_url = input("Enter The Repo URl: ")
bit_url = gitClone_url.replace('git clone','')
print(bit_url)

# bit_url = input('Enter bit repo url')
#os operations
os.system('git init')
os.system('git add .')
os.system('git status')
os.system('git commit -m "Initial Commit"')
os.system('git remote add origin'+bit_url )
os.system('git push -f origin master')

print('\n task completed')


