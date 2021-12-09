import streamlit as st
import pymongo

client = pymongo.MongoClient("mongodb+srv://Rudy_datascience:Cr21042014.@cluster0.mlwpv.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.Kaggle_cars

@st.cache
def get_data():
    cars_collection = db.Cars_dataset
    cars = [car for car in cars_collection.find()]
    return cars

cars = get_data()

st.write(cars)
