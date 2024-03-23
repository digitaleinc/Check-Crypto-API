from datetime import datetime
from functions import logger
from config import bot

import requests
import json


def process_usdt_trc20(message):
    logger(message)
    trans = message.text
    req = requests.get(f"https://apilist.tronscanapi.com/api/transaction-info?hash={trans}")
    transaction_info = json.loads(req.content)
    if not len(transaction_info) == 1:
        try:
            # Extracting data
            contract_ret = transaction_info['contractRet']
            confirmed = transaction_info['confirmed']
            risk_transaction = transaction_info['riskTransaction']
            transaction_date = int(transaction_info['timestamp'])/1000
            transfer_info = transaction_info['transfersAllList'][0]
            from_address = transfer_info['from_address']
            to_address = transfer_info['to_address']
            decimals = transfer_info['decimals']
            amount_str = transfer_info['amount_str']
            status_sender = transaction_info['normalAddressInfo'][from_address]['risk']
            status_reciever = transaction_info['normalAddressInfo'][to_address]['risk']

            # Check if transaction is confirmed
            if confirmed:
                confirmed = "Yes"
            else:
                confirmed = "No"

            # Check if transaction is risk
            if risk_transaction:
                risk_transaction = "Yes"
            else:
                risk_transaction = "No"

            # Check if sender's wallet is marked dirty or clear
            if status_sender:
                status_sender = "dirty"
            else:
                status_sender = "clear"

            # Check if reciever's wallet is marked dirty or clear
            if status_reciever:
                status_reciever = "dirty"
            else:
                status_reciever = "clear"

            converted_date = datetime.fromtimestamp(transaction_date)

            amount = int(amount_str) / (10 ** decimals)

            bot.send_message(message.chat.id, f"Transaction Status: {contract_ret}\n"
                                              f"Is confirmed: {confirmed}\n"
                                              f"Token: USDT TRC20\n"
                                              f"Transaction date: {converted_date}\n"
                                              f"Amount: {amount}$\n"
                                              f"\n"
                                              f"From: {from_address}\n"
                                              f"To: {to_address}\n"
                                              f"\n"
                                              f"Is transaction on risk: {risk_transaction}\n"
                                              f"\n"
                                              f"Wallet statuses (risk):\n"
                                              f"Sender: {status_sender}\n"
                                              f"Receiver: {status_reciever}\n"
                                              f"\n"
                                              f"By CryptoCheck Bot", reply_to_message_id=message.message_id)
        except KeyError:
            bot.send_message(message.chat.id, "No info/wrong input",
                             reply_to_message_id=message.message_id)
    else:
        bot.send_message(message.chat.id, "No info/wrong input", reply_to_message_id=message.message_id)


# def process_tron(message):
#     logger(message)
#     transaction = message.text
#     req = requests.get(f"https://apilist.tronscanapi.com/api/transaction-info?hash={transaction}")
#     transaction_info = json.loads(req.content)
#     print(transaction_info)
#
#
# def process_btc(message):
#     logger(message)
#     transaction = message.text
#     req = requests.get(f"https://blockchain.info/rawtx/{transaction}")
#     transaction_info = json.loads(req.content)
#     print(transaction_info)
