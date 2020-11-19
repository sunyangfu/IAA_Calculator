import csv
import re
import os
import glob
from shutil import copyfile
import datetime
from bs4 import BeautifulSoup
import json
from xml.etree import ElementTree
from lxml import etree


class NLP_MAE_ANN():

    def __init__(self, resourDir, corpusDir, outDir, dtdDir):
        self.resourdir = resourDir
        self.corpusDir = corpusDir
        self.outDir = outDir
        self.dtdDir = dtdDir
        self.corpus_mae,self.corpus_nlp  = {},{}
        self.schemaElements = []
        self.load_dtd()
        self.update_js_elements()

    def load_corpus(self, warn_and_continue=False):
        for subdir, dirs, files in os.walk(self.corpusDir):
            # print subdir, dirs, files
            if '.xml' in ''.join(files):
                annname = subdir.split(os.path.sep)[-1]
                for fname in files:
                    if fname == '' or fname == [] or '.xml' not in fname:
                        continue
                    # print fGenericName
                    fGenericName = fname.split('.')[0]
                    fGenericName = '_'.join(fGenericName.split('_')[:4])
                    fp = open(subdir + '/' + fname).read()
                    soup = BeautifulSoup(fp, 'xml')
                    if fGenericName not in self.corpus_mae:
                        self.corpus_mae[fGenericName] = [[fGenericName, soup]]
                    else:
                        self.corpus_mae[fGenericName] = self.corpus_mae[fGenericName] + [[fGenericName, soup]]
            if '.ann' in ''.join(files):
                for fname in files:
                    if fname == '' or fname == [] or '.ann' not in fname:
                        continue
                    flist = self.read_file_list(subdir + '/' + fname, '\t')
                    fGenericName = fname.split('.')[0]
                    if fGenericName not in self.corpus_nlp:
                        self.corpus_nlp[fGenericName] = [[fGenericName, flist]]
                    else:
                        self.corpus_nlp[fGenericName] = self.corpus_nlp[fGenericName] + [[fGenericName, flist]]
        return (self.corpus_mae,self.corpus_nlp)

    def read_file_list(self, indir, d):
        opt_notes = []
        with open(indir, 'rU') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=d)
            for row in spamreader:
                opt_notes += [row]
        return opt_notes

    def read_dtd(self, indir):
        f = open(indir, 'r')
        txt = f.read()
        f.close()
        return txt

    def load_dtd(self):
        txt = self.read_dtd(self.dtdDir)
        for i in txt.split('\n'):
            if '!ELEMENT' in i and i != '':
                self.schemaElements += [i.split(' ')[1].strip()]

    def run_test(self):
        for i in self.corpus:
            print (i, len(self.corpus[i]))

    def update_js_elements(self):
        js_template = self.read_dtd('resources/js/labelviz_template.txt')

        ele_str = ''
        for e in self.schemaElements:
            as1 = 'ANN1_'+e
            inital_str = "{ type: '%s', labels: ['%s'], bgColor: 'limegreen',}," % (as1, as1)
            ele_str += inital_str

        for e in self.schemaElements:
            as2 = 'ANN2_'+e
            inital_str = "{ type: '%s', labels: ['%s'], bgColor: 'yellow',}," % (as2, as2)
            ele_str += inital_str
        js_out = js_template.split('|')[0]+ele_str+js_template.split('|')[1]

        with open("output/viz_out/js/labelviz.js", "w") as text_file:
            text_file.write(js_out)


