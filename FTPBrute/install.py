import os
choice = input('[+] to install press (Y) to uninstall press (N) >> ')
run = os.system
if str(choice) =='Y' or str(choice)=='y':

    run('chmod 777 ftpbrute.py')
    run('mkdir /usr/share/ftpbrute')
    run('cp ftpbrute.py /usr/share/ftpbrute/ftpbrute.py')

    cmnd=(' #! /bin/sh \n exec python3 /usr/share/ftpbrute/ftpbrute.py "$@"')
    with open('/usr/bin/ftpbrute','w')as file:
        file.write(cmnd)
    run('chmod +x /usr/bin/ftpbrute & chmod +x /usr/share/ftpbrute/ftpbrute.py')
    print('''\n\ncongratulation ftpbrute is installed successfully \nfrom now just type \x1b[6;30;42mftpbrute\x1b[0m in terminal ''')
if str(choice)=='N' or str(choice)=='n':
    run('rm -r /usr/share/ftpbrute ')
    run('rm /usr/bin/ftpbrute ')
    print('[!] now ftpbrute  has been removed successfully')
