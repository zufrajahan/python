try:
    a = int(input("enter a number: "))
    print(a)

# except ValueError as v:
#     print("value dekho andhe")
#     print(v)

except Exception as e:
    print(e)

else:
    print("I am inside else")

    # try thek ho to tab else mein chala jata hai