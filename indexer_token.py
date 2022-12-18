import json
import logging
import sys
import time

from web3 import Web3, middleware

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)8s %(asctime)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

FILENAME_CONTRACTS = 'contracts/contracts.json'
FILENAME_ABI_TOKEN_SALE = 'contracts/artifacts/contracts/TokenSale.sol/TokenSale.json'
STEP = 100
START_BLOCK = 0
TIME_SLEEP = 1


def read_file(filename):
    with open(filename) as f:
        return json.load(f)


if __name__ == '__main__':
    logging.info(f'start indexer {sys.argv[0]}')

    w3 = Web3(Web3.HTTPProvider(
        'http://localhost:8545',
        request_kwargs={'timeout': 120}
    ))
    w3.middleware_onion.inject(middleware.geth_poa_middleware, layer=0)

    token_contract = w3.eth.contract(
        abi=read_file(FILENAME_ABI_TOKEN_SALE)['abi'],
        address=Web3.toChecksumAddress(read_file(FILENAME_CONTRACTS)['token_sale'])
    )

    from_block = START_BLOCK
    to_block = START_BLOCK + STEP

    while True:
        logging.info(f'sleep {TIME_SLEEP} ...')
        time.sleep(TIME_SLEEP)

        last_block = w3.eth.get_block('latest')['number']
        if to_block > last_block:
            continue

        events = token_contract.events.Bought.createFilter(
            fromBlock=from_block,
            toBlock=to_block
        ).get_all_entries()

        logging.info(f'number of events : {len(events)}')

        for event in events:
            print(event)
