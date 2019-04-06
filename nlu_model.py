from rasa_nlu.training_data import load_data
from rasa_nlu import config
from rasa_nlu.model import Trainer
from rasa_nlu.model import Interpreter, Metadata
def train_nlu(data,configuration,model_dir):
	training_data=load_data(data)
	trainer=Trainer(config.load(configuration))
	trainer.train(training_data)
	model_directory=trainer.persist(model_dir,fixed_model_name='chatbotnlu')

def run_nlu():
	interpreter=Interpreter.load('./models/nlu/default/chatbotnlu')
	print(interpreter.parse(u"tell me something about you"))

if __name__ =='__main__':
	#train_nlu('./data/data.json','config_spacy.json','./models/nlu')
	run_nlu()

