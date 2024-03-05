from dataBase import data_text_overall,data_text_Coworker,data_text_Manager,data_text_Self,data_text_Subordinate
from langchain.llms.openai import OpenAI
# from openai import OpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, LLMMathChain, TransformChain, SequentialChain
from langchain.callbacks import get_openai_callback
import os
import streamlit as st
 
import inspect
import re
os.environ["GOOGLE_API_KEY"]=st.secrets["GOOGLE_API_KEY"]

 

def llm_data(value_list,text,Employee_Name,total):
   
    if text =="":
        insights="Data not Found"
        # print(insights)
        return insights
    else:
        inputs = {
        "Area of improvement": " Analyze the performance of a specific employee {Employee_Name} and identify areas for improvement in 4 or 5 points.Only provide areas of imrovement  points.  ",
        "Strength and Weakness": " Write 4 strengths and 4 weaknesses of {Employee_Name} in heading points only. If there are no strengths or weaknesses then write 'There are no Strengths worth mentioning' or 'There are no Weaknesses worth mentioning' respectively.",
        "Sentiment": "Given a list of reviews enclosed within parentheses `( )`, Although each set of parentheses contains multiple individual questions, treat each set as a single review for processing. Classify each review into positive, negative, and neutral categories.Finally, provide the count for each category and ensure the total sum of count of all the categories DOES NOT EXCEED {total}.If there is no review for any categorie just write 0",
                       
        
        "Employee Performance Matrix":"Provide information for each heading in about 30 words , based on {Employee_Name}'s performance data:"
                                        "'Work Efficiency:' Rate of task completion."
                                        "'Teamwork': Collaborative efforts with colleagues."
                                        "'Learning Ability': Capacity for acquiring new skills"
                                        "'Quality of Work': Standard of output."
                                        "'Adherence to Timelines': Consistency in meeting deadlines."
                                    
                                        
        }
        final_prompt = """There is a data {text} of employee performance reviews in format which contains 
            some reviews on the basis of different questions for which the reviewers gives feedback to the reviewee.on the basis of this question answer data you need to answer the following points:
            
           """
        i=1
        for value in value_list:
            
                final_prompt+=str(i)
                final_prompt += inputs.get(value, "")
                i+=1
                final_prompt+="\n"
        final_prompt+="""Write the heading for each point and then write the answer for point for that point. Don't use asterisk intstead use a bold point to start the point.MAKE SURE TO NUMBER THE POINT and give a STRUCTURED response
        
             
             """
        # # print(final_prompt)
        # llm=OpenAI(temperature=0)
        
        llm = ChatGoogleGenerativeAI(model="gemini-pro",temperature=0)
       
        insights=""
        prompt_template1=PromptTemplate(
            input_variables=["text","Employee_Name"],
            template=final_prompt
        )
        chain=LLMChain(llm=llm,prompt=prompt_template1)
        insights+=chain.run({"text":text,"Employee_Name":Employee_Name,"total":total})
        # print(insights)
        return insights
       
# llm_data(value_list,text,Employee_Name)