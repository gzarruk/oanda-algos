import pandas as pd
import tpqoa
import json
import sys
from datetime import datetime

api = tpqoa.tpqoa("oanda.cfg")


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    account_info = json.dumps(api.get_account_summary(), sort_keys=False, indent=4)
    print(account_info)
    # pairs = api.get_instruments()
    # print(api.account_type)
    # print(pairs, "\n")

    gold = api.get_history(
        instrument="XAU_USD",
        start="2020-07-01",
        end=datetime.now().strftime("%Y/%m/%d"),
        granularity="D",
        price="B",
    )
    print(gold.head())
    print(gold.tail())


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
