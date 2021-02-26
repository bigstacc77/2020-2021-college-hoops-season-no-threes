from more_itertools import unique_everseen
with open('output.csv','r') as f, open('output_cleaned.csv','w') as out_file:
    out_file.writelines(unique_everseen(f))
