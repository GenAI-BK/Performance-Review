
import app
import streamlit as st

from datetime import datetime






 
 
 
# Define the Streamlit app

def main():
    st.title("Employee Review App")
     # Input field for the employee's name
    Employee_name = st.text_input("Enter employee's name:")
   
    # Dropdown menu for selecting review type
    review_type = st.selectbox("Select review type", ["Overall", "Manager_Reviews", "Coworker_Reviews", "Subordinate_Reviews", "Self_Reviews"])
   
   
    # Dynamically generate range for selecting start year and end year
    current_year = datetime.now().year
    start_year_range = [str(year) for year in range(current_year - 6, current_year+1 )]
    end_year_range = [str(year) for year in range(current_year - 6, current_year+1 )]
    
    # Dropdown columns for selecting start date and end date
    start_year = st.selectbox("Start Year", start_year_range)
    end_year = st.selectbox("End Year", end_year_range)
    
    # Checkbox list for selecting additional options
    selected_options  = st.multiselect("Select additional options", ["Area of improvement", "Sentiment", "Strength and Weakness","Employee Performance Matrix"])
    prompt_list = list(selected_options)
    Ordered_list= ["Strength and Weakness", "Area of improvement", "Sentiment", "Employee Performance Matrix"]
    sorted_value_list = sorted(prompt_list, key=lambda x: (Ordered_list.index(x) if x in Ordered_list else float('inf')))

 
    if st.button("Run"):
        if Employee_name:
            if start_year <= end_year:
                # Perform some action here
                st.success(f"Processing data for employee: {Employee_name} from {start_year} to {end_year}")
               
                
                response = app.get_data(Employee_name,review_type,start_year,end_year,sorted_value_list)
               
                # Display the response
                if response != None:
                    
                    display_response(response)
                else:
                    st.error(f"Failed to retrieve data. Status code: {response.status_code}")
            else:
                st.error("End year must be greater than or equal to start year.")
        else:
            st.warning("Please enter an employee's name.")
 
# Function to display the response
def display_response(response):
    st.subheader("Employee Review Insights")
    
    # Accessing individual attributes of the OutputData object
    st.write(f"- Employee Name: {response.Employee_name}")
    st.write("- Count Reviews:")
    
    # Iterating over key-value pairs in the Count_Reviews dictionary
    for key, value in response.Count_Reviews.items():
        st.write(f"  - {key}: {value}")
    
    st.write(f"- Insights: {response.Insights}")
if __name__ == "__main__":
    main()