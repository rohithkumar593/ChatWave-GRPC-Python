import asyncio, threading
from src.config import config


def get_inputs():
    data = input("please enter your message update here :  ")
    receivers_id = input(
        f"receivers id: available clients are {config.clients}\n Please enter any id from above"
    )
    return data, receivers_id


def get_receivers_id():
    return input("receivers id")


def run_two_functions(
    func_a, funca_args, funca_kwargs, func_b, funcb_args, funcb_kwargs
):
    t2 = threading.Thread(target=func_a, args=funca_args)
    t1 = threading.Thread(target=func_b, args=funcb_args)

    t1.start()
    t2.start()

    t1.join()
    t2.join()
