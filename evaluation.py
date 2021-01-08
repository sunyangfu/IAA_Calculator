from os.path import expanduser

class Evaluation:
    def __init__(self, ann1Corpus, ann2Corpus, dtdDir, overlap_ratio):
        self.labels = {}
        self.schemaElementsAttr = self.load_dtd(dtdDir)
        self.annSpan, self.txtCorpus = self.get_spans(ann1Corpus, ann2Corpus)
        self.cpLevelOutput = []
        self.overlap_ratio = overlap_ratio

    def read_txt(self, indir):
        f = open(indir, 'r')
        txt = f.read()
        f.close()
        return txt

    def load_dtd(self, dtdDir):
        txt = self.read_txt(dtdDir)
        schemaElements = {}
        for i in txt.split('\n'):
            if '<!ATTLIST' in i:
                ele = i.split(' ')[1]
                schemaElements[ele] = {}
        for i in txt.split('\n'):
            if '<!ATTLIST' in i:
                ele = i.split(' ')[1]
                attr = i.split(' ')[2]
                if "(" in i and ")" in i:
                    attrList = [sub_attr.strip() for sub_attr in i.split('(')[1].split(')')[0].split('|')]
                else:
                    attrList = []
                if attr not in schemaElements[ele]:
                    schemaElements[ele][attr] = attrList
                else:
                    schemaElements[ele][attr] = schemaElements[ele][attr]+attrList
        return schemaElements

    def get_spans(self, ann1Corpus, ann2Corpus):
        spanCorpus, txtCorpus, attrCorpus = {}, {}, {}
        ann2Pool = [i.split('/')[-1] for i in ann2Corpus]
        for i in ann1Corpus:
            doc_name = i.split('/')[-1]
            if doc_name not in ann2Pool:
                continue
            spanCorpus[doc_name] = {}
            txtCorpus[doc_name] = {}
            soup = ann1Corpus[i]
            # for e in self.dtdElements
            for mae_concept in self.schemaElementsAttr:
                for item in soup.find_all(mae_concept):
                    mae_cp = item.name
                    try:
                        txt = item['text']
                    except:
                        txt = ''
                    #get spans from MEA v0.9 and v2.0
                    if item.has_attr('spans'):
                        attrDict = {}
                        if ',' in item['spans']:
                            continue
                        key_ = doc_name + item.name + 'ann1' + item['spans']
                        attrList = self.schemaElementsAttr[mae_concept]
                        for at in attrList:
                            if item.has_attr(at):
                                if at not in attrDict:
                                    attrDict[at] = item[at]
                        try:
                            spanCorpus[doc_name][item.name]['ann1'].append(item['spans'])
                        except KeyError:
                            spanCorpus[doc_name][item.name] = {"ann1": [item['spans']], "ann2": []}
                        if key_ not in txtCorpus:
                            txtCorpus[key_] = [txt, attrDict]
                    elif item.has_attr('start'):
                        attrDict = {}
                        spans = item['start']+'~'+item['end']
                        key_ = doc_name + item.name + 'ann1' + spans
                        attrList = self.schemaElementsAttr[mae_concept]
                        for at in attrList:
                            if item.has_attr(at):
                                if at not in attrDict:
                                    attrDict[at] = item[at]
                        try:
                            spanCorpus[doc_name][item.name]['ann1'].append(spans)
                        except KeyError:
                            spanCorpus[doc_name][item.name] = {"ann1": [spans], "ann2": []}
                        if key_ not in txtCorpus:
                            txtCorpus[key_] = [txt, attrDict]
        for i in ann2Corpus:
            doc_name = i.split('/')[-1]
            if doc_name not in spanCorpus:
                continue
            soup = ann2Corpus[i]
            for mae_concept in self.schemaElementsAttr:
                for item in soup.find_all(mae_concept):
                    try:
                        txt = item['text']
                    except:
                        txt = ''
                    if item.has_attr('spans'):
                        if ',' in item['spans']:
                            continue
                        # spans = item['spans'].split('~')
                        txtCorpus[doc_name][item.name] = {'ann1':{}, 'ann2':{}}
                        key_ = doc_name + item.name + 'ann2' + item['spans']
                        attrDict = {}
                        attrList = self.schemaElementsAttr[mae_concept]
                        for at in attrList:
                            if item.has_attr(at):
                                if at not in attrDict:
                                    attrDict[at] = item[at]
                        try:
                            spanCorpus[doc_name][item.name]['ann2'].append(item['spans'])
                        except KeyError:
                            spanCorpus[doc_name][item.name] = {"ann1": [], "ann2": [item['spans']]}
                        if key_ not in txtCorpus:
                            txtCorpus[key_] = [txt, attrDict]
                    elif item.has_attr('start'):
                        spans = item['start']+'~'+item['end']
                        txtCorpus[doc_name][item.name] = {'ann1':{}, 'ann2':{}}
                        key_ = doc_name + item.name + 'ann2' + spans
                        attrDict = {}
                        attrList = self.schemaElementsAttr[mae_concept]
                        for at in attrList:
                            if item.has_attr(at):
                                if at not in attrDict:
                                    attrDict[at] = item[at]
                        try:
                            spanCorpus[doc_name][item.name]['ann2'].append(spans)
                        except KeyError:
                            spanCorpus[doc_name][item.name] = {"ann1": [], "ann2": [spans]}
                        if key_ not in txtCorpus:
                            txtCorpus[key_] = [txt, attrDict]
        return spanCorpus, txtCorpus

    def do_calculation_averaged(self, spanCorpus):
        tp_doc, fp_doc, fn_doc = 0, 0, 0
        print("TOTAL MICRO AVERAGE:")
        print ('(Aggregation the contributions of all classes)')
        for doc in spanCorpus:
            for cp in spanCorpus[doc]:
                tp, fp, fn = self._cal_matching_overlap(spanCorpus[doc][cp]['ann1'], spanCorpus[doc][cp]['ann2'])
                tp_doc += tp
                fp_doc += fp
                fn_doc += fn
                self.cpLevelOutput += [[doc, cp, tp, fp, fn]]
        self.get_pr_f1(tp_doc, fp_doc, fn_doc)

    def do_calculation_cp_level(self, spanCorpus):
        tp_doc, fp_doc, fn_doc = 0, 0, 0
        for doc in spanCorpus:
            for cp in spanCorpus[doc]:
                tp, fp, fn = self._cal_matching_overlap(spanCorpus[doc][cp]['ann1'], spanCorpus[doc][cp]['ann2'])
                tp_doc += tp
                fp_doc += fp
                fn_doc += fn
                self.cpLevelOutput += [[doc, cp, tp, fp, fn]]
        cp_d = {}
        for cp in self.cpLevelOutput:
            if cp[1] not in cp_d:
                cp_d[cp[1]] = [cp[2], cp[3], cp[4]]
            else:
                cp_d[cp[1]] = [cp_d[cp[1]][0]+cp[2], cp_d[cp[1]][1]+cp[3], cp_d[cp[1]][2]+cp[4]]
        precision_macro, recall_macro, f1_macro = [],[],[]
        for k in cp_d:
            print ('concept name:', k)
            if cp_d[k][0] == 0:
                print ('0 TP found in', k, 'please double check your result')
                continue
            precision, recall, f1 = self.get_pr_f1(cp_d[k][0], cp_d[k][1], cp_d[k][2])
            precision_macro += [precision]
            recall_macro += [recall]
            f1_macro += [f1]
        print ('')
        print ('____________________')
        print ('TOTAL MACRO AVERAGE:')
        print ('(Compute the metric independently for each class)')
        print("Precision\tRecall\tF1")
        print("{:.4f}\t{:.4f}\t{:.4f}".format(sum(precision_macro)/float(len(precision_macro)), sum(recall_macro)/float(len(recall_macro)), sum(f1_macro)/float(len(f1_macro))))
        print('')

    def print_mismatch(self, spanCorpus, txtCorpus, corpusDir):
        home = expanduser("~")
        txt = 'annotation_file|concept_name|annotator|spans|agreement|text'+'\n'
        for doc in spanCorpus:
            for cp in spanCorpus[doc]:
                txt += self.print_cp_evidence(spanCorpus, doc, cp, txtCorpus)
        our_dir = corpusDir.replace('/input', '/output') + "/annotation_result.csv"
        with open(our_dir, "wb") as text_file:
            text_file.write(txt.encode('utf-8'))
        print ('File saved at:', our_dir)

    def get_pr_f1(self, tp, fp, fn):
        print("TP\tFP\tFN\t")
        print("{}\t{} \t{}".format(tp, fp, fn))
        try:
            precision = tp / float(tp + fp)
            recall = tp / float(tp + fn)
            specificity = fn
            f1 = 2 * precision * recall / (precision + recall)
            iaa_ratio = tp / float(tp + fp + fn)
            print("Precision\tRecall\tF1")
            print("{:.4f}\t{:.4f}\t{:.4f}".format(precision, recall, f1))
            print ('')
            return precision, recall, f1
        except:
            print ("division zero error")

    def get_f1(self, tp, fp, fn):
        try:
            precision = tp / float(tp + fp)
            recall = tp / float(tp + fn)
            f1 = 2 * precision * recall / (precision + recall)
            print(f1)
        except:
            print ("division zero error")

    def overlap(self, idx_a_str, ann2):
        for idx_b_str in ann2:
            idx_a = idx_a_str.split('~')
            idx_b = idx_b_str.split('~')
            aIndices = set(range(int(idx_a[0]), int(idx_a[1])))
            bIndices = set(range(int(idx_b[0]), int(idx_b[1])))
            overlap = len(aIndices & bIndices) / float(len(aIndices | bIndices))
            if overlap >= self.overlap_ratio:
                return True
        return False

    def cal_matching_exact(self, ann1, ann2):
        tp, fp = 0, 0
        for sp in ann1:
            if sp in ann2:
                tp += 1
            else:
                fp += 1
        fn = len(ann2) -  tp
        return tp, fp, fn

    def _cal_matching_overlap(self, ann1, ann2):
        tp, fp = 0, 0
        for sp in ann1:
            if sp in ann2:
                tp += 1
            elif self.overlap(sp, ann2):
                tp += 1
            else:
                fp += 1
        fn = len(ann2) -  tp
        return tp, fp, fn

    def apply_transpose(self, attrDict, cp):
        for cp_ in self.schemaElementsAttr:
            if cp_ == cp:
                print (cp, self.schemaElementsAttr[cp])


    def print_cp_evidence(self, spanCorpus, doc, cp, txtCorpus):
        ann1 = spanCorpus[doc][cp]['ann1']
        ann2 = spanCorpus[doc][cp]['ann2']
        txt = ''
        tp, fp = 0, 0
        for sp in ann1:
            key_ = doc + cp + 'ann1' + sp
            # self.apply_transpose(txtCorpus[key_][1], cp)
            att_txt = ''
            for m in txtCorpus[key_][1]:
                att_txt += m+': '+txtCorpus[key_][1][m]+'|'
            if sp in ann2:
                tp += 1
                txt += doc + '|' + cp + '|' + 'ann1' + '|' + sp + '|' + 'agree' + '|' + txtCorpus[key_][0] + '|' + att_txt + '\n'
            elif self.overlap(sp, ann2):
                tp += 1
                txt += doc+ '|'+ cp+ '|'+ 'ann1'+ '|'+ sp+ '|'+ 'agree'+ '|'+ txtCorpus[key_][0]+ '|'+ att_txt+ '\n'
            else:
                fp += 1
                txt += doc+ '|'+ cp+ '|'+ 'ann1'+ '|'+ sp+ '|'+'disagree'+ '|'+txtCorpus[key_][0]+ '|'+ att_txt + '\n'
        for sp2 in ann2:
            key_ = doc + cp + 'ann2' + sp2
            att_txt = ''
            for m in txtCorpus[key_][1]:
                att_txt += m+': '+txtCorpus[key_][1][m]+'|'
            if sp2 in ann1:
                txt += doc+ '|'+ cp+ '|'+ 'ann2'+ '|'+ sp2+ '|'+ 'agree'+ '|'+ txtCorpus[key_][0]+ '|'+ att_txt + '\n'
            elif self.overlap(sp2, ann1):
                txt += doc+ '|'+ cp+ '|'+ 'ann2'+ '|'+ sp2+ '|'+ 'agree'+ '|'+ txtCorpus[key_][0]+ '|'+ att_txt + '\n'
            else:
                txt += doc+ '|'+ cp+ '|'+ 'ann2'+ '|'+ sp2+ '|'+ 'disagree'+ '|'+txtCorpus[key_][0]+ '|'+ att_txt + '\n'
        fn = len(ann2) -  tp
        return txt