# card-drawing

Small script to calculate card drawing probability (MTG)

# Usage 1: Starting Propa

Show probability to draw each card given a 7 card hand

```
NAME
    app.py

SYNOPSIS
    app.py <flags>

FLAGS
    --deck_file=DECK_FILE
```

## Example Output:

```
                                           Qty    1+         2+         3+         4+         5+         6+         7+
  0 Mountain                                 17     0.91656    0.64821    0.30924    0.09195    0.01590    0.00143    0.00005
  1 Torbran, Thane of Red Fell               4      0.39950    0.06322    0.00388    0.00007
  2 Shock                                    4      0.39950    0.06322    0.00388    0.00007
  3 Scorch Spitter                           4      0.39950    0.06322    0.00388    0.00007
  4 Runaway Steam-Kin                        4      0.39950    0.06322    0.00388    0.00007
  5 Robber of the Rich                       4      0.39950    0.06322    0.00388    0.00007
  6 Rimrock Knight                           4      0.39950    0.06322    0.00388    0.00007
  7 Fervent Champion                         4      0.39950    0.06322    0.00388    0.00007
  8 Castle Embereth                          4      0.39950    0.06322    0.00388    0.00007
  9 Slaying Fire                             3      0.31543    0.03355    0.00102
 10 Tibalt, Rakish Instigator                2      0.22147    0.01186
 11 Light Up the Stage                       2      0.22147    0.01186
 12 Footlight Fiend                          2      0.22147    0.01186
 13 Skewer the Critics                       1      0.11667
 14 Chandra, Acolyte of Flame                1      0.11667
Total                                        60
```

# Usage 2: Interactive proba

Probability to draw each card given a 7 card hand. And probabilty to get next card given the already drawn cards. Each iteration you given the index of the card you draw.

```
NAME
    app.py

SYNOPSIS
    app.py <flags> none

FLAGS
    --deck_file=DECK_FILE
```


## Output Example for second iteration with a starting hand of (indexes of drawn card : 0 1 2 3 4 5 6)

```
                                             Qty    1+
  0 Mountain                                 16     0.30189
  1 Fervent Champion                         4      0.07547
  2 Castle Embereth                          4      0.07547
  3 Torbran, Thane of Red Fell               3      0.05660
  4 Slaying Fire                             3      0.05660
  5 Shock                                    3      0.05660
  6 Scorch Spitter                           3      0.05660
  7 Runaway Steam-Kin                        3      0.05660
  8 Robber of the Rich                       3      0.05660
  9 Rimrock Knight                           3      0.05660
 10 Tibalt, Rakish Instigator                2      0.03774
 11 Light Up the Stage                       2      0.03774
 12 Footlight Fiend                          2      0.03774
 13 Skewer the Critics                       1      0.01887
 14 Chandra, Acolyte of Flame                1      0.01887
Total                                        53
```
