from rasa_core.channels.slack import SlackInput
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
import yaml
from rasa_core.utils import EndpointConfig
from rasa_core.interpreter import RegexInterpreter

#load your agent

nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/chatbotnlu')
action_endpoint = EndpointConfig(url="http://localhost:5055/webhook")
agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter,action_endpoint = action_endpoint)


input_channel = SlackInput(
        slack_token="xoxb-540012694912-606987517429-eUfhgwS5BnVGa6eLiTYQN6vw")
	
	
s=agent.handle_channels([input_channel], 5004, serve_forever=True)	
