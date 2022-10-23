# шифр цезаря
def caesar_cipher(n, message):
    message = list(message)
    alphabet_lower = [chr(ord("а") + i) for i in range(32)]
    alphabet_upper = [chr(ord("А") + i) for i in range(32)]

    changed_lower_alphabet = [chr(ord("а") + i) for i in range(32)]
    changed_upper_alphabet = [chr(ord("А") + i) for i in range(32)]

    for i in range(n):
        letter = changed_lower_alphabet.pop(0)
        changed_lower_alphabet.append(letter)

    for i in range(n):
        letter = changed_upper_alphabet.pop(0)
        changed_upper_alphabet.append(letter)

    new_message = []
    for i in range(len(message)):
        for j in range(len(alphabet_lower)):
            if message[i] == alphabet_lower[j]:
                new_message.append(changed_lower_alphabet[j])

        for g in range(len(alphabet_upper)):
            if message[i] == alphabet_upper[g]:
                new_message.append(changed_upper_alphabet[g])

    answer = "".join(new_message)
    print(answer)


# caesar_cipher(int(input(" Введите шаг шифрования: ")), input("Введите сообщение, которое хотите зашифровать: "))


# RSA шифрование
l = list("abcdefghijklmnopqrstuvwxyz")
# словарь буква - индекс
dictOfIndezes = {l[x]: x for x in range(len(l))}
# словарь индекс - буква
tempDict = {x: l[x] for x in range(len(l))}
# словарь буква - зашифрованная буква
dictToCode = {}
for k, v in dictOfIndezes.items():
    dictToCode[k] = tempDict[(v*7)%26]
dictToCode[" "] = " "


def rsaIn(message):
    message = list(message)
    print(message)
    newMessage = []

    for i in message:
        for letter, newLetter in dictToCode.items():
            if i == letter:
                newMessage.append(newLetter)

    codedMessage = "".join(newMessage)
    print(codedMessage)


def rsaOut(message):
    message = list(message)
    newMessage = []

    for i in message:
        for letter, newLetter in dictToCode.items():
            if i == newLetter:
                newMessage.append(letter)

    codedMessage = "".join(newMessage)
    print(codedMessage)


rsaIn("hello hello")
rsaOut("xczzu")














































