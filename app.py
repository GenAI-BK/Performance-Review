from fastapi import FastAPI,Request, Response
from dataBase import data_text_overall,data_text_Coworker,data_text_Manager,data_text_Self,data_text_Subordinate,data_text_overall_count,data_text_Subordinate_count,data_text_Self_count,data_text_Coworker_count,data_text_Manager_count
from llm_model import llm_data
import uvicorn
from pydantic import BaseModel
import re
 
 

class OutputData(BaseModel):
    Employee_name:str
    Count_Reviews:dict
    Insights:str
 
def get_data(Employee_name,review_type,start_year,end_year,sorted_value_list):
    
   
    
    if(review_type=="Overall"):
        text=data_text_overall(Employee_name,start_year,end_year)
        Count_Reviews=data_text_overall_count(Employee_name,start_year,end_year)
    elif(review_type=="Manager_Reviews"):
        text=data_text_Manager(Employee_name,start_year,end_year)
        Count_Reviews=data_text_Manager_count(Employee_name,start_year,end_year)
    elif(review_type=="Coworker_Reviews"):
        text=data_text_Coworker(Employee_name,start_year,end_year)
        Count_Reviews=data_text_Coworker_count(Employee_name,start_year,end_year)
       
    elif(review_type=="Subordinate_Reviews"):
        text=data_text_Subordinate(Employee_name,start_year,end_year)
        Count_Reviews=data_text_Subordinate_count(Employee_name,start_year,end_year)
       
    elif(review_type=="Self_Reviews"):
        text=data_text_Self(Employee_name,start_year,end_year)
        Count_Reviews=data_text_Self_count(Employee_name,start_year,end_year)
    total = sum(val if isinstance(val, int) else sum(val) for val in Count_Reviews.values())
    summary=llm_data(sorted_value_list,text,Employee_name,total)
    
    
    insight="\n\n"
    insight+=summary

        
    Insights=OutputData(Employee_name=Employee_name,Count_Reviews=Count_Reviews,Insights=insight)
    return Insights