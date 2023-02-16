matrix_DNA = []
no_of_seq = int(input('How many sequences you want to add? '))
for i in range(no_of_seq):
    x = str(input('Enter your sequence= '))
    matrix_DNA.append(x)
length_of_sequence = len(x)
initial_result = [0]*length_of_sequence
profile = {'A': initial_result[:],
          'C': initial_result[:],
          'G': initial_result[:],
          'T': initial_result[:]}
for j in matrix_DNA:
    for k,l in enumerate(j):
        profile[l][k] += 1

result = []
AGCT = profile.keys()

for m in range(length_of_sequence):
    max_count = 0
    max_value = None
    for n in AGCT:
        count = profile[n][m]
        if count > max_count:
            max_count = count
            max_value = n
    result.append(max_value)
        
consensus = ''.join(result)
print(f'\n{consensus}')

for y,z in profile.items():
    a = []
    for c in z:
        d = str(c)
        a.append(d)
    b = ' '.join(a)
    print(f'{y}: {b}')