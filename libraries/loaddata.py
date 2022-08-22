import mysql.connector
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '', 'libraries'))
# sys.path.append(r'C:/Users/nanas/python_libs')
from operations import *
from functions import *
# 2D---------------------------------
def loadPlotData(tablename):
    # database connection
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="perceptron"
    )
    # variables of data
    x1 = []
    y1 = []
    x2 = []
    y2 = []
    # cursor, execution, result -> C1
    c1 = mydb.cursor()
    query = "SELECT * FROM "+tablename+" WHERE EO=0"
    c1.execute(query)
    result_c1 = c1.fetchall()
    # print("Result for c1: \n",result_c1)
    # cursor, execution, result -> C2
    c2 = mydb.cursor()
    query = "SELECT * FROM "+tablename+" WHERE EO=1"
    c2.execute(query)
    result_c2 = c2.fetchall()
    # print("Result for c2: \n",result_c2)
    # # x1[],y1[]        
    for row in result_c1:
        x1.append(row[0])
        y1.append(row[1])
    # x2[],y2[]        
    for row in result_c2:
        x2.append(row[0])
        y2.append(row[1])
    return x1,y1,x2,y2

def loaddata(database, tablename):
    # database connection
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database=database
    )
    cursor = mydb.cursor()
    query = "SELECT * FROM "+tablename
    cursor.execute(query)
    result = cursor.fetchall()
    # print 
    print_title = "database : "+database+" - table: "+tablename    
    print_array(result, print_title)   
    return result

def loadTupleData(tablename):
    # database connection
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="perceptron"
    )
    # cursor, execution, result -> C1
    cursor = mydb.cursor()
    query = "SELECT x1,x2 FROM "+tablename
    cursor.execute(query)
    result = cursor.fetchall()
    query = "SELECT EO FROM "+tablename
    cursor.execute(query)
    resultEO = cursor.fetchall()
    print("---------------------------")

    print("Result for EO: \n")
    print(resultEO)
    print(type(resultEO))

    alldata= list(zip(result,resultEO))
    return alldata

def loaddataPerCategory(tablename):
    # database connection
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="perceptron"
    )
    # cursor, execution, result -> C1
    cursor = mydb.cursor()
    query = "SELECT x1,x2 FROM "+tablename+ " WHERE category='C1'"
    cursor.execute(query)
    result = cursor.fetchall()
    print("---------------------------")
    print("Result for C1: \n")
    print(result)
    print(type(result))
    return result
# 3D---------------------------------

def load3DPlotData(tablename):
    # database connection
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="perceptron"
    )
    # variables of data
    x1 = []
    y1 = []
    z1 = []
    x2 = []
    y2 = []
    z2 = []
    # cursor, execution, result -> C1
    c1 = mydb.cursor()
    query = "SELECT x1,x2,x3 FROM "+tablename+" WHERE EO=0"
    c1.execute(query)
    result_c1 = c1.fetchall()
    # print("Result for c1: \n",result_c1)
    # cursor, execution, result -> C2
    c2 = mydb.cursor()
    query = "SELECT x1,x2,x3 FROM "+tablename+" WHERE EO=1"
    c2.execute(query)
    result_c2 = c2.fetchall()
    # print("Result for c2: \n",result_c2)
    # # x1[],y1[]        
    for row in result_c1:
        x1.append(row[0])
        y1.append(row[1])
        z1.append(row[2])
    # x2[],y2[]        
    for row in result_c2:
        x2.append(row[0])
        y2.append(row[1])
        z2.append(row[2])
    return x1,y1,z1,x2,y2,z2

def load3DTupleData(tablename):
    # database connection
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="perceptron"
    )
    # cursor, execution, result -> C1
    cursor = mydb.cursor()
    query = "SELECT x1,x2,x3 FROM "+tablename
    cursor.execute(query)
    result = cursor.fetchall()
    query = "SELECT EO FROM "+tablename
    cursor.execute(query)
    resultEO = cursor.fetchall()
    # print("---------------------------\n","Result for EO: \n", resultEO,"\n type: ", type(resultEO))    
    alldata= list(zip(result,resultEO))
    return alldata
# naive_bayes------------------------
# table_tennis
def load_ordered_data(database, tablename, order_by_column):
    # database connection
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database=database
    )
    cursor = mydb.cursor()
    query = "SELECT outlook, temperature, humidity, wind, play_tennis FROM "+tablename+" ORDER BY "+order_by_column
    cursor.execute(query)
    result = cursor.fetchall()
    print_title = tablename +" ORDER BY -> "+order_by_column 
    print_array(result, print_title)   
    return result

def facts_per_category(database, tablename, category, cat_value):
    # database connection
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database=database
    )
    # cursor, execution, result -> C1
    cursor = mydb.cursor()
    query = "SELECT outlook, temperature, humidity, wind, play_tennis FROM "+tablename+" WHERE `"+category+"`='"+cat_value+"'"
    cursor.execute(query)
    result = cursor.fetchall()
    # print 
    print_title = category +" = "+ cat_value 
    # print_array(result, print_title)
    return result

def facts_per_result(database, tablename, category, cat_value, result_value): 
    # database connection
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database=database
    )
    # cursor, execution, result 
    cursor = mydb.cursor()
    query = "SELECT outlook, temperature, humidity, wind, play_tennis FROM "+tablename+" WHERE `"+category+"`='"+cat_value+"' AND play_tennis ='"+result_value+"'"
    cursor.execute(query)
    result = cursor.fetchall()
    # print 
    print_title = category +" = "+ cat_value +" AND result= " + result_value
    print_array(result, print_title)
    return result

def uniq_ordered_feats(database, tablename, category):
    # database connection
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database=database
    )
    # cursor, execution, result 
    cursor = mydb.cursor()
    query = "SELECT DISTINCT `"+category+"` FROM `"+tablename+"` ORDER BY "+category+"_num_val"
  
    cursor.execute(query)
    result = cursor.fetchall()
    # print 
    print_title = "unique values of "+category
    # print_array(result, print_title)
    return result

def simple_feats_prob(data, database, tablename):
    print_title("Function: Simple feature probabilities()") 

    len_data= len(data)
    p_feats = dict()

    for column_name in data:
        unique_column_values=uniq_ordered_feats(database, tablename, column_name)
        p_feat = dict()
        for column_value in unique_column_values:        
            # calculate for simple probabilities
            facts_per_cat = facts_per_category(database, tablename, category= column_name, cat_value= column_value[0])
            p_value = P(len(facts_per_cat), len_data)
            key = "p_"+column_value[0]
            p_feat[key] = p_value
        p_feats[column_name] = p_feat # simple probablities
    print_dict(p_feats, "p_feats")    
    return p_feats

def p_feat_inter_result(data, database, tablename, result_value):
    msg = "Function: P (feature_value_∩_"+result_value
    print_title(msg) 

    len_data= len(data)
    p_feats_inter_res = dict()
    
    for column_name in data:
        unique_column_values=uniq_ordered_feats(database, tablename, column_name)
        p_feat_inter_res=dict()
        for column_value in unique_column_values:        
            # calculate for conditional probabilities - YES
            facts_per_res=facts_per_result(database, tablename, category=column_name, cat_value=column_value[0], result_value = result_value)
            p_value_inter_res = P(len(facts_per_res), len_data) # P(value ∩ res )
            # print_var(p_value_inter_yes, "P(value ∩ yes )" )
            key = "p_"+column_value[0]+"_inter_"+result_value
            p_feat_inter_res[key] = p_value_inter_res   
        p_feats_inter_res[column_name] = p_feat_inter_res
    msg = "p(feature_value_∩_"+result_value
    print_dict(p_feats_inter_res, msg)
    return p_feats_inter_res

def p_feat_given_result(database, tablename, p_feats, p_feat_inter_result, result_value):
    msg = "Function: P(feature_value_|_"+result_value   
    print_title(msg) 

    p_feats_given_res = dict()
    for category in p_feats.items():
        # print("category", category[0])
        unique_column_values=uniq_ordered_feats(database, tablename, category[0])

        p_feat_given_res = dict()
        for feature in unique_column_values:
            # print( "feature" , str(feature) )
            key_p_feat_inter_res = "p_"+feature[0]+"_inter_"+result_value 
            # print_var(key_p_feat_inter_res,key_p_feat_inter_res) 
            # print("p_feat_inter_result[category].get(feature)", p_feat_inter_result[ category[0] ].get(key_p_feat_inter_res) )
            p_value_given_res = Pcond(p_feat_inter_result[ category[0] ].get(key_p_feat_inter_res), p_feats['Play_Tennis'].get('p_'+result_value)) # P(value | result )
            key_p = "p_"+feature[0]+"_given_"+result_value
            # print_var(key, "key")
            p_feat_given_res[key_p] = p_value_given_res   
        p_feats_given_res[category[0]] = p_feat_given_res
    msg = "p(feature_value_|_"+result_value
    print_dict(p_feats_given_res, msg)
    return p_feats_given_res

def get_inputs(categories, database, tablename):
    print_title("Function: inputs()") 
    categories.drop('Play_Tennis')
    input_feats=[]

    for category in categories.drop('Play_Tennis'):
        message = "Give me "+category+" value: \n"  
        print(message)
        unique_column_values=uniq_ordered_feats(database, tablename, category)
        print("Valid inputs: ", unique_column_values)
        input_feats.append(input())
    print_var(input_feats, "input_feats given")
    return input_feats   
    
def p_res_given_ev(categories, input_feats, p_feats, p_feats_given_res, res_val):
    print_title("Function: p_res_given_ev()") 
    i = 0
    p_event_given_res = float(1)
    for category in categories.drop('Play_Tennis'):
        p_key = "p_"+input_feats[i]+"_given_"+res_val
        print(p_key," :", p_feats_given_res[category].get(p_key))
        p_feat_given_res = p_feats_given_res[category].get(p_key)             
        p_event_given_res *= p_feat_given_res
        i+=1
    # print("p_event_given_yes :", p_event_given_yes )
    key_p = "p_"+ res_val
    p_res_given_ev = ( p_event_given_res * p_feats['Play_Tennis'].get(key_p) )
    print_var(p_res_given_ev, "p_yes_given_ev" ) 
    return p_res_given_ev


