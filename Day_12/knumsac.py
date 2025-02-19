def knumsac(list, wight):
    list.sort(key=lambda x: x[0]/x[1], reverse=True) # x[0]/x[1] means cost ber unit
    total_wight = 0
    total_cost = 0
    for cost, unit_w in list:
        if wight >= unit_w:
            total_cost += cost
            wight -= unit_w
        else:
            total_cost += wight * (cost / unit_w)
            break
    return total_cost

list = [[60,10],[100,20],[120,30]]
wight = 50
print(knumsac(list,wight))
