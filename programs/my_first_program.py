from nada_dsl import *


def nada_main():
    party1 = Party(name="Party1")
    my_int1 = SecretInteger(Input(name="my_int1", party=party1))
    my_int2 = SecretInteger(Input(name="my_int2", party=party1))
    
    r=my_int1*my_int2
    r3=my_int1/my_int2
    r4=(my_int1+my_int2)*(my_int1-my_int2)
    # write the computation for your program here - use my_int1 and my_int2 as inputs
    # make sure you change the output below to be your new output
    int1=my_int1+Integer(1)
    int2=my_int2+Integer(1)
    def max(a: SecretInteger, b: SecretInteger) -> SecretInteger:
        return (a < b).if_else(b, a)
    r6=(my_int1+my_int2)*((my_int1*my_int1)-(my_int1*my_int2)+(my_int2*my_int2))
    r1 = max(my_int1, my_int2)
    r5=Integer(0)
    out1=Output(r1,"Maximum of two Numbers",party1)
    out2=Output(r,"Multiplication of Two Numbers",party1)
    out3=Output(r3,"Division of Two Numbers",party1)
    out5=Output(r5,"Welcome to Hacker House GOA 2024",party1)
    out4=Output(r4,"(a^2-b^2)=(a+b)(a-b) = ",party1)
    out4=Output(r6,"(a^3+b^3)=(a+b)(a^2-ab-b^2) = ",party1)
    return [out1,out2,out3,out4,out5]