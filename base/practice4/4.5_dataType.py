def prg2com(inlist, coms):
    outlist = []
    sumout = []
    for x in range(coms):
        outlist.append([])
        sumout.append(0)

    inlist.sort(reverse=True)

    for bread in inlist:
        lowbasket = sumout.index(min(sumout))
        outlist[lowbasket].append(bread)
        sumout[lowbasket] += bread

    return outlist

print(prg2com([3,15,6,22,13,2], 3))