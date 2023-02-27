
from mypymongo import brevet_insert, brevet_find
import nose
import arrow

import logging
logging.basicConfig(format='%(levelname)s:%(message)s',
                    level=logging.WARNING)
log = logging.getLogger(__name__)

# reuse some code from test_acp_times
def test_brevet_insert():
    # Yes??
    brevet = 200
    start = '2023-02-17 00:00'
    checkpoints = [
        {"km": 0, "miles": 0.0, "open": start, "close": '2023-02-17 01:00', "location": 'Optional'},
        {"km": 50, "miles": 31.0686, "open": '2023-02-17 01:28', "close": '2023-02-17 03:30', "location": 'Optional2'},
        {"km": 100, "miles": 62.1371, "open": '2023-02-17 02:56', "close": '2023-02-17 06:40', "location": 'Optional3'},
        {"km": 150, "miles": 93.2057, "open": '2023-02-17 04:25', "close": '2023-02-17 10:00', "location": 'Optional3'},
        {"km": 200, "miles": 124.274, "open": '2023-02-17 05:53', "close": '2023-02-17 13:30', "location": 'Optional4'}
    ]

    table_id = brevet_insert(brevet, start, checkpoints)
    assert(table_id != -1 and table_id != None)

def test_brevet_find():
    ## YES!
    brevet = 200
    start = '2023-02-17 00:00'
    checkpoints = [
        {"km": 0, "miles": 0.0, "open": start, "close": '2023-02-17 01:00', "location": 'Optional'},
        {"km": 50, "miles": 31.0686, "open": '2023-02-17 01:28', "close": '2023-02-17 03:30', "location": 'Optional2'},
        {"km": 100, "miles": 62.1371, "open": '2023-02-17 02:56', "close": '2023-02-17 06:40', "location": 'Optional3'},
        {"km": 150, "miles": 93.2057, "open": '2023-02-17 04:25', "close": '2023-02-17 10:00', "location": 'Optional3'},
        {"km": 200, "miles": 124.274, "open": '2023-02-17 05:53', "close": '2023-02-17 13:30', "location": 'Optional4'}
    ]

    table_id = brevet_insert(brevet, start, checkpoints)

    table = brevet_find()
    assert (table == (brevet, start, checkpoints))
