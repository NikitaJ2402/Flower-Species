import numpy as np 
import pickle 
import streamlit as st 


#loading the saved model
loaded_model=pickle.load(open("D:\\Programmes\\Python\\Jupyter Notebook\\flower_species.sav",'rb'))



#creating a function for prpediction
def Flower_species(input_data):
    #changing the input data to numpy array
    input_data_as_numpy_array=np.asarray(input_data)

    #reshape the array as we are predicting for one instance
    input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)

    prediction=loaded_model.predict(input_data_reshaped)
    print(prediction)

    if(prediction[0]==1):
        return 'The Species is Iris-setosa'
    elif(prediction[0]==2):
        return 'The Species is Iris-versicolor' 
    else:
        return 'The Species is Iris-virginica'

def main():

    #giving a title
    st.title('Flower Species Prediction Web App')
    st.markdown(":tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

    #getting the input data from the User

    SepalLength=st.text_input('Sepal Length in Decimal Value :')
    SepalWidth=st.text_input('Sepal Width in Decimal Value :')
    PetalLength=st.text_input('Petal Length in Decimal Value :')
    PetalWidth=st.text_input('Petal Width in Decimal Value :')


      #code for prediction
    Species=''

    #creating a button for prediction
    if st.button('Flower Species Prediction Result'):
        Species=Flower_species([SepalLength,SepalWidth,PetalLength,PetalWidth])

    st.success(Species)

if __name__ =='__main__':
    main()