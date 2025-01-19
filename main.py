import base58
from solders.keypair import Keypair 


def generate_wallets(wallets_amount: int) -> None:
    try:
        with open("wallets.txt", 'w') as f:
            for i in range(wallets_amount):
                account = Keypair()
                pk = base58.b58encode(account.secret() + base58.b58decode(str(account.pubkey()))).decode('utf-8')
                f.write(pk + '\n')
            print("Кошельки были сгенерированы успешно!\nНе забудьте их сохранить куда - нибудь и сделать резервную копию!")
    except Exception as e:
        print("Произошла ошибка при генерации. Попробуйте перезапустить программу или обратиться к разработчику " \
            f"Код ошибки: {e}")


def main():
    while True:
        try:
            wallets_amount = int(input("Введите кол - во кошельков для генерации: "))
            generate_wallets(wallets_amount)
            break
        except:
            print("Неверный ввод. Попробуйте ещё раз.")


if __name__ == "__main__":
    main()