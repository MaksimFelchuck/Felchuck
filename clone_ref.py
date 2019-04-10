import sys
import subprocess
import os
def clone_ref(rep, ref, dir):
    subprocess.run('git clone {0} -b {1} {2}'.format(rep,ref, dir))

    return True
def clone_repo(rep, commit_id, dir):
    subprocess.run('git clone {0} {1}'.format(rep,dir))
    if commit_id != '':
        os.chdir(dir)
        FNULL = open(os.devnull, 'w')
        subprocess.run('git reset {0}'.format(commit_id),stdout=FNULL)
        subprocess.run('git stash',stdout=FNULL)


    return True

if '__main__':
    if sys.argv[1] == '--help':
        print('''
usage:      [-r]  <ref>  <commit_id> <dir>   
            <link>[<args>]<dir>
            
    -r                  Download repository on branch
    <ref>               Branch name
    <commit_id>         Commit's id(hash)
    <dir>               The directory in which the repository will be installed (required) 
        ''')

    repo = sys.argv[1]
    try:

        if sys.argv[2] == '-r':
            mode = '-r'

            try:
                ref = sys.argv[3]
                dir = sys.argv[4]
                clone_ref(repo, ref, dir)
            except:
                print ('fatal:directory or branch not specified')

        else:
            commit_id = sys.argv[2]
            dir = sys.argv[3]
            clone_repo(repo, commit_id, dir)

    except:
        try:
            dir = sys.argv[2]
            clone_repo(repo,'',dir)
        except:
            print("""
usage:      [-r]  <ref>  <commit_id> <dir>   
            <link>[<args>]<dir>

--help to learn more
                
        """)




#af696919d867d9d55e618d3307dc6293baa2fb2b