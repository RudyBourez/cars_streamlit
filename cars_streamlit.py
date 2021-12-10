from numpy import mod
import streamlit as st
import pymongo

client = pymongo.MongoClient(**st.secrets["mongo"])
db = client.Kaggle_cars

def get_data():
    return db.Cars_dataset

cars_collection = get_data()


list_constructeur = [make["Make"] for make in cars_collection.find({}, {"Make":1, "_id":0})]
constructeur = [""]
for i in range (len(list_constructeur)):
    if list_constructeur[i] not in constructeur:
        constructeur.append(list_constructeur[i])

with st.sidebar:
    my_constructeur = st.selectbox("Constructeur", constructeur)
    my_model = ""
    if my_constructeur != "":
        model = [""]
        list_model = [model["Model"] for model in cars_collection.find({"Make" : my_constructeur} , {"Model": 1, "_id":0})]
        for i in range (len(list_model)):
            if list_model[i] not in model:
                model.append(list_model[i])
        my_model = st.selectbox("Model", model)
    my_dream_car = st.container()
    my_dream_car.subheader("Ajouter une voiture")
    form = st.form("Add a car", True)
    new_make = form.text_input("Mark")
    new_model = form.text_input("Model")
    new_year = form.number_input("Year", min_value = 0, value = 2000)
    new_engine_hp = form.number_input("Engine HP", min_value = 0, value = 0)
    new_engine_cylinders = form.number_input("Engine Cylinders", min_value = 0, value = 0)
    submit = form.form_submit_button()

if my_model != "":
    my_final_list = [item for item in cars_collection.find({"Model" : my_model}, {"_id":0})]
    for item in my_final_list:
        try:    
            st.write(f'La {item["Make"]} {item["Model"]} de {item["Year"]} a {item["Engine HP"]} chevaux et {item["Engine Cylinders"]} cylindres. Sa consommation sur autoroute est de {round(item["highway L/100km"])}L au 100km et de {round(item["city L/100km"])}L au 100km en ville.')
        except KeyError:
            st.write(f'Cette voiture est une voiture électrique')

if submit:
    if new_make == "" or new_model == "" or new_year == 0 or new_engine_hp == 0 or new_engine_cylinders == 0:
        st.write("Renseignez tous les champs avant d'insérer une voiture")
    else :
        st.write("Votre voiture vient d'être ajouté")
        cars_collection.insert_one({"Make" : new_make, "Model":new_model, "Year": new_year, "Engine HP": new_engine_hp, "Engine Cylinders": new_engine_cylinders})