import hashlib
import timeit
import plotly.express as px

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
        if(hash_object == shake128 or hash_object == shake256):
            print('{}: {}'.format(hash_object.name, hash_object.hexdigest(20))) 
        else:
            print('{}: {}'.format(hash_object.name, hash_object.hexdigest())) 

def measure_time_of_hashing_with_all(text):
    return timeit.timeit(lambda: hashWithAllMethods(text), number=1000)

def measure_time_of_hasing_with_single_hashing(text): 
    measureTimes = {}
    for hash_object in hash_list:
        measureTimes[hash_object.name] = timeit.timeit(lambda: hash_object.update(text))
    return measureTimes

def fileHashing(path: str, hashingName: str) -> str:
    for hashFunction in hash_list:
        if hashFunction.name == hashingName:
            with open(path, 'rb') as file: 
                while True:
                    chunk = file.read(hashFunction.block_size)
                    if not chunk:
                        break
                    hashFunction.update(chunk)
    return hashFunction.hexdigest(20) if "shake_" in hashFunction.name else hashFunction.hexdigest()

def plot_times_of_hashes(text):
    fig = px.bar(measure_time_of_hasing_with_single_hashing(text), x='times', y='y_vals')
    fig.show()