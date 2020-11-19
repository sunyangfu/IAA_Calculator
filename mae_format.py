import os
from bs4 import BeautifulSoup


class MAE_ANN():

    def __init__(self, resourDir, corpusDir, outDir, dtdDir):
        self.resourdir = resourDir
        self.corpusDir = corpusDir
        self.outDir = outDir
        self.dtdDir = dtdDir
        self.corpus = {}
        self.schemaElements = []

        self.load_dtd()
        self.update_js_elements()

    def load_corpus(self, warn_and_continue=False):
        for subdir, dirs, files in os.walk(self.corpusDir):
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
                    if fGenericName not in self.corpus:
                        self.corpus[fGenericName] = [[fGenericName, soup]]
                    else:
                        self.corpus[fGenericName] = self.corpus[fGenericName] + [[fGenericName, soup]]

        return self.corpus

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


