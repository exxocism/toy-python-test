def queuePrinter( buffersize, capacities, documents ):
    queue = [ None ] * buffersize
    def queueSum():
        nonlocal queue
        sum = 0
        for i in range(0, len(queue)):
            if queue[i]:
                sum += queue[i]
        return sum
    
    def queueHasValue():
        nonlocal queue
        for i in range(0, len(queue)):
            if queue[i]:
                return True
        return False

    def queueLength():
        nonlocal queue
        sum = 0
        for i in range(0, len(queue)):
            if queue[i]:
                sum += 1
        return sum

    second = 0
    while len(documents):
        queue.pop(0)
        if ( queueLength() < buffersize
             and len(documents)
             and queueSum() + documents[0] <= capacities
           ):
            queue.append( documents.pop(0) )
        else: 
            queue.append( None )
        second += 1
    while queueHasValue():
        queue.pop(0)
        second += 1

    return second

# bufferSize = 2
# capacities = 10
# documents = [7, 4, 5, 6]
# output = queuePrinter(bufferSize, capacities, documents)
# print(output)
# # 8
