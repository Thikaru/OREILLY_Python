print("test" + "get" + "func")

print("Ha" * 5)

print("test"[0] + "test"[1] + "test"[-2] + "test"[-1])
char = "test"
# char[0] = "K"　これはできない
letters = "abcdefghijklmnopqrstuvwxyz"
print(letters[:])
print(letters[1:2])
print(letters[3:])
print(letters[:-2])
print(letters[::7])
print(letters[4:20:3])
print(letters[::-1])
print(letters[-1::-1])
print(len(letters));
print(len(letters[::7]))

split_str = "test,google,god,killer"
print(split_str.split(','))

list = ["abc","efd","hjk","bnm","iop"]
print(",".join(list))