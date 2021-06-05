import joblib
print("\n\t|-- Salary predictor App --|\n")
#Loading trained model
model = joblib.load('Dataset.pk1')

while(1):
    data = int(input('\tExperience of candidate: '))

    #Prediction
    predicted = model.predict([[data]])

    print(f"\n\n\tFor work experience of {data} ,your salary will be : {predicted}")
    ch = input("\n\tDo you want to continue (Y|N):")
    ch = ch.capitalize()
    if ch != 'Y':
        print("\n\tExiting the program .........")
        exit()




