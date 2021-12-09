import streamlit as st
import pymongo

client = pymongo.MongoClient(**st.secrets["mongo"])
db = client.Kaggle_cars

def get_data():
    return db.Cars_dataset

cars_collection = get_data()


list_constructeur = [make["Make"] for make in cars_collection.find({}, {"Make":1, "_id":0})]
constructeur = []
for i in range (len(list_constructeur)):
    if list_constructeur[i] not in constructeur:
        constructeur.append(list_constructeur[i])

with st.sidebar:
     constructeur = st.selectbox("Constructeur", constructeur)
