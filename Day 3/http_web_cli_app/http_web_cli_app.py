import requests

print('  ===============================================================')
print('         WELCOME TO THE DIKU OPEN CONSOLE FOR GITHUB - D.O.C.G ')
print('  ===============================================================')
print('  Do you have a GitHub Account?\n')
print('  1 - True')
print('  0 - False\n')

user_input = input()

if user_input == '1':
    print('\n')
    username = input('  Enter your GitHub username: ')

    if username and len(username) > 0:
        print('\n\n  FETCHING YOUR ACCOUNT DETAILS FROM GITHUB.com...\n')
        resp = requests.get('https://api.github.com/users/%s/events' % username)
        if resp.status_code == 200:
            if len(resp.json()[0]['payload']['commits']) > 0:
                print('===================================================')
                print('   LATEST COMMIT HISTORY FOR %s' % username)
                print('====================================================')
                commit_history = input('Press 1 to continue, 0 to Quit: ')

                if commit_history == '1':
                    for j in resp.json()[0]['payload']['commits']:
                        print('[message]:%s;[url]:%s' % (j.get('message'), j.get('url')))
                elif commit_history == '0':
                    print('  QUITTING D.O.C.G WITH ERROR (002C) ==> NOT_INTERESTED_IN_LATEST_COMMIT')
                else:
                    print('  BAD INPUT: TRY AGAIN')
            else:
                print('  QUITTING D.O.C.G WITH ERROR (002D) ==> USER_HAS_NOT_COMMITTED_LATELY')
        else:
            print('  QUITTING D.O.C.G WITH HTTP ERROR %d' % resp.status_code)
    else:
        print('  QUITTING D.O.C.G WITH ERROR (002B) ==> BAD_USER_NAME')
elif user_input == '0':
    print('  QUITTING D.O.C.G WITH ERROR (001A) ==> USER_IS_NOT_REGISTERED_ON_GITHUB')
    print('  ==> ERROR DESCRIPTION: ONLY USERS WITH A GITHUB.com USER ACCOUNT CAN USE D.O.C.G: '
          'PLEASE FIRST SIGNUP AT: https://github.com/ <==')
else:
    print('BAD INPUT: TRY AGAIN')