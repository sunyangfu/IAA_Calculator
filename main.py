import argparse
import os
import sys
import yaml
from visualize import MaeViz
from corpus import Corpus
from evaluation import Evaluation
import glob


def str2bool(v):
    if isinstance(v, bool):
       return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')

parser = argparse.ArgumentParser(description='MAE IAA Calculator')
parser.add_argument('-ratio', type=float, default=0.5, help='span matching ratio [default: 0.5]')
parser.add_argument('-mismatch', type=str2bool, default=False, help='print mis-matched cases')
parser.add_argument('-cp-level', type=str2bool, default=True, help='calculate concept level IAA')
parser.add_argument('-total-average', type=str2bool, default=True, help='calculate document level IAA')
parser.add_argument('-vis', type=str2bool, default=False, help='plot ann visualization plot')

args = parser.parse_args()
with open("config.yml", 'r') as ymlfile:
    cfg = yaml.safe_load(ymlfile)

ROOTDIR = os.path.dirname(os.path.abspath(__file__))
RESOURCE_DIR = os.path.join(ROOTDIR, "resources")
INPUT_DIR = os.path.join(ROOTDIR, "input")
OUTPUT_DIR_VIZ = os.path.join(ROOTDIR, "output/viz_out")

corpusDir= cfg["datasets"][cfg["datasets"]["choice"]]["corpus"]["path"]
dtd_path = cfg["datasets"][cfg["datasets"]["choice"]]["dtd_file"]["path"]

print ('program start...')
print ('corpus dir: ', corpusDir)
print ('dtd dir: ', dtd_path)

sub_dir = glob.glob(corpusDir+'/*')
if len(sub_dir) == 2:
    ann1Corpus = Corpus(sub_dir[0])
    ann2Corpus = Corpus(sub_dir[1])
else:
    print ('check sub folder configuration')

#IAA calculation
parsedCorpus = Evaluation(ann1Corpus.soup, ann2Corpus.soup, dtd_path)
if args.cp_level == True:
    print ('CONCEPT SPECIFIC AGREEMENT:')
    parsedCorpus.do_calculation_cp_level(parsedCorpus.annSpan)
    print ()
if args.total_average == True:
    print('TOTAL AVERAGE AGREEMENT:')
    parsedCorpus.do_calculation_averaged(parsedCorpus.annSpan)
    print()
if args.mismatch == True:
    print('PRINTING MISMATCH:')
    parsedCorpus.print_mismatch(parsedCorpus.annSpan, parsedCorpus.txtCorpus, corpusDir)

#output visualization
if args.vis == True:
    eval = MaeViz(RESOURCE_DIR, corpusDir, OUTPUT_DIR_VIZ, dtd_path)
    eval.do_parse('MAE')

