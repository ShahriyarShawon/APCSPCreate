from Accounts import Accounts

# TODO: make this check accounts.json for first time boot or not
def bootup():
    # with open()
    try:       
        sign_in_or_sign_up = int(input("Press 1 to Sign In or 2 to Sign up\n>"))
        if sign_in_or_sign_up == 1:
            # sign in
            pass
        elif sign_in_or_sign_up == 2:
            account.create_account()
    except Exception as e:
        print(e)


def main():
    bootup()

if __name__ == "__main__":
    account = Accounts()
    main()