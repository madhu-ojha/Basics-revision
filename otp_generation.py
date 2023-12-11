import random
import math


def generate_otp(otplen):

    stringg = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    OTP = ""
    length = len(stringg)
    # otp_len = len(otplen)

    for i in range(otplen):
        OTP += stringg[math.floor(random.random() * length)]
    return OTP


if __name__ == "__main__":
    otplen = int(input("Enter length of OTP you need: "))
    print(f"OTP of length {otplen}:", generate_otp(otplen))
