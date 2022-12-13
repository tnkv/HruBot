import asyncio


async def mainHru(message: str) -> str:
    counter = 0
    hru_msg = ""
    for i in range(len(message)):
        if isLetter(message[i]):
            if counter ==  0:
                hru_msg += "х" if not message[i].isupper() else "Х"
            elif counter == 1:
                hru_msg += "р" if not message[i].isupper() else "Р"
            else:
                hru_msg += "ю" if not message[i].isupper() else "Ю"
            counter += 1
        else:
            hru_msg += message[i]
            counter = 0
    if len(message) != 0: return "> " + hru_msg
    return "🔪🐖"


def isLetter(letter: str) -> bool:
    if "а" <= letter <= "я" or "А" <= letter <= "Я" or "a" <= letter <= "z" or "A" <= letter <= "Z" or letter in (
            "Ё", "ё"):
        return True
    else:
        return False


if __name__ == "__main__":
    print(asyncio.run(mainHru(input())))
