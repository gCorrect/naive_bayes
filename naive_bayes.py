#------PACKAGES-------
import pandas as pd
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '', 'libraries'))
# sys.path.append(r'C:/Users/nanas/python_libs')
from operations import *  
from loaddata import *  
from functions import *
#------DATA------------
data=pd.read_csv('data/play_tennis.csv')
#------VARIABLES-------
#   loaddata
database = "naive_bayes"
tablename = "play_tennis"
print_var(data, "data - file.csv ")
loaddata(database, tablename)
ordered_data =load_ordered_data(database, tablename, order_by_column = "play_tennis_num_val")
#------Probabilities----
p_feats = simple_feats_prob(data,database, tablename)
#   result = Yes
p_feat_inter_yes = p_feat_inter_result(data,database, tablename, result_value = "Yes")
p_feat_given_yes = p_feat_given_result(database, tablename, p_feats, p_feat_inter_yes, result_value = "Yes")
#   result = No
p_feat_inter_no = p_feat_inter_result(data,database, tablename, result_value = "No")
p_feat_given_no = p_feat_given_result(database, tablename, p_feats, p_feat_inter_no, result_value = "No")

input_feats = get_inputs(data.columns, database, tablename)
p_res_given_ev(data.columns, input_feats, p_feats, p_feat_given_yes, res_val="Yes")
p_res_given_ev(data.columns, input_feats, p_feats, p_feat_given_no, res_val="No")


print_title("END YEAH!!!") 





