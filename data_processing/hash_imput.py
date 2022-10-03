import hashlib
def hash_in(thing_to_hash):
    h = hashlib.new('SHA512')
    h.update(bytes(thing_to_hash, encoding='utf-8'))
    print(h.hexdigest())
    # return h.hexdigest()