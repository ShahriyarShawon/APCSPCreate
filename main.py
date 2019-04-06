from Accounts import Accounts
import json

def bootup(isFirstTime):
    with open("account.json","r") as f:
        content = json.load(f)
        isFirstTime = content["first_time"]

        if isFirstTime:
            content["first_time"] = False
            f.seek(0)
            json.dump(content, f, indent=4)
            f.truncate()
            try:       
                sign_in_or_sign_up = int(input("Press 1 to Sign In or 2 to Sign up\n>"))
                if sign_in_or_sign_up == 1:
                    # sign in
                    print("Sign in")
                    pass
                elif sign_in_or_sign_up == 2:
                    account.create_account()
            except Exception as e:
                print(e)
        else:
            # sign in
            print("Sign in")
            pass


def main():
    with open("account.json", "r+") as f:
        content = json.load(f)        
        bootup(content["first_time"])

if __name__ == "__main__":
    account = Accounts()
    main()