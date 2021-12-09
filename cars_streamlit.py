import streamlit as st
import pymongo

client = pymongo.MongoClient(**st.secrets["mongo"])
db = client.Kaggle_cars

def get_data():
    cars_collection = db.Cars_dataset
    cars = [car for car in cars_collection.find()]
    return cars

cars = get_data()

st.write(cars)
