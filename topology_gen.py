#!/usr/bin/python

def get_full_uid(str):
    str.rstrip()
    return str

def get_id_from_str(str):
    str.rstrip()    #remove whitespace!
    i = len(str) -1
    while i>=0 :
        if not str[i].isdigit() : break
        i-=1

    substr = str[(i+1):]

    return int(substr)



def gen_id_loc(filename,asn):
    cch_file = open(filename,'r')
    uid_file = open(asn+"_loc.txt",'w')

    for line in cch_file:
        items = line.split()
        uid = items[0]
        loc = items[1]
        if uid.isdigit() and loc.startswith('@') :
            uid_file.write(uid + ' ' + loc + '\n')

    uid_file.close()
    cch_file.close()


def gen_backbone_uids(filename,asn):
    uids = []
    w_file = open(filename,'r')
    for line in w_file:
        x = line.split()
        fr = x[0]
        to = x[1]
        metric = x[2]
        
        #uid = get_id_from_str(fr)
        uid = get_full_uid(fr)
        uids.append(uid)
        #print('%d ' % (uid) ,end=' ')
        #uid = get_id_from_str(to)
        uid = get_full_uid(fr)
        uids.append(uid)
        #print('%d %s' % (uid, metric))

    w_file.close()
    x = list(set(uids))
    x.sort()
    print_uids(x)

def print_uids(uids):

    for uid in uids :
        print(uid)

    count = len(uids)
    print('Count = %d ' % (count) )


print ("=========Rockfuel Topology===========")

while True :
    asn = input("Please enter asn (0 to finish): \n")
    
    if int(asn) > 0 :
        #gen_id_loc('cch/'+asn+'.r0.cch', asn)
        uids = gen_backbone_uids('weight/'+asn+'/weights.intra',asn)
    else : break


