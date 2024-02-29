# # from dataBase import data_text_overall,data_text_Coworker,data_text_Manager,data_text_Self,data_text_Subordinate 
# # from langchain.llms.openai import OpenAI
# # # from openai import OpenAI
# # from langchain.prompts import PromptTemplate
# # from langchain.chains import LLMChain, LLMMathChain, TransformChain, SequentialChain
# # from langchain.callbacks import get_openai_callback
# # import os
# # import inspect
# # import re

# # os.environ["OPENAI_API_KEY"]="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"
# # # employee_name="Shelly Sharma"

# # # text=data_text_Coworker(employee_name,"2023","2023")
# # # if text==None:
# # #     text=""
    
# # # print(text)

# # def llm_data(text,employee_name):
# #     if(text==""):
# #         insights="Data not found"
# #         print(insights)
# #         return insights
# #     else:
# #         llm=OpenAI(temperature=0)
# #         insights=""
# #         prompt1="""
# #             There is a data {text} of employee performance reviews in format of:
# #             which contains columns as
# #             Reviewer Name, Reviewee Name, Date and
# #             After that, there are some reviews on the basis of different questions for which the reviewers gives feedback to the reviewee.
# #             1. On the basis of this data, generate a concise summary, within 100 words, of feedbacks provided to the {employee_name}
# #             2. Write 4 strengths and 4 weaknesses of {employee_name}
# #             3. Analyze the performance of a specific employee {employee_name} and identify areas for improvement.Only provide areas of imrovement in 3 or 4  points.

# #             On the basis of these 3 insights generate an answer in 3 points that should not exceed the word limit of 25 words per point and can also satisfy all the three insights.
# #         """
# #         prompt_template1=PromptTemplate(
# #             input_variables=["text","employee_name"],
# #             template=prompt1 
# #         )
# #         chain1=LLMChain(llm=llm,prompt=prompt_template1)
# #         insights+=chain1.run({"text":text,"employee_name":employee_name})
        
# #         prompt2="""
# #             There is a data {text} of employee performance reviews in format of:
# #             which contains columns as
# #             Reviewer Name, Reviewee Name, Date and there are some reviews on the basis of different questions for which the reviewers gives feedback to the reviewee.

# #             4. Find the sentiment of feedbacks of {employee_name} in one word.
# #             5. These are the 4 Core Values:
# #             Team Oriented:
# #             Definition: Collaborating effectively with colleagues to achieve common goals.
# #             Trust & Respect:
# #             Definition: Building and maintaining trustful and respectful relationships within the team.
# #             Focused:
# #             Definition: Maintaining concentration and attention to detail in tasks.
# #             Passionate:
# #             Definition: Showing strong enthusiasm and dedication in the assigned responsibilities.
# #             Analyze the reviews of {employee_name}  based on the core values of Team Oriented, Trust & Respect, Focused, and Passionate. Provide a one-word assessment of whether the employee follows each core value or not.
           
# #             On the basis of these 2 insights generate  answer in 2 points that should not exceed the word limit of 35 words per point and can also satisfy all the two insights.
# #             Make sure to number the points as 4 and 5  not 1 and 2 .
# #         """
# #         insights+="\n"
# #         prompt_template2=PromptTemplate(
# #             input_variables=["text","employee_name"],
# #             template=prompt2 
# #         )
# #         chain2=LLMChain(llm=llm,prompt=prompt_template2)
# #         insights+=chain2.run({"text":text,"employee_name":employee_name})
# #         # print(insights)
# #         return insights
        

# # # llm_data(text,employee_name)

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

 

def llm_data(value_list,text,Employee_Name):
   
    if text =="":
        insights="Data not Found"
        # print(insights)
        return insights
    else:
        inputs = {
        "Area of improvement": " Analyze the performance of a specific employee {Employee_Name} and identify areas for improvement in 4 or 5 points.Only provide areas of imrovement  points.  ",
        "Strength and Weakness": " Write 4 strengths and 4 weaknesses of {Employee_Name} in heading points only. If there are no strengths or weaknesses then write 'There are no Strengths worth mentioning' or 'There are no Weaknesses worth mentioning' respectively.",
        "Sentiment": "Process Sentiment Analysis by classifying each review as positive, negative, or neutral. After analyzing each review, provide counts for each classification. For example, 'Positive Review':3 'Negative Review':2 'Neutral Review':6.Don't Add any Description",
        
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
        
        llm = ChatGoogleGenerativeAI(model="gemini-pro")
       
        insights=""
        prompt_template1=PromptTemplate(
            input_variables=["text","Employee_Name"],
            template=final_prompt
        )
        chain=LLMChain(llm=llm,prompt=prompt_template1)
        insights+=chain.run({"text":text,"Employee_Name":Employee_Name})
        # print(insights)
        return insights
       
# llm_data(value_list,text,Employee_Name)