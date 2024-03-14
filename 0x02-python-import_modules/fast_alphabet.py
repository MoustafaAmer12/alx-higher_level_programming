#!/usr/bin/python3
def get_alphabet():
    alpha  = ""
    for i in range(ord('A'), ord('Z') + 1):
        alpha += chr(i)
    return alpha

if __name__ == "__main__":
    alpha = get_alphabet()
    print(alpha)
