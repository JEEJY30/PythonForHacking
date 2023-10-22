import base64

def decrypt_pass(password):
    decode_bytes = base64.b64decode(password)
    decode_data = decode_bytes.decode()
    print(f"decoded password {decode_data}")

encode_string = input("enter the base64 string: ")
decrypt_pass(encode_string)






