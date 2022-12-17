import json

FILENAME_CONTRACTS = 'contracts/contracts.json'


def run():
    with open(FILENAME_CONTRACTS) as f:
        data = json.load(f)
        print(data)


if __name__ == '__main__':
    run()
