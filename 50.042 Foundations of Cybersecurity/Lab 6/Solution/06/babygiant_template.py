#50.042 FCS Lab 6 template
#Year 2019
# See Wan Yi Faith (1002851)

import math
import primes_template as primes

def calc_m(p):
    m = int(math.floor(math.sqrt(p)))
    return m

def baby_step(alpha,beta,p,fname):
    m = calc_m(p)

    with open("baby_step.txt", "w") as bsout:
        for xb in range(0, m):
            # bsout.write(str((primes.square_multiply(alpha, xb, p) * beta) % p) + '\n')
            bsout.write(str((alpha**xb*beta) % p) + '\n')
        bsout.close()

def giant_step(alpha,p,fname):
    m = calc_m(p)

    with open("giant_step.txt", "w") as gsout:
        for xg in range(0, m):
            gsout.write(str(primes.square_multiply(alpha, m*xg, p)) + '\n')
        gsout.close()

def baby_giant(alpha,beta,p):
    m = calc_m(p)

    # call both methods
    baby_step(alpha,beta,p,'baby_step.txt')
    giant_step(alpha,p,'giant_step.txt')

    with open("baby_step.txt", "r") as bs:
        baby_step_list = [line.strip() for line in bs]
        bs.close()

    with open("giant_step.txt", "r") as gs:
        giant_step_list = [line.strip() for line in gs]
        gs.close()

    # compare both lists to find any that match
    match = list(set(baby_step_list).intersection(set(giant_step_list)))
    for i in match:
        xb_match = baby_step_list.index(match[0])
        xg_match = giant_step_list.index(match[0])*(m)
        new_x = xg_match - xb_match
        return new_x

if __name__=="__main__":
    """
    test 1
    My private key is:  264
    Test other private key is:  7265

    """
    p=17851
    alpha=17511
    A=2945
    B=11844
    sharedkey=1671
    a=baby_giant(alpha,A,p)
    b=baby_giant(alpha,B,p)
    guesskey1=primes.square_multiply(A,b,p)
    guesskey2=primes.square_multiply(B,a,p)
    print ('Guess key 1:',guesskey1)
    print ('Guess key 2:',guesskey2)
    print ('Actual shared key :',sharedkey)
