from enum import Enum
from hashlib import md5, sha1, sha256, sha512

class HashType(Enum):
    MD5 = 'md5'
    SHA1 = 'sha1'
    SHA256 = 'sha256'
    SHA512 = 'sha512'

def get_hash(text:str, hash_type:HashType):
    if hash_type == HashType.MD5:
        return md5(text.encode('utf-8')).hexdigest()
    elif hash_type == HashType.SHA1:
        return sha1(text.encode('utf-8')).hexdigest()
    elif hash_type == HashType.SHA256:
        return sha256(text.encode('utf-8')).hexdigest()
    elif hash_type == HashType.SHA512:
        return sha512(text.encode('utf-8')).hexdigest()
