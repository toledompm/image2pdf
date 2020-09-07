def dictListFilter(dictList,key,expectedValues):
    newDictList = list()
    for dict in dictList:
        if dict[key] in expectedValues:
            newDictList.append(dict)
    return newDictList