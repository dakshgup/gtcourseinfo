from main import RateMyProfScraper
import pickle

gt = RateMyProfScraper(361)
toPrint = gt.professorlist

def save_object(obj, filename):
    with open(filename, 'wb') as output:  # Overwrites any existing file.
        pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)

save_object(toPrint, "C:/Users/daksh/Desktop/RegisterGT/profList.pkl")

print("done")