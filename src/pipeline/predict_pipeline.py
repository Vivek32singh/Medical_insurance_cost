import sys
import pandas as pd
from src.exception import CustomException
from src.utils import load_object
import os

class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            model_path=os.path.join("artifacts","model.pkl")
            preprocessor_path=os.path.join('artifacts','proprocessor.pkl')
            print("Before Loading")
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            print("After Loading")
            data_scaled=preprocessor.transform(features)
            preds=model.predict(data_scaled)
            return preds
        
        except Exception as e:
            raise CustomException(e,sys)


class CustomData:
    def __init__(  self,
        sex: str,
        children:int,
        region: str,
        smoker: str,
        age: int,
        bmi: int):

        self. sex =  sex

        self.children = children

        self.region = region

        self.smoker = smoker

        self.age = age

        self.bmi = bmi
        


    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "sex": [self.sex],
                "children": [self.children],
                "region": [self.region],
                "smoker": [self.smoker],
                "age": [self.age],
                "bmi": [self.bmi],
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)