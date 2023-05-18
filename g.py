
import pandas as pd
import streamlit as st

#fruits and vegetables
gfv=pd.read_excel('Grandiose F&V (Updated).xlsx')
sfv=pd.read_excel('Spinneys_Fruits_&_Vegetables_Updated.xlsx')
cfv=pd.read_excel('Grandiose Cleaned Data.xlsx',sheet_name='Fruits and Vegs')

#HouseHold
ghh=pd.read_excel('Grandiose HouseHold.xlsx')
shh=pd.read_excel('Spinneys_Household_Updated.xlsx')
chh=pd.read_excel('Grandiose Cleaned Data.xlsx',sheet_name='HouseHold')

#Frozen
gf=pd.read_excel('Grandiose Frozen.xlsx')
sf=pd.read_excel('Spinneys_Frozen.xlsx')
cf=pd.read_excel('Grandiose Cleaned Data.xlsx',sheet_name='Frozen')

#Beverages
gb=pd.read_excel('Grandiose Beverages.xlsx')
sb=pd.read_excel('Spinneys Beverage.xlsx')
cb=pd.read_excel('Grandiose Cleaned Data.xlsx',sheet_name='Beverages')




#data = pd.read_excel('Grandiose Cleaned Data.xlsx',sheet_name='Fruits and Vegs')

st.image('grandiose_building_.png',use_column_width=True)

rad3 = st.sidebar.radio('**Navigation**',['Select an option','Price Parity','Product Mix'])

if rad3=='Select an option':
    pass

if rad3=='Price Parity':

    st.header('PRICE PARITY')
    
    
    cat = st.selectbox('**PRODUCTS**', ['Select an option','Fruits and Vegetables','Household','Frozen Food','Beverages'])
    if(cat=='Fruits and Vegetables'):
        sb1 = st.selectbox('Sub-Category',['Select an option','Fruits','Vegetables'])
        
        rad = st.radio('',['Select an option','Grandiose','Spinneys','Price Parity'])
        
        if rad == 'Grandiose':
            st.subheader('Grandiose')
            df = gfv[gfv['Sub_category']==sb1][['Sub_category','Product Name','Quantity','Price']]
            st.dataframe(df)
        if rad == 'Spinneys':
            st.subheader('Spinneys')
            df = sfv[sfv['Sub_category']==sb1][['Sub_category','Product Name','Quantity','Price']]
            st.dataframe(df)
        if rad == 'Price Parity':
            st.subheader('Price Parity')
            df = cfv[cfv['Sub_category']==sb1][['Sub_category','Product Name','Quantity','Grandiose_Price','Spinneys_Price']]
            st.dataframe(df)
        
        
    if(cat=='Household'):
        sb2 = st.selectbox('Sub-Category',['Select an option','Laundry Supplies', 'Carpet & Floor', 'Disinfectants',
       'Bathroom & Kitchen', 'Insect & Pest Control','Foil & Cling Films', 'Cleaning Tools', 'Dishwashing',
       'Air Fresheners', 'Kitchen & Toilet Rolls', 'Containers & Storage','Lighters, Matches & Candles', 'Glass & Surface', 'Shoes Care'])
        
        rad = st.radio('',['Select an option','Grandiose','Spinneys','Price Parity'])
        
        if rad == 'Grandiose':
            st.subheader('Grandiose')
            df = ghh[ghh['Sub_category']==sb2][['Sub_category','Product Name','Quantity','Price']]
            st.dataframe(df)
        if rad == 'Spinneys':
            st.subheader('Spinneys')
            df = shh[shh['Sub_category']==sb2][['Sub_category','Product Name','Quantity','Price']]
            st.dataframe(df)
        if rad == 'Price Parity':
            st.subheader('Price Parity')
            df = chh[chh['Sub_category']==sb2][['Sub_category','Product Name','Quantity','Grandiose_Price','Spinneys_Price']]
            st.dataframe(df)
            
    if(cat=='Frozen Food'):
        sb3 = st.selectbox('Sub-Category',['Select an option','Fruits & Vegetables', 'Chicken & Turkey', 'Fish & Seafood',
       'Breaded & Fries', 'Burgers, Meatballs & Sausage','Appetizers & Snacks', 'Pastries', 'Ice Cream','French Fries & Chips', 'Meat', 'Ready Meals','Vegan & Alternatives'])
        
        rad = st.radio('',['Select an option','Grandiose','Spinneys','Price Parity'])
        
        if rad == 'Grandiose':
            st.subheader('Grandiose')
            df = gf[gf['Sub_category']==sb3][['Sub_category','Product Name','Quantity','Price']]
            st.dataframe(df)
        if rad == 'Spinneys':
            st.subheader('Spinneys')
            df = sf[sf['Sub_category']==sb3][['Sub_category','Product Name','Quantity','Price']]
            st.dataframe(df)
        if rad == 'Price Parity':
            st.subheader('Price Parity')
            df = cf[cf['Sub_category']==sb3][['Sub_category','Product Name','Quantity','Grandiose_Price','Spinneys_Price']]
            st.dataframe(df)
            
    if(cat=='Beverages'):
        sb4 = st.selectbox('Sub-Category',['Select an option','Still Water', 'Sparkling Water', 'Soft Drinks', 'Juices',
       'Healthy Drinks', 'Fresh Juices', 'Energy Drinks','Ice Tea & Coffee', 'Malt Drinks'])
        
        rad = st.radio('',['Select an option','Grandiose','Spinneys','Price Parity'])
        
        if rad == 'Grandiose':
            st.subheader('Grandiose')
            df = gb[gb['Sub_category']==sb4][['Sub_category','Product Name','Quantity','Price']]
            st.dataframe(df)
        if rad == 'Spinneys':
            st.subheader('Spinneys')
            df = sb[sb['Sub_category']==sb4][['Sub_category','Product Name','Quantity','Price']]
            st.dataframe(df)
        if rad == 'Price Parity':
            st.subheader('Price Parity')
            df = cb[cb['Sub_category']==sb4][['Sub_category','Product Name','Quantity','Grandiose_Price','Spinneys_Price']]
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
        
    
    
        
        
        
        
