import json
from PassMger import PassMger


def bootup(account):
    with open("account.json","r+") as f:
        content = json.load(f)
        isFirstTime = content["first_time"]

        if isFirstTime:
            content["first_time"] = False
            f.seek(0)
            json.dump(content, f, indent=4)
            f.truncate()
            try:       
                sign_in_or_sign_up = int(raw_input("Press 1 to Sign In or 2 to Sign up\n>"))
                if sign_in_or_sign_up == 1:
                    passMger.sign_in()
                    # print("Sign in")                    
                elif sign_in_or_sign_up == 2:
                    passMger.create_account()
            except Exception as e:
                print(e)
        else:
            passMger.sign_in()

def main(account):
    bootup(account)

if __name__ == "__main__":
    passMger = PassMger()
    # account = Accounts()
    main(passMger)