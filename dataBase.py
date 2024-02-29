import sqlite3
sql_connect = sqlite3.connect('Employee_Review.db',check_same_thread=False)
cursor = sql_connect.cursor()

# Execute each query and fetch the results for overall data
# def data_text_overall(employee_name,start_date,end_date):
#     queries = [
#         f"SELECT * FROM Coworker_Reviews WHERE Reviewee_Name = ? AND Date BETWEEN ? AND ?;",
#         f"SELECT * FROM Self_Reviews WHERE Reviewer_Name = ? AND Date BETWEEN ? AND ?;",
#         f"SELECT * FROM Manager_Reviews WHERE Reviewee_Name = ? AND Date BETWEEN ? AND ?;",
#         f"SELECT * FROM Subordinate_Reviews WHERE Reviewee_Name = ? AND Date BETWEEN ? AND ?;"
#     ]
#     param=(employee_name,start_date,end_date)
#     # elif start_date:
#     #     queries=[
#     #         f"SELECT * FROM Coworker_Reviews WHERE Reviewee_Name = ? AND Date = ?;",
#     #         f"SELECT * FROM Self_Reviews WHERE Reviewer_Name = ? AND Date = ? ;",
#     #         f"SELECT * FROM Manager_Reviews WHERE Reviewee_Name = ? AND Date = ?;",
#     #         f"SELECT * FROM Subordinate_Reviews WHERE Reviewee_Name = ? AND Date = ?;"
#     #         ]
#     #     param=(employee_name,start_date)
#     text = ""
#     for query in queries:
#         cursor.execute(query, (param))
#         results = cursor.fetchall()
#         # Process the results
#         for row in results:
#             text += str(row)
#     # print(text)
#     return text    
def data_text_overall_count(employee_name, start_date, end_date):
    queries = [
        "SELECT * FROM Coworker_Reviews WHERE Reviewee_Name = ? AND Date BETWEEN ? AND ?;",
        "SELECT * FROM Self_Reviews WHERE Reviewer_Name = ? AND Date BETWEEN ? AND ?;",
        "SELECT * FROM Manager_Reviews WHERE Reviewee_Name = ? AND Date BETWEEN ? AND ?;",
        "SELECT * FROM Subordinate_Reviews WHERE Reviewee_Name = ? AND Date BETWEEN ? AND ?;"
    ]
    param = (employee_name, start_date, end_date)
    
    # Initialize dictionary to store the count of data fetched from each review type
    review_counts = {
        "Coworker_Reviews": [],
        "Self_Reviews": [],
        "Manager_Reviews": [],
        "Subordinate_Reviews": []
    }
    
    for query in queries:
        cursor.execute(query, param)
        results = cursor.fetchall()
        review_type = query.split(" ")[3]  # Extracting the review type from the query
        review_counts[review_type].append(len(results))
    # print(review_counts)
    return review_counts

def data_text_Manager_count(employee_name, start_date, end_date):
    query = f"SELECT * FROM Manager_Reviews WHERE Reviewee_Name = '{employee_name}' AND Date BETWEEN '{start_date}' AND '{end_date}';"
    cursor.execute(query)
    results = cursor.fetchall()
    review_count = len(results)
    # print(review_count)
    return {"Review_Count": review_count}

def data_text_Subordinate_count(employee_name,start_date,end_date):
    # param=(employee_name,start_date,end_date)
    query = f"SELECT * FROM Subordinate_Reviews WHERE Reviewee_Name = '{employee_name}' AND Date BETWEEN '{start_date}' AND '{end_date}';"
    cursor.execute(query)
    results = cursor.fetchall()
    review_count = len(results)
    # print({"Review_Count": review_count})
    return {"Review_Count": review_count}

def data_text_Coworker_count(employee_name,start_date,end_date):
    query = f"SELECT * FROM Coworker_Reviews WHERE Reviewee_Name = '{employee_name}' AND Date BETWEEN '{start_date}' AND '{end_date}';"
    cursor.execute(query)
    results = cursor.fetchall()
    review_count = len(results)
    # print({"Review_Count": review_count})
    return {"Review_Count": review_count}

def data_text_Self_count(employee_name,start_date,end_date):
    query = f"SELECT * FROM Self_Reviews WHERE Reviewer_Name = '{employee_name}' AND Date BETWEEN '{start_date}' AND '{end_date}';"
         
    cursor.execute(query)
    results = cursor.fetchall()
    review_count = len(results)
    # print({"Review_Count": review_count})
    return {"Review_Count": review_count} 








def data_text_overall(employee_name, start_date, end_date):
    queries = [
        "SELECT * FROM Coworker_Reviews WHERE Reviewee_Name = ? AND Date BETWEEN ? AND ?;",
        "SELECT * FROM Self_Reviews WHERE Reviewer_Name = ? AND Date BETWEEN ? AND ?;",
        "SELECT * FROM Manager_Reviews WHERE Reviewee_Name = ? AND Date BETWEEN ? AND ?;",
        "SELECT * FROM Subordinate_Reviews WHERE Reviewee_Name = ? AND Date BETWEEN ? AND ?;"
    ]
    param = (employee_name, start_date, end_date)
    
    # Dictionary to store the count of data fetched from each review type
   
    text = ""
    # Loop through each query and fetch data
    for query in queries:
        cursor.execute(query, param)
        results = cursor.fetchall()
        for row in results:
             text += str(row)
        
       
    
    return text


# Execute each query and fetch the results for manager reviews
def data_text_Manager(employee_name,start_date,end_date):
    query = f"SELECT * FROM Manager_Reviews WHERE Reviewee_Name = '{employee_name}' AND Date BETWEEN '{start_date}' AND '{end_date}';"
    cursor.execute(query)
    text = ""
    results = cursor.fetchall()
    for row in results:
        text += str(row)
    # print(text)  
    return text  

# Execute each query and fetch the results for subordinate reviews
def data_text_Subordinate(employee_name,start_date,end_date):
    # param=(employee_name,start_date,end_date)
    query = f"SELECT * FROM Subordinate_Reviews WHERE Reviewee_Name = '{employee_name}' AND Date BETWEEN '{start_date}' AND '{end_date}';"
    cursor.execute(query)
    text = ""
    results = cursor.fetchall()
    for row in results:
        text += str(row)
    # print(text)
    return text


 
# Execute each query and fetch the results for Coworker reviews
def data_text_Coworker(employee_name,start_date,end_date):
    query = f"SELECT * FROM Coworker_Reviews WHERE Reviewee_Name = '{employee_name}' AND Date BETWEEN '{start_date}' AND '{end_date}';"
    cursor.execute(query)
    text = ""
    results = cursor.fetchall()
    for row in results:
        text += str(row)
    # print(text)  
    return text     

# Execute each query and fetch the results for self reviews
def data_text_Self(employee_name,start_date,end_date):
    queries = [
        f"SELECT * FROM Self_Reviews WHERE Reviewer_Name = '{employee_name}' AND Date BETWEEN '{start_date}' AND '{end_date}';"
        ]
    # Execute each query and fetch the results
    text = ""
    for query in queries:
        cursor.execute(query)
        results = cursor.fetchall()
        # Process the results
        for row in results:
            text += str(row)
    # print(text)
    return text    



# data_text_Self("Misha Shah")    
# name=input()
# # data_text(name)
data_text_Self_count("Misha Shah","2018","2022")    
