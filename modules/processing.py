from datetime import datetime
from modules.functions import logger
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
            transaction_date = int(transaction_info['timestamp']) / 1000
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
                status_conf = "✅"
            else:
                confirmed = "No"
                status_conf = "⭕️"

            # Check if transaction is risk
            if risk_transaction:
                risk_transaction = "Yes"
                status_risk = "❗️"
            else:
                risk_transaction = "No"
                status_risk = "✔️"

            # Check if sender's wallet is marked dirty or clear
            if status_sender:
                status_sender = "dirty"
                status_s = "🔴"
            else:
                status_sender = "clear"
                status_s = "🟢"

            # Check if reciever's wallet is marked dirty or clear
            if status_reciever:
                status_reciever = "dirty"
                status_r = "🔴"
            else:
                status_reciever = "clear"
                status_r = "🟢"

            converted_date = datetime.fromtimestamp(transaction_date)

            amount = int(amount_str) / (10 ** decimals)

            bot.send_message(message.chat.id, f"🔗 <b>Transaction Status:</b> {contract_ret}\n"
                                              f"{status_conf} <b>Is confirmed:</b> {confirmed}\n"
                                              f"🔧 <b>Token:</b> USDT TRC20\n"
                                              f"📆 <b>Transaction date:</b> {converted_date}\n"
                                              f"💰 <b>Amount:</b> {amount}$\n"
                                              f"\n"
                                              f"➡️ <b>From:</b> {from_address}\n"
                                              f"⬅️ <b>To:</b> {to_address}\n"
                                              f"\n"
                                              f"{status_risk} <b>Is transaction on risk:</b> {risk_transaction}\n"
                                              f"\n"
                                              f"🔍 <b>Wallet statuses (risk):</b>\n"
                                              f"{status_s} <b>Sender:</b> {status_sender}\n"
                                              f"{status_r} <b>Receiver:</b> {status_reciever}\n"
                                              f"<i>Bot was created by A.K.</i>\n"
                                              f"<b>GitHub ► https://github.com/digitaleinc</b>",
                             parse_mode='HTML',
                             reply_to_message_id=message.message_id)
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
