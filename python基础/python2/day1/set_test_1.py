try:
    n = int(input("please enter your number:"))
    result = 10/n
except IOError:
    print("io error")
except EOFError:
    print("user press ctrl D")
except KeyboardInterrupt:
    print("user cancelled")
except ZeroDivisionError:
    print("0 cant be division")
except TypeError:
    print("please input right words")
except NameError:
    print("please enter right words")
except ValueError:
    print("this is not a number")
else:
    print(result)
finally:
    print("thanks for yout using!")