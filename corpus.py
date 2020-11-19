import glob
from bs4 import BeautifulSoup
import csv
class Corpus:
    def __init__(self, corpusDir, format='mae'):
        self.dir = corpusDir
        self.soup = {}
        if format=='mae':
            self.files = glob.glob(corpusDir + '/*.xml')
            self.load_MAE()
        if format=='brat':
            self.files = glob.glob(corpusDir + '/*.ann')
            self.load_Brat()

    def load_MAE(self, warn_and_continue = False):
        for p in self.files:
            name= p.split('/')[-1]
            ## standard:
            # name = p.split('/')[-1].split('_')[0]+'.xml'
            try:
                fp = open(p).read()
                soup = BeautifulSoup(fp, 'xml')
                self.soup[name] = soup
            except:
                print ("Error for file")

    def load_Brat(self, warn_and_continue = False):
        for p in self.files:
            ann_list =  self.read_file_list(p)
            # name= '_'.join(p.split('/')[-1].split('_')[:4])
            ## standard:
            name = p.split('/')[-1].split('_')[0]+'.ann'


    def read_file_list(self, indir, d):
        opt_notes = []
        with open(indir, 'rU') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=d)
            for row in spamreader:
                opt_notes += [row]
        return opt_notes

