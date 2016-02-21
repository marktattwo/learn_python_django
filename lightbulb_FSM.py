from random import randint
from time import clock

#################################################

State = type("State", (object,), {})

class LightOn(State):
	def Enter(self):
		print "Spark"

	def Execute(self):
		print "On"

	def Exit(self):
		pass

class LightOff(State):
	def Enter(self):
		pass

	def Execute(self):
		print "Off"

	def Exit(self):
		print "Blink Blink"

#################################################

class Transition(object):
	def __init__(self, toState):
		self.toState = toState

	def Execute(self):
		print 'Transitioning...'

#################################################

class SimpleFSM(object):
	def __init__(self, char):
		self.char = char
		self.states = {}
		self.transitions = {}
		self.curState = None
		self.prevState = None #prevent unfinite loop
		self.trans = None

	def AddTransition(self, transName, transition):
		self.transitions[transName] = transition

	def AddState(self, stateName, state):
		self.states[stateName] = state

	def SetState(self, stateName):
		self.curState = self.states[stateName]

	def Transition(self, transName):
		self.trans = self.transitions[transName]

	def Execute(self):
		if(self.trans):
			self.curState.Exit()
			self.trans.Execute()
			self.SetState(self.trans.toState)
			self.curState.Enter()
			self.trans = None
		self.curState.Execute()

#################################################

class Char(object):
	def __init__(self):
		pass

#################################################
class LightBulb(Char):
	def __init__(self):
		self.FSM = SimpleFSM(self)

		# State
		self.FSM.AddState("On",LightOn())
		self.FSM.AddState("Off",LightOff())

		#transition
		self.FSM.AddTransition("toOn", Transition("On"))
		self.FSM.AddTransition("toOff", Transition("Off"))

		#Current
		self.LightOn = True
		self.FSM.SetState("On")



if __name__ == "__main__":
	light = LightBulb()

	for i in xrange(20):
		startTime = clock()
		timeInterval = 1
		while(startTime + timeInterval > clock()):
			pass
		if(randint(0,2)):
			if(light.LightOn):
				light.FSM.Transition("toOff")
				light.LightOn = False
			else:
				light.FSM.Transition("toOn")
				light.LightOn = True
		light.FSM.Execute()
