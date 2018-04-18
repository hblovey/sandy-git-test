import csv

def get_pageinfo(path):
    page_list=[]
    page_dict={}
    data=csv.reader(open(path,'r'))
    for info in data:
        page_list.append(info)
        page_dict=dict(page_list)
    return page_dict
if __name__=='__main__':
    re=get_pageinfo(r'.\PageMsg.csv')
    for i in re:
        print(i,re[i])


