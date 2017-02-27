import random
import copy

def reservoirSampling(seq, k):
    # localSeq = copy.deepcopy(seq)
    localSeq = seq
    N = len(localSeq)
    for i in xrange(k, N):
        M = int(random.uniform(0, i))
        if M < k:
            temp = copy.deepcopy(localSeq[M])
            localSeq[M] = copy.deepcopy(localSeq[i])
            localSeq[i] = temp
    return localSeq[0:k]


def main():
    a = [4, 5, 6, 3, 4, 7, 7, 4, 3, 3, 2, 4, 5, 5, 6, 9, 5, 4, 3, 45, 3, 23, 44, 55, 33, 5, 8]
    k = 5
    print reservoirSampling(a, k)


if __name__ == '__main__':
    main()