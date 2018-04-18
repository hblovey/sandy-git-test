def get_emailinfo(path):
    email_list=[]
    email_dict={}
    with open(path,'rb') as f:
        for info in f.readlines():
            email_list.append(info.decode('utf-8').strip().split('='))
            email_dict=dict(email_list)
    return email_dict
if __name__=='__main__':
    re=get_emailinfo(r'.\emailMsg.txt')
    print(re)
