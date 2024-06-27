## Prediction of source flow based on microbial abundance data
The sample microbial abundance data file is under the `test_data/` folder for test, the format of other input data is the same as the file format in this folder.

Note1: that scikit-learn is available in version 1.1.2, other version maybe failed.

Note2: Due to the large size of the model, it requires more than 16G of memory to run

The script used is called `predict_class.py`
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
output result:
```shell
FileName BioProject Class
ERR2726438.txt PRJEB11532      human_gut
ERR2726431.txt PRJEB11532      human_gut
ERR3515526.txt PRJEB34231      bovine_rumen
```
The output has three columns, the first column is file name, the second column is BioProject, the third column is the category that BioProject corresponds to
