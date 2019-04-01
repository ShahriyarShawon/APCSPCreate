class Encryptor:
    def __init__(self):
        # self.offset_value = offset_value
        pass

    def encrypt(self, raw_password):
        enc_pass = ""
        for letter in raw_password:
            enc_pass += hex(ord(letter)).replace("0x","").replace("6","!X:2").replace("5","&^~").replace("4","[]_{+-")
        print(enc_pass)
        return enc_pass

    def decrypt(self, enc_password):
        enc_password =  enc_password.replace("!X:2","6").replace("&^~","5").replace("[]_{+-","4")
        raw_pass = bytearray.fromhex(enc_password).decode('utf-8')
        print(raw_pass)
        return raw_pass
        
encryptor = Encryptor()
encryptor.decrypt(encryptor.encrypt("P@$$word1"))