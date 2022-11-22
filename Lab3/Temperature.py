class temperature:
   
	__slots__ = ('__temp', '__temp_fahr')
        
	def __init__(self, temp = 0):
		self.__temp = temp
		self.__temp_fahr = (9/5) * self.__temp + 32  
				
	def __add__(self, ile_stopni):
		return temperature(self.__temp + ile_stopni)
	    
	def __iadd__(self, ile_stopni):
		self.__temp += ile_stopni
		self.__temp_fahr = (9/5) * self.__temp + 32 
		return self
		
	def __str__(self):
		return "{0}C\n{1}F".format(self.__temp, self.__temp_fahr)
		
	def __radd__(self, ile_stopni):
		return temperature(self.__temp + ile_stopni)
		
	@property
	def temp(self):
		return self.__temp
		
	@property
	def temp_fahr(self):
		return self.__temp_fahr
		
	@temp.setter
	def temp(self, other):
		self.__temp = other
		
	@temp_fahr.setter
	def temp_fahr(self, other):
		self.__temp_fahr = other
		self.__temp_fahr = (9/5) * self.__temp + 32 
    
