
import unittests
from model import *

SAVED_MODEL="Models/modelfile.joblib"
class ModelTest(unittests.TestCase):

    def test_01_train(self):

        model_train("Data/cs-train")
        self.assertTrue(os.path.exists(SAVED_MODEL))

    def test_02_load(self):

        model = model_load()
        self.assertTrue('predict' in dir(model))
        self.assertTrue('fit' in dir(model))

    def test_03_Predict(self):
        model = model_load()

        result = model_predict("all","2018","5","15", model)
        y_pred = result['y_pred']
        self.assertTrue(y_pred[0] is not None)


### Run the tests
if __name__ == '__main__':
    unittests.main()
