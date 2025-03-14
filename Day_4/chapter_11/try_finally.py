def main():
    try:
        a = int(input("enter a number: "))
        print(a)
        return

    except Exception as e:
        print(e)
        return

    finally: # isks use function mein ata hai
        print("i am finally k andar nikalo mujhe")

main()