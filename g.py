
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

st.image('gsc.png',use_column_width=True)

rad3 = st.sidebar.radio('**Navigation**',['Select an option','Price Parity','Product Mix'])

if rad3=='Select an option':
    pass

if rad3=='Price Parity':

    
    
    comp=st.radio('',['Select an option','Grandiose Products','Spinneys Products'])
    if(comp=='Grandiose Products'):
        d1=pd.concat([gfv,ghh],ignore_index=True)
        d2=pd.concat([d1,gf],ignore_index=True)
        d3=pd.concat([d2,gb],ignore_index=True)
        d3=gfv[['Sub_category','Product Name','Quantity','Price']]
        
        st.dataframe(d3)
        
        excel_button = st.button('Download as Excel')
        if excel_button:
            writer = pd.ExcelWriter('data.xlsx', engine='openpyxl')
            d3.to_excel(writer, sheet_name='Sheet1', index=False)
            writer.close()
            with open('data.xlsx', 'rb') as f:
                excel_data = f.read()
                st.download_button(label='Click here to download', data=excel_data, file_name='data.xlsx', mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    if(comp=='Spinneys Products'):
        d4=pd.concat([sfv,shh],ignore_index=True)
        d5=pd.concat([d4,sf],ignore_index=True)
        d6=pd.concat([d5,sb],ignore_index=True)
        d6=gfv[['Sub_category','Product Name','Quantity','Price']]
        
        st.dataframe(d6)
        
        excel_button = st.button('Download as Excel')
        if excel_button:
            writer = pd.ExcelWriter('data.xlsx', engine='openpyxl')
            d6.to_excel(writer, sheet_name='Sheet1', index=False)
            writer.close()
            with open('data.xlsx', 'rb') as f:
                excel_data = f.read()
                st.download_button(label='Click here to download', data=excel_data, file_name='data.xlsx', mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        
    st.subheader('Price Parity')       
    cat = st.selectbox('**PRODUCTS**', ['Select an option','Fruits and Vegetables','Household','Frozen Food','Beverages'])
    if(cat=='Fruits and Vegetables'):
        sb1 = st.selectbox('Sub-Category',['Select an option','Fruits','Vegetables'])
        
        
        st.subheader('Price Parity')
        df = cfv[cfv['Sub_category']==sb1][['Sub_category','Product Name','Quantity','Grandiose_Price','Spinneys_Price']]
        st.dataframe(df)
        
        
    if(cat=='Household'):
        sb2 = st.selectbox('Sub-Category',['Select an option','Laundry Supplies', 'Carpet & Floor', 'Disinfectants',
       'Bathroom & Kitchen', 'Insect & Pest Control','Foil & Cling Films', 'Cleaning Tools', 'Dishwashing',
       'Air Fresheners', 'Kitchen & Toilet Rolls', 'Containers & Storage','Lighters, Matches & Candles', 'Glass & Surface', 'Shoes Care'])
        
       
        st.subheader('Price Parity')
        df = chh[chh['Sub_category']==sb2][['Sub_category','Product Name','Quantity','Grandiose_Price','Spinneys_Price']]
        st.dataframe(df)
            
    if(cat=='Frozen Food'):
        sb3 = st.selectbox('Sub-Category',['Select an option','Fruits & Vegetables', 'Chicken & Turkey', 'Fish & Seafood',
       'Breaded & Fries', 'Burgers, Meatballs & Sausage','Appetizers & Snacks', 'Pastries', 'Ice Cream','French Fries & Chips', 'Meat', 'Ready Meals','Vegan & Alternatives'])
        
        
        st.subheader('Price Parity')
        df = cf[cf['Sub_category']==sb3][['Sub_category','Product Name','Quantity','Grandiose_Price','Spinneys_Price']]
        st.dataframe(df)
            
    if(cat=='Beverages'):
        sb4 = st.selectbox('Sub-Category',['Select an option','Still Water', 'Sparkling Water', 'Soft Drinks', 'Juices',
       'Healthy Drinks', 'Fresh Juices', 'Energy Drinks','Ice Tea & Coffee', 'Malt Drinks'])
        
        
        st.subheader('Price Parity')
        df = cb[cb['Sub_category']==sb4][['Sub_category','Product Name','Quantity','Grandiose_Price','Spinneys_Price']]
        st.dataframe(df)
        
    
    
    
        
if rad3=='Product Mix':

    st.header('PRODUCT MIX')
    
    rad2 = st.radio('**Select the Location**',['Oud Metha'])
    
    
    company2 = st.selectbox('**PRODUCTS**', ['Select an option','Fruits and Vegetables'])
    if(company2=='Fruits and Vegetables'):
        c3 = st.selectbox('Sub-Category',['Select an option','Fruits','Vegetables'])

        
        
   
        
    rad1 = st.radio('',['Select an option','Grandiose','Not in Grandiose'])
        
    if rad1 == 'Grandiose':
        df = pd.read_excel('try1.xlsx',sheet_name=c3,header=None)
        df = df.fillna("")
        st.write(df.to_html(index=False, header=False, escape=False),unsafe_allow_html=True)
        
    if rad1 == 'Not in Grandiose':
        dn=pd.read_excel('Not_in_Grandiose.xlsx')
        dn=dn[['Sub_Category','Product_name','Quantity','Price']]
        if(c3=='Fruits'):
            dn1=dn[dn['Sub_Category']=='Fruit']
            st.dataframe(dn1)
        if(c3=='Vegetables'):
            dn1=dn[dn['Sub_Category']==c3]
            st.dataframe(dn1)
        
        
    
    
        
        
        
        
