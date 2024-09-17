from model import model_train, model_load

def main():
    
    ## train the model
    model_train("Data/cs-train")

    ## load the model
    model = model_load()
    
    print("model training complete.")


if __name__ == "__main__":
    print('starts1')
    main()
