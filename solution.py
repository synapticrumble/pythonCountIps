def count_ips(filename):
    import re
    #Define the search term:
    # Simple matching: \d+ means match one of more digits
    pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')

    #Create an empty list, and empty dict:
    data = []
    myDict = {}

    for line in open(filename, 'r'):
        if line !='':  #<-- To make sure the whole file is read
            word = re.findall(pattern, line)
            data.append(str(word)) 


    for i in range(len(data)):
        myDict[data[i]] = data.count(data[i])
    
    return myDict