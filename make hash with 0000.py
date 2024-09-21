import hashlib

hundred_T=100000000000000

def find_hash(block_num,prev_hash,transaction):
    for i in range(hundred_T):
        to_str=str(block_num)+str(prev_hash)+str(transaction)+str(i)
        hash_result=hashlib.sha256(to_str.encode()).hexdigest()
        print(hash_result)
        if hash_result.startswith("0000"):
            print(i)
            break


find_hash(1,0,2)