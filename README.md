# About

It's a plugin for [csv2qif](https://github.com/fighterpoul/csv2qif-core) that allows the script to convert transactions written in `csv` exported from mBank into `qif` file that may be used in programs like HomeBank.

# Prerequisites

Please visit and install core module firstly: [csv2qif](https://github.com/fighterpoul/csv2qif-core)

# Installation

1. Make sure that your conda environment is active: `conda activate csv2qif`
1. Install the plugin: `python setup.py install`
1. Check if everything is OK:
```
> csv2qif-plugins 
mbank
```

# Usages

```shell script
> csv2qif transactions.csv mbank transactions.qif
```

# Troubleshooting

### Encoding issues
In case of any encoding issues you may need to fix encoding of the input csv file by running
```shell script
> iconv -f Windows-1250 -t utf-8 original_exported_transactions.csv > fixed_transactions_in_utf8.csv
```