
def filter_by_event():
    myfilter = Contract.eventFilter('EventName', {'fromBlock': 0,'toBlock': 'latest'});
