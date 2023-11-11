import inspect
import cryo

# function_to_inspect = cryo.collect()
# signature = inspect.signature(function_to_inspect)
# print(signature)

print("Working")
# txs = cryo.collect('transactions', blocks=['13891880:13893600'],rpc='https://eth.llamarpc.com' , requests_per_second=50,output_dir='./data')
txs = cryo.freeze('transactions', blocks=['13891880:13893600'],rpc='https://eth.llamarpc.com' , requests_per_second=50,output_dir='./data')
print("Done")