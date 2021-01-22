import time
import csv
from bleurt import score

candidates = []
references = []

with open('newsela_aligned/newsela.test.dst') as f:
    candidates = f.read().splitlines()
f.close()

with open('newsela_aligned/newsela.test.src') as f:
    references = f.read().splitlines()
f.close()

# Number of training set sentences = 94208
# candidates = candidates[:1000]
# references = references[:1000]
print(len(candidates))

start_time = time.time()
checkpoint = "/home/yelman/Desktop/IS/bleurt-base-128"
scorer = score.BleurtScorer(checkpoint)
scores = scorer.score(references, candidates)

rows = zip(references, candidates, scores)


with open("BLEURT_output_test.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(("Reference", "Candidate", "BLEURT Score"))
    for row in rows:
        writer.writerow(row)
f.close()
print("--- Done!! Took %s seconds ---" % (time.time() - start_time))
