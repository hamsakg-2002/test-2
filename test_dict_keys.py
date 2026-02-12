def dict_keys(d):
    return[k for k in d]
def test_dict_keys():
    assert dict_keys({'a':1,'b':2}) ==['a','b']