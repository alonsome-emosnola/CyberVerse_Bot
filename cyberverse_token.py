import os
# import asyncio
from bscscan import BscScan
# from bscscan.modules.tokens import Tokens
from dotenv import load_dotenv

load_dotenv()

apiKey = os.environ["BSCSCAN_API_KEY"]
contract_addr = os.environ["CONTRACT_ADDRESS"]
addr = os.environ["ADDRESS"]

async def get_total_token_supply_amount():
  async with BscScan(apiKey) as bsc:
    try:
      result = await bsc.get_total_supply_by_contract_address(contract_address=contract_addr)
    except:
      raise Exception("Error getting CBV total token supply")
    else:
      return result

async def get_total_token_circulating_amount():
  async with BscScan(apiKey) as bsc:
    try:
      result = await bsc.get_circulating_supply_by_contract_address(contract_address=contract_addr)
    except:
      raise Exception("Error getting CBV total circulating amount")
    else:
      return result

async def get_balance(address):
  async with BscScan(apiKey) as bsc:
    try:
      result = await bsc.get_acc_balance_by_token_contract_address(contract_address=contract_addr, address=address)
    except:
      raise Exception("Error getting your CBV balance, please ensure your wallet address is correct")
    else:
      return result


async def get_transfer_history(add_ress):
  async with BscScan(apiKey) as bsc:
    try:
      result = await bsc.get_bep20_token_transfer_events_by_address(address=add_ress, startblock=0, endblock=999999999, sort="asc")
    except:
      raise Exception("Error getting transaction history")
    else:
      return result

async def get_internal_txs_history(add_ress):
  async with BscScan(apiKey) as bsc:
    try:
      result = await bsc.get_internal_txs_by_address(address=add_ress, startblock=0, endblock=2702578, sort="asc")
    except:
      raise Exception("Error getting internal transaction history")
    else:
      return result

def normalize(decimal: str) -> float:
  beginning = decimal[:13]
  ending = decimal[13:]
  result = f"{beginning}.{ending}"
  return float(result)

func = {
  "bal": get_balance,
  "total_supply": get_total_token_supply_amount,
  "total_circulating": get_total_token_circulating_amount,
  "transfer_history": get_transfer_history,
  "internal_txs": get_internal_txs_history,
  "normalize": normalize
}
