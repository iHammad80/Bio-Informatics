x = 'ACCAGTATCATATGCCTAACACGTTGGATAGCGGTAACCTTCTATTCTTGCCTTCGGTATTTTTACTATAACTGCCCTTGGATCCGATATCGCCCTAAAGCCTCGAGTTTTCACCTTACATGATCCCACTTTTTTGCAGTCGGTTCAAAATAGGACTGCGGTTATTTGCAAGTGACCAAGGTTCGCGACTCTGTGGCTACGAGTGATGAAAGACTTGCTTGTAGGGCCAATCCGTAAGAGGTGATGCGGTGACAGTAAAGCGGACGGATAAACGGAGTGTCGGAGTTTATGGACGTATCAGACGGAATGTAAGTTGTTTAGTAATGGCCTTGAGGTGGACTATTAAAACCGGCGCGGTACCTAAAACACTTCCCTACTACATTCGCAGAACACTGAACACTTACCTACCCCTTTTGCCATTGCCCACCTGACACGAGGAGAACCCGCGCGACTGTGGCGGGCGAGTTGCCGCGTCCGAGAGTCCAGTCATATTATGCATATAACGGCTCTCGCAATCCGCGGCGAGGTCCCTCGTAAAGATCACGTCCAACGTATAATTAATGTGTCTTACAATCTAAAGGAATGGACCACCTTCAGACATGGCATATCCGTCAAATTTCCAACTGCTTGAGCTTGTAACACTTTTCACAGCAAGCTCCGGTGGTCTCTCTAAGTATCTCAATGGAATTCTATGATACGCGGTGAATTACGCAATGATGCGTTAAATGTCGACAAACATGGTTAACCGTCAATAATATTGCCCGCCTAGTCCGAGACTAGTATCATTCTGGCGAACATGTTCCCGTTCGGATCAGTTTCGTCGGGGGGCTTTCGTCCAGCAGGGCA'
y = {'A':'T','C':'G','G':'C','T':'A'}
s = ''
for i in x:
    z = str(y[i])
    s = s+z
print(s[::-1])
