# -*- coding: utf-8 -*-
"""
Created on Mon May 15 11:28:11 2023

@author: Akshays
"""

import pandas as pd
import streamlit as st




#gfv = pd.read_excel('Grandiose F&V (Updated).xlsx')
#gh = pd.read_excel('Grandiose HouseHold.xlsx')
#sfv = pd.read_excel('Spinneys_Fruits_&_Vegetables_Updated.xlsx')
#sh = pd.read_excel('Spinneys_Household_Updated.xlsx')

data = pd.read_excel('Clean Data(F&V).xlsx',sheet_name='Sheet2')

st.image('grandiose_1.png',use_column_width=True)

rad3 = st.sidebar.radio('**Navigation**',['Select an option','Price Parity','Product Mix','Contact us'])

if rad3=='Select an option':
    pass

if rad3=='Price Parity':

    st.header('PRICE PARITY')
    
    
    company1 = st.selectbox('**PRODUCTS**', ['Select an option','Fruits and Vegetables','Household'])
    if(company1=='Fruits and Vegetables'):
        c1 = st.selectbox('Sub-Category',['Select an option','Fruits','Vegetables','Organic'])
    if(company1=='Household'):
        c2 = st.selectbox('Sub-Category',['Laundry Supplies', 'Disinfectants', 'Dishwashing',
       'Carpet & Floor', 'Glass & Surface', 'Bathroom & Kitchen',
       'Cleaning Tools', 'Garbage Bags & Bins', 'Air Fresheners',
       'Containers & Storage', 'Foil & Cling Films',
       'Facial & Pocket Tissues', 'Kitchen & Toilet Rolls',
       'Insect & Pest Control', 'Shoes Care', 'Disposable Cutlery',
       'Batteries', 'Wires & Plugs', 'Light Bulbs',
       'Lighters, Matches & Candles', 'Outdoor & Garden',
       'Cookware, Bakeware & Utensils', 'Tableware',
       'Tumblers, Tea & Coffee Pots'])
        
    rad = st.radio('',['Select an option','Grandiose','Spinneys','Price Parity'])
    
    if rad == 'Grandiose':
        st.subheader('Grandiose')
        df = data[data['Sub_category']==c1][['Sub_category','Product Name','Quantity','Grandiose_Price']]
        st.dataframe(df)
    if rad == 'Spinneys':
        st.subheader('Spinneys')
        df = data[data['Sub_category']==c1][['Sub_category','Product Name','Quantity','Spinneys_Price']]
        st.dataframe(df)
    if rad == 'Price Parity':
        st.subheader('Price Parity')
        df = data[data['Sub_category']==c1][['Sub_category','Product Name','Quantity','Grandiose_Price','Spinneys_Price']]
        st.dataframe(df)
        
if rad3=='Product Mix':

    st.header('PRODUCT MIX')
    
    rad2 = st.radio('**Select the Location**',['Oud Metha'])
    
    
    company2 = st.selectbox('**PRODUCTS**', ['Select an option','Fruits and Vegetables','Household'])
    if(company2=='Fruits and Vegetables'):
        c3 = st.selectbox('Sub-Category',['Select an option','Fruits','Vegetables','Organic'])

        
        
    if(company2=='Household'):
        c4 = st.selectbox('Sub-Category',['Laundry Supplies', 'Disinfectants', 'Dishwashing',
       'Carpet & Floor', 'Glass & Surface', 'Bathroom & Kitchen',
       'Cleaning Tools', 'Garbage Bags & Bins', 'Air Fresheners',
       'Containers & Storage', 'Foil & Cling Films',
       'Facial & Pocket Tissues', 'Kitchen & Toilet Rolls',
       'Insect & Pest Control', 'Shoes Care', 'Disposable Cutlery',
       'Batteries', 'Wires & Plugs', 'Light Bulbs',
       'Lighters, Matches & Candles', 'Outdoor & Garden',
       'Cookware, Bakeware & Utensils', 'Tableware',
       'Tumblers, Tea & Coffee Pots'])
        
    rad1 = st.radio('',['Select an option','Grandiose','Not in Grandiose'])
        
    if rad1 == 'Grandiose':
        df = pd.read_excel('try1.xlsx',sheet_name=c3,header=None)
        df = df.fillna("")
        st.write(df.to_html(index=False, header=False, escape=False),unsafe_allow_html=True)
        
    if rad1 == 'Not in Grandiose':
        pass
        


import webbrowser

url = 'https://www.grandiose.ae/contact/'

if rad3 =='Contact us':
    webbrowser.open_new_tab(url)
    
    
        
        
        
        
