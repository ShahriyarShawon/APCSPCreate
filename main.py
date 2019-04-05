from Accounts import Accounts
import json

# TODO: make this check accounts.json for first time boot or not
def bootup(isFirstTime):
    # with open()
    if isFirstTime:
        try:       
            sign_in_or_sign_up = int(input("Press 1 to Sign In or 2 to Sign up\n>"))
            if sign_in_or_sign_up == 1:
                # sign in
                pass
            elif sign_in_or_sign_up == 2:
                account.create_account()
        except Exception as e:
            print(e)
    else:
        # sign in
        pass


def main():
    with open("account.json", "r+") as f:
        content = json.load(f)        
        bootup(content["first_time"])

if __name__ == "__main__":
    account = Accounts()
    main()