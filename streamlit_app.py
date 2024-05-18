# streamlit_app.py
import pandas as pd

# Load your dataset
data = pd.read_csv('/Users/fhariyaaseem/Downloads/fashion_products.csv')
def recommend_products(product_id, num_recommendations):
    # This is a placeholder function, implement your recommendation logic here
    # For now, it just returns num_recommendations random samples from the dataset
    return data.sample(n=num_recommendations)


import streamlit as st
st.title('Fashion Products Recommendations')


# Input for Product Name
product_name = st.text_input('Enter Product Name')

# Button to trigger the rating display
if st.button('Show Rating'):
    # Filter the data for the input product name
    product_data = data[data['Product Name'].str.contains(product_name, case=False, na=False)]
    if not product_data.empty:
        st.write('Ratings for:', product_name)
        # Display the ratings (assuming 'Rating' columns exist)
        for index, row in product_data.iterrows():
            # Safely accessing the elements using .loc
            product_id = row['Product ID']
            rating = row['Rating']
            brand = row['Brand']
            st.write('Product ID:', product_id, 'Rating:', rating,'Brand:' , brand)
    else:
        st.write('No product found with that name.')
