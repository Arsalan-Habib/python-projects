def replacer(char,word,index_list):
    for i in index_list:

        new_word=word[:i*2]+char+word[(i*2)+1:]
        word=new_word
    return word
    


z=[1,5,8]
print(replacer('a','_,_,_,_,_,_,_,_,_,_,_,_',z))