# Brownie Intro

## Install Packages

```
yay -S solidity

python3 -m pip install --user pipx

pipx install eth-brownie

npm i -g ganache-cli

pip install brownie
```

## Create Brownie Project

```
mkdir brownie-intro

cd brownie-intro

brownie init
```

## Commands

- See all commands

```
brownie --help
```

- Compile Contract to JSON

```
brownie compile
```

- Run the contract with brownie

```
brownie run deploy
```

- Start ganache before running brownie

```
ganache-cli --port 8545 --gasLimit 12000000 --accounts 10 --hardfork istanbul --mnemonic brownie
```

## Networks

```
brownie network list
```

```
brownie network add
```

Example:

All EVM compatible chains have a chainid

```
brownie network add Ethereum avalanche host=?? ?? chainid=??
```

## Environment Variables

```
touch .env
```

Add the following:

```
WEB3_INFURA_PROJECT_ID = XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
PRIVATE_KEY = 0xXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
ETHERSCAN_TOKEN = XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

## Deploy to testnet

```
brownie run scripts/deploy.py --network kovan
```
