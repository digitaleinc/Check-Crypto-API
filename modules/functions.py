import json


def logger(message):
    log_id = message.from_user.id
    log_name = message.from_user.first_name
    log_surname = message.from_user.last_name
    log_username = message.from_user.username
    if log_surname is None:
        if log_username is None:
            print(f"{log_name} ({log_id}): {message.text}")
        else:
            print(f"{log_name} ({log_id}) [@{log_username}]: {message.text}")
    else:
        if log_username is None:
            print(f"{log_name} {log_surname} ({log_id}): {message.text}")
        else:
            print(f"{log_name} {log_surname} ({log_id}) [@{log_username}]: {message.text}")


def extract_arg(arg):
    return arg.split()[1:]


def transaction_validation(transaction_info):
    try:
        if "riskTransaction" in transaction_info and transaction_info["riskTransaction"] is False:
            return True
        else:
            return False
    except json.JSONDecodeError:
        return False
