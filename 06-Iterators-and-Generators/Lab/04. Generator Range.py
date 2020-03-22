def genrange(start_idx, end_idx):
    while start_idx <= end_idx:
        yield start_idx
        start_idx +=1

print(list(genrange(1, 10)))