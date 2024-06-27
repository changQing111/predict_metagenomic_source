## Prediction of source flow based on microbial abundance data
The sample microbial abundance data file is under the `test_data/` folder
The script used is called `predict_class.py`, note that scikit-learn is available in version 1.1.2, other version maybe failed.
Usage:
```shell
python predict_class_pipe.py -f all_feature -l file_list.txt -m multi_class.model -c train_project_class.txt
```
`all_feature`, `multi_class.model`, `train_project_class.txt`
All three files can be downloaded here https://zenodo.org/records/12542364

`file_list.txt` microbial abundance data file path
```shell
$ cat file_list.txt
test_data/ERR2726431.txt
test_data/ERR2726438.txt
test_data/ERR3515526.txt
```
