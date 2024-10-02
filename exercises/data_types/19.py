def concat(*dicts):
    result = {}
    for dicto in dicts:
        result.update(dicto)
    return result

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}

print(concat(dic1, dic2, dic3))
