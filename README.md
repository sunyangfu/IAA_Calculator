# IAA Calculator for MAE


### Prerequisites

python 3.0 above

### Configuration
place .dtd file to IAA_Calculator/input/dtd

place annotated .xml files to 
IAA_Calculator/input/annotation/ann1
IAA_Calculator/input/annotation/ann2

Open config.yml, modify corpus path and .dtd path
corpus path example: full_direcctory + IAA_Calculator/input/annotation/ (do not put ann1 or ann2)
dtd path example: full path + IAA_Calculator/input/dtd

## Runn program

By default this will output the concept specific agreement and total averaged agreement
```
python main.py
```

To modify the span ratio:
```
python main.py -ratio 0.7
```

To print out mis-matched cases:
```
python main.py -mismatch 1
```

To visualize annotation results:
```
python main.py -vis 1
```

To perform all features:
```
python main.py -vis 1 -mismatch 1 -ratio 0.7
```
