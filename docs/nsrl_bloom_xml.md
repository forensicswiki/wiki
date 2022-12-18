---
tags:
  - Digital Forensics XML
---
NSRL_Bloom XML is an XML Forensics object that is used to represent
bloom filters encoded using the NPS NSRL Bloom Filter package.

Parameters stored in the bloom filter XML are the number of bits in the
input hash, M (which is log2 of the number of bits in the Bloom filter),
the number of partitions from the hash function to use, a comment, and
the bloom filter itself. The bloom filter is typically encoded using
base64 coding and can optionally be compressed with zlib.

## Sample

This bloom filter holds the SHA1 codes of the ASCII numbers "0" through
"999":

    <nsrl_bloom version='2'>
      <hash_bits>160</hash_bits>
      <M>16</M>
      <k>4</k>
      <comment>A test of bloom filter in memory</comment>
      <data encoding='base64' compression='zlib'>eNrtWTtSZrkOto3oMn0
    J1BQBoaE6IGQJpqtvFcEELIGalRhqAibrJfRSWNq19bBl+zA3nOR3dQPn+CXL0qd
    POs6d2qmd2qmd2qmd2qmd2qmd2qmd2qmd2r/YyvgT6z/v+e9voXYVV58yD0p2Eny
    tr1/bX6E9pUwvnXuuL4q8peZd5D/6m9hWBHoVli7q9LyS6fE6QV4W+RGawDLimn4
    nnpPqhFt5lDXan9lxl2np2j6FSTG8ZYrmlaeHF9Ua6LiMs07BL8uijoTzOhdIjFi
    f47iDzAeRm/AB7BLfZDO/3h7o4SIU0zsd0vPNysrfy5hYJYMqaxEVjWPguI/kgZ8
    /7Oa5/btwcRImpUmLObl37KvhwzyWXvuh1dHhh9x6iVW2Yo8VxulF12MjmgFod4L
    PjD8vz8mcnRXQ3MDedt+30MiiWhrK97wwcE+bHMtkh2azGyQZkPsDzcBut79nm7S
    CBRTRv88H8PNZYuwejnJc2Hy+/g/qOHap5FLtgbDcMi0Z++ywXuDecPKoKqO8eO7
    rTe4S9WKa9oJ4WBsWp2PWIb7MvuvlUotT4FKFoIPAw6bzr4bRFhRvoOEQd/sQEUN
    9wLF7GOhlfriYwjQz7XiTjV69NUnMSdBPURFY1TEfafmtrfcArqMquF/04FXJejL
    czuT5d1s3h8s2PH9yl9E4QdGrzaCqLHyqOQaEQ9TaV2TrF3GuHOu4tjPpQXaJNW4
    B9Ods/KV6XUFRMBw4fEl5PEFyT6Gvy3f3tf0RnAJVXSP9pfHHSJG38KGXHH6PJzQ
    A/uazEeVZcedRZRzqyRhL0KDF+/oslvX3cMNDzYJx5PbzdR4YZJk4RxXQK4lDXWL
    b93y4P90StMb5PVqzuuRpr2QoPyIrAjZzaqtnPUjwBueKg2xsJBLWFFoiW50X+h+
    wdWCcUYfOdj0h/uvGfvTQr+4zw7zlN2BAuOA9rU+QkTb60FCOdexLR6bysS3dZv4
    k93UglsXESEJY0DgJw7bQ7obiiq3d0LCi6O8UfdwlA0CZXAeH1SKyfxG6FHUav8U
    Kub6KQNWrX3DWpN8pZbtfsMpmBWDQ7XPXxZUTdkX7YzNNv5pLC7PeWjdzumZqZDh
    ldYfX1vsmc0dvhpmtERvxM5kgn/2mIPSwmJQXclhRxpf57smgr6dnhmAYu0a5zVL
    tp0WTojHEhupm06xERZSf/eDJ3mGyr8+/rHFmSB2F4MCFQUOsv5Vrke7jh1qo0Wc
    /0F/HFHO6KkZxUWbKi4no3cUbPh0YnNGh8JJcSAY5dae82sTNINi0qu/QxJQKDrg
    9ce8ohgRXxoiTca7GiC4MiYjdVouZQUEml40lXG6MbCWfXjUZZqvLFiEI1IrVbKm
    aCzjA7+fOtvpSGlFHJwsnQBTt0CVs4ApVwsvetkDKv+7+KbXsWhHnaalCobPcqWG
    kPYRlCfxPnHTRZDb4rOwODCias2Il7gGS6jaoE3LKsJPliddI6EuHUb5sVLsYmYk
    4YdxHGwP0LZ1D058mVpGdJhCexWLRU9vji/yd5+UJXqpJVDB6PrAzHGydrVXERRU
    izgQgOIlctZ331C4mxsh+RzBlE3c078bA2HSLKYaeRBc+TIV+y6/pTIFx78FZsLR
    GAU2GGA+SN7hfxhsMDD/M+3w77uRqXLxfNsMDl5WYHG+hMKcZJuKtPHXrcNOF1vh
    ApQ8ppxwgdAuVmopz4SRVBr/nrpe8Ghq7Sl3paWW6xdo3OGsg5XHiOJdbFtm2iE+
    dWrTVv+z5c+NlHODCmUnvNG9kY80BOaGjo+FQc5m3JETq2bsBpzcDV+E7bjDTKzv
    dkd6LechdN3mxHc2TYYbqRlF+1a0eJp1g11iYCkytSJJExd5gym30TBFrgMhPFgg
    MfyMwnKwWOdKNi/N2ThxAqAab2XeEa1Uw9dnKjQsl9o3rBlsYa6lOOMwlQAN5G/Y
    7SUd07rCoYfH0j4NgoIcqn9RjELTiQ+QHranFg5qCDSv8CNaKyxJJBXB/Wt1mrqO
    wi+LkXJXt3MxnSGrV/Q2Tf0PSzHZU+cFAfKOL5TmTkfbVqZhHTAEydGNlBM2yfT/
    WhzsucMXdUx+mmEfcKC0X0ZL1TDceRlGY545sgKsoU2Jd5oTcK10ddeCLFhnKKJl
    pGuDSf+DCd1pmiznGxDEWt1SFWzzsR21FylsZf2/DKcz2gdb5Bc2rGFltTplZmIq
    HCTPXXyzvg2FmadE2zuTCFBp8L+lY28wpTPGDyw36a0H/Qil9nCxN8cE3F42mLMU
    E+OaA8bC7p90VuSAULMA7qcRxiSszPQjc0z0uTCFbqg7NpbeaDza4fLQq4XIwPLm
    DTHo1ar/35173oy2l/wezor04atTwSBufzSA2rPr9EN8yFym7Bd2PJcMqlddPCOE
    fq6OoMdxv1cZxQbckm1S5MXlKwIu8KL14GrTqC/DsRmmZsd6Ww6F/obnMbGwyLoY
    VRu7mvIt4dWa66ycym4+KudFQSwrNMOqmWw0r9bWkcv26ZJpeSz55IkG2NmPXI4S
    FR/2YQ1VV/LZ8A/BHZfZo7h5VF1pTKexvs31d9iUhan7imS2/dMnq88X/La9a4ap
    9vZn6d+yQZ+uX4gBlMBPVDVFOmxgQfz6fbOwj9R39qKmN60R3rdTxuNoPtg+Yvxj
    CZT8/+NX6k1SKQopjjbJ8bTlwoXTwZaQXM9qnqzHwfaXC5ivNfgc6Mb/0EDvZYM2
    i/jtX7ieQsOumz9JiJE9O3hY9apgpSgajZzzvdatqR+eUaSTJzCKLBgcpLH23OVN
    p7o5T62ajL6ZkUPo3vJJ6Dd1mFzbJuDSbFrUVnHDA91lJA2K0Hy9QOVUZS5GIV/m
    4pIA4l884Mw0oxZAclgJUqdf+TmPSL3MZiVCnHJoyTp+N4oJk+/eKyVLR6MfCSvk
    M+739ig1go1M1sZh6aWxuZ8Ouvqv3IJvM4g1pCPhFClyFlySFfP0fXurtlQ==</data>
    </nsrl_bloom>
