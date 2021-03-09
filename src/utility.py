import hashlib

blake2b = hashlib.blake2b()
blake2s = hashlib.blake2s()
md5 = hashlib.md5()
sha1 = hashlib.sha1()
sha224 = hashlib.sha224()
sha256 = hashlib.sha256()
sha384 = hashlib.sha384()
sha3224 = hashlib.sha3_224()
sha3256 = hashlib.sha3_256()
sha3384 = hashlib.sha3_384()
sha3512 = hashlib.sha3_512()
sha512 = hashlib.sha512()
shake128 = hashlib.shake_128()
shake256 = hashlib.shake_256()

hash_list = [blake2b,blake2s,md5,sha1,sha224,sha256,sha384,sha3224,sha3256,sha3384,sha3512,sha512,shake128,shake256]

def hashWithAllMethods(text):
    for hash_object in hash_list:
        hash_object.update(text)
        print('{}: {}'.format(hash_object.name, hash_object.hexdigest())) 
    
    