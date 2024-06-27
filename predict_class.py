import argparse
import sys
import os
import pickle
import warnings
import math
import numpy as np

def read_params():
    parser = argparse.ArgumentParser(description="predict metagenomics class")
    parser.add_argument("-f", "--feature", action="store", help="all feature")
    parser.add_argument("-l", "--list", action="store", help="sample list")
    parser.add_argument("-m", "--model", action="store", help="model path")
    parser.add_argument("-c", "--category", action="store", help="category path")
    args = parser.parse_args()

    return args

def load_all_species(species_path):
    with open(species_path, 'rb') as f:
        species_li = pickle.load(f)
    return species_li

def read_profile(file_name):
    profile_dic = {}
    with open(file_name, "rt") as f:
        for i in f:
            i = i.rstrip()
            li = i.split('\t')
            profile_dic[li[-1]] = li[0]
    return profile_dic

def shape_profile(file_list_path, all_species_li):
    with open(file_list_path, "rt") as f:
        file_li = [i.rstrip() for i in f]
    all_profile_dic = {}
    for i in file_li:
        all_profile_dic[i] = read_profile(i)
    
    profile_mat = np.zeros((len(file_li), len(all_species_li)))
    for row, sp_ratio in enumerate(all_profile_dic.values()):
        for col, sp in enumerate(all_species_li):
            if sp in sp_ratio:
                profile_mat[row, col] = sp_ratio[sp]
    return (profile_mat, file_li)


def load_model(model_path):
    f = open(model_path, 'rb')
    model = pickle.load(f)
    f.close()
    return model

def load_class(project_class_path):
    with open(project_class_path, "rt") as f:
        num_label_map = {index:i.rstrip() for index, i in enumerate(f)}
    return num_label_map

def predict_class(X, model_path):
    model = load_model(model_path)
    Y_pred = model.predict(X)
    pass

if __name__ == "__main__":
    args = read_params()
    all_species_path = args.feature
    file_li_path = args.list
    model_path = args.model
    class_path = args.category
    
    # load all species
    all_species = load_all_species(all_species_path)
    # shape profile matrix
    X, name_li = shape_profile(file_li_path, all_species)
    # load trained model
    model = load_model(model_path)
    # load class
    num_label_map = load_class(class_path)
    # predict
    Y_pred = model.predict(X)
    print("FileName", "BioProject", "Class", sep='\t')
    for i, j in zip(name_li, Y_pred):
        print(i, num_label_map[j], sep='\t')
    
          
        
      
 







