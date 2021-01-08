import csv
import re
import os
import glob
from shutil import copyfile
import datetime
from bs4 import BeautifulSoup
import json
from mae_format import MAE_ANN
from nlp_mae_format import NLP_MAE_ANN
from xml.etree import ElementTree


class MaeViz:

    def __init__(self, resourDir, corpusDir, outDir, dtd_path):
        self.resourdir = resourDir
        self.corpusDir = corpusDir
        self.outDir = outDir
        self.corpus = []
        self.mae_corpus = {}
        self.dtd_path = dtd_path
        self.DELI = ','
        self.REPORT_ENDING_MARKER = '[- - - - - - - - - - - - - - - - - - -End of Report- - - - - - - - - - - - - - - - - - - -]'


    def load_corpus(self, warn_and_continue = False):

        try:
            self.corpus = self.file_reader(self.corpusDir, self.DELI)
        except:
            print ("Error for file %s: %s" % (self.corpusDir, str(self.corpus)))

    def load_corpus_dhs(self, warn_and_continue = False):
        dhs_file = glob.glob(self.corpusDir+'/*.tsv')
        try:
            self.corpus = self.file_reader(dhs_file[0], '\t')
        except:
            print ("Error for file %s: %s" % (self.corpusDir, str(dhs_file[0])))


    def file_reader(self, indir, d):
        out = []
        with open(indir, 'rU') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=d)
            for row in spamreader:
                out += [row]
        return out

    def get_idx(self, s, txt):
        txt = txt[:s]
        c = txt.count("\n\n") * 2
        return c

    def write_html(self, docData, reportName):
        fp = open(os.path.join(self.resourdir, "template.html"), "r")
        s = fp.read()
        fp.close()
        fp = open(os.path.join(self.outDir, reportName + ".html"), "w")
        fp.write(s.replace("TPL_DOCDATA", json.dumps(docData)))
        fp.close()

    def do_parse(self, corpusType):
         if corpusType == 'MAE':
            mae = MAE_ANN( self.resourdir, self.corpusDir, self.outDir, self.dtd_path)
            self.mae_corpus = mae.load_corpus()
            mae.load_dtd()
            for fname in self.mae_corpus:
                span_list = []
                idx = 0
                for ann, soup in enumerate(self.mae_corpus[fname]):
                    txtCorpus = soup[1].find('TEXT')
                    for sp in soup[1].find_all(mae.schemaElements):
                        idx += 1
                        try:
                            if sp.has_attr('spans'):
                                star, end = sp['spans'].split('~')[0], sp['spans'].split('~')[1]
                                span_list += [["T%d" % idx, "ANN"+str(ann+1)+'_'+sp.name, [star, end]]]
                            elif sp.has_attr('start'):
                                spans = sp['start'] + '~' + sp['end']
                                star, end = spans.split('~')[0], spans.split('~')[1]
                                span_list += [["T%d" % idx, "ANN" + str(ann + 1) + '_' + sp.name, [star, end]]]
                        except:
                            continue
                docData = {"text": txtCorpus.text,
                           "entities": [[i[0], i[1], [i[2]]] for i in span_list],
                           "normalizations": [[]],
                           "attributes": []}
                # print (self.outDir)
                self.write_html(docData, self.outDir+'/'+fname)
            print('Visualization saved at:', self.outDir)
         elif corpusType == 'NLP_MAE':
            mae = NLP_MAE_ANN( self.resourdir, self.corpusDir, self.outDir, self.dtd_path)
            self.mae_corpus, self.nlp_corpus = mae.load_corpus()
            mae.load_dtd()
            for fname in self.mae_corpus:
                span_list = []
                idx = 0
                for ann, soup in enumerate(self.mae_corpus[fname]):
                    txtCorpus = soup[1].find('TEXT')
                    for sp in soup[1].find_all(mae.schemaElements):
                        idx += 1
                        star, end = sp['spans'].split('~')[0], sp['spans'].split('~')[1]
                        span_list += [["T%d" % idx, "ANN"+str(ann+1)+'_'+sp.name, [star, end]]]
                if fname in self.nlp_corpus:
                    for ann, flist in enumerate(self.nlp_corpus[fname]):
                        for sp in flist[1]:
                            idx += 1
                            star, end = sp[4].split('\"')[1], sp[4].split('\"')[1]
                            span_list += [["T%d" % idx, "NLP"+str(ann+1)+'_'+sp[9].split('\"')[1], [star, end]]]
                docData = {"text": txtCorpus.text,
                           "entities": [[i[0], i[1], [i[2]]] for i in span_list],
                           "normalizations": [[]],
                           "attributes": []}
                self.write_html(docData, self.outDir+'/'+fname)
            print ('Visualization saved at:', self.outDir)

