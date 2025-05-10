from math import *

def bitSeq2PlainBlocks(bitSeq,plainBlockSize):
    bitSeq = bitSeq + "1"
    if len(bitSeq)%plainBlockSize != 0:
        bitSeq = bitSeq + "0" * (plainBlockSize - len(bitSeq)%plainBlockSize)
    plainBlocks = []
    noOfblocks = int(len(bitSeq)/plainBlockSize)
    for i in range(0,noOfblocks):
        plainBlocks.append(bitSeq[i*plainBlockSize:(i+1)*plainBlockSize])
    return plainBlocks

def removePadding(bitSeq):
    indexOfOne = len(bitSeq)-1
    while bitSeq[indexOfOne]=="0":
        indexOfOne = indexOfOne -1
    return bitSeq[0:indexOfOne]

def blocks2numberSeq(blocks):
    numSeq = []
    for b in blocks:
        numSeq.append(int(b,2))
    return numSeq

def numberSeq2Blocks(numSeq, bsize):
    blocks = []
    for num in numSeq:
        block = bin(num)
        block = block[2:]
        if len(block)<bsize:
            block = "0"*(bsize-len(block)) + block
        blocks.append(block)
    return blocks

def rsaEncrypt(key, plainBitSeq):
    (e,n) = key
    plainBlockSize = floor(log(n,2))
    cipherBlockSize =  plainBlockSize + 1
    plainBlocks = bitSeq2PlainBlocks(plainBitSeq,plainBlockSize)
    plainNumSeq = blocks2numberSeq(plainBlocks)

    cipherNumSeq = []
    for plainNum in plainNumSeq:
        cipherNum = plainNum**e % n
        cipherNumSeq.append(cipherNum)
    cipherBlocks = numberSeq2Blocks(cipherNumSeq,cipherBlockSize)
    cipherBitSeq = ""
    for b in cipherBlocks:
        cipherBitSeq = cipherBitSeq + b
    return cipherBitSeq

def rsaDecrypt(key, cipherBitSeq):
    (d,n) = key
    plainBlockSize = floor(log(n,2))
    cipherBlockSize =  plainBlockSize + 1
    cipherBlocks = []
    numOfCipherBlocks = floor(len(cipherBitSeq)/cipherBlockSize)
    for i in range(0,numOfCipherBlocks):
        cipherBlocks.append(cipherBitSeq[i*cipherBlockSize: (i+1)*cipherBlockSize])
        cipherNumSeq = blocks2numberSeq(cipherBlocks)

    plainNumSeq = []
    for cipherNum in cipherNumSeq:
        plainNum = cipherNum**d % n
        plainNumSeq.append(plainNum)
    plainBlocks = numberSeq2Blocks(plainNumSeq,plainBlockSize)
    plainBitSeq = ""
    for pb in plainBlocks:
        plainBitSeq = plainBitSeq + pb
    return removePadding(plainBitSeq)
