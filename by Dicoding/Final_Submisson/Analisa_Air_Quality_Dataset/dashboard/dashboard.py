import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st
sns.set(style = "dark")
def create_temp_mean_all_df (df):
    temp_mean_all_df = df.resample(rule='M',on='date').agg({
    "TEMP":"mean"
    }).reset_index()
    temp_mean_all_df.rename (columns = {
        "TEMP" : "temperatur"
    }, inplace = True)
    return temp_mean_all_df

def create_pm25_all_df (df):
    pm25_df = df.groupby(by="station").agg({
    "PM2.5":  "mean"
    }).sort_values(by="PM2.5",ascending=False).reset_index()
    pm25_df.rename(columns ={
        "PM2.5": "pm2.5"
    }, inplace = True)
    return pm25_df

def create_pm10_all_df (df):
    pm10_df = df.groupby(by="station").agg({
    "PM10":  "mean"
    }).sort_values(by="PM10",ascending=False).reset_index()
    pm10_df.rename(columns ={
        "PM10": "pm10"
    }, inplace = True)
    return pm10_df

all_df = pd.read_csv('dashboard/main_data.csv')
all_df.sort_values(by="date", inplace=True)
all_df.reset_index(inplace=True)
all_df["date"] = pd.to_datetime(all_df["date"])
all_df.drop("Unnamed: 0",axis = 1,inplace=True)
# temp_mean_all_df = create_temp_mean_all_df(all_df)
# pm25_all_df = create_pm25_all_df(all_df)
# pm10_all_df = create_pm10_all_df(all_df)

max_date = all_df["date"].max()
min_date = all_df["date"].min()
with st.sidebar:
    st.image('dashboard/th.jpg')
    start_date, end_date = st.date_input(
        label='Rentang Waktu',min_value=min_date,
        max_value=max_date,
        value=[min_date,max_date]
    )

main_df = all_df[(all_df["date"] >= str(start_date)) & (all_df["date"] <= str(end_date))]
temp_mean_df = create_temp_mean_all_df(main_df)
pm25_df = create_pm25_all_df(main_df)
pm10_df = create_pm10_all_df(main_df)
st.header("Analisa Air Quality Dataset")

st.subheader("Suhu rata - rata semua wilayah")
col1,col2 = st.columns(2)
with col1:
    max_temp = temp_mean_df['temperatur'].max()
    st.metric(label = "Temperatur max: ",value= str(max_temp.round(2)) + ' C')
with col2:
    min_temp = temp_mean_df['temperatur'].min()
    st.metric(label = "Temperatur min: ",value= str(min_temp.round(2)) + ' C')
fig, ax = plt.subplots(figsize = (35,15))
ax.plot(
    temp_mean_df["date"],
    temp_mean_df["temperatur"],
    marker = 'o',
    linewidth = 2,
    color = '#90CAF9'
)
ax.tick_params(axis = 'y',labelsize= 20)
ax.tick_params(axis ='x',labelsize = 15)
st.pyplot(fig)

st.subheader("Tingkat polusi pm 2.5 pada semua wilayah")
fig, ax = plt.subplots(nrows=1,ncols=2,figsize = (35,15))
colors = ["#90CAF9", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]
sns.barplot(data=pm25_df.head(5),x="pm2.5",y="station",palette=colors,ax=ax[0])
ax[0].set_ylabel(None)
ax[0].set_xlabel("Jumlah polusi pm 2.5",fontsize = 35)
ax[0].set_title("wilayah dengan polusi pm 2.5 terbanyak",loc = "center",fontsize = 50)
ax[0].tick_params(axis = "x", labelsize = 35) 
ax[0].tick_params(axis = "y", labelsize = 35) 
sns.barplot(data=pm25_df.sort_values(by = "pm2.5", ascending = True).head(5),x="pm2.5",y="station",palette=colors,ax=ax[1])
ax[1].set_ylabel(None)
ax[1].set_xlabel("Jumlah polusi pm 2.5",fontsize = 35)
ax[1].set_title("wilayah dengan polusi pm 2.5 tersedikit",loc = "center",fontsize = 50)
ax[1].invert_xaxis()
ax[1].yaxis.set_label_position("right")
ax[1].yaxis.tick_right()
ax[1].tick_params(axis = "x", labelsize = 35) 
ax[1].tick_params(axis = "y", labelsize = 35) 
st.pyplot(fig)

st.subheader("Tingkat polusi pm 10 pada semua wilayah")
fig, ax = plt.subplots(nrows=1,ncols=2,figsize = (35,15))
colors = ["#90CAF9", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]
sns.barplot(data=pm10_df.head(5),x="pm10",y="station",palette=colors,ax=ax[0])
ax[0].set_ylabel(None)
ax[0].set_xlabel("Jumlah polusi pm 10",fontsize = 35)
ax[0].set_title("wilayah dengan polusi pm 10 terbanyak",loc = "center",fontsize = 50)
ax[0].tick_params(axis = "x", labelsize = 35) 
ax[0].tick_params(axis = "y", labelsize = 35) 
sns.barplot(data=pm10_df.sort_values(by = "pm10", ascending = True).head(5),x="pm10",y="station",palette=colors,ax=ax[1])
ax[1].set_ylabel(None)
ax[1].set_xlabel("Jumlah polusi pm 10",fontsize = 35)
ax[1].set_title("wilayah dengan polusi pm 10 tersedikit",loc = "center",fontsize = 50)
ax[1].invert_xaxis()
ax[1].yaxis.set_label_position("right")
ax[1].yaxis.tick_right()
ax[1].tick_params(axis = "x", labelsize = 35) 
ax[1].tick_params(axis = "y", labelsize = 35) 
st.pyplot(fig)
