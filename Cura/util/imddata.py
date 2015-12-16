from Cura.util import resources
import sqlite_helper

class ImdData(object):
	'''usage example:
	import imddata
	imd = imddata.ImdData('params.imd')
	
	
	
	'''
	db_file = ''
	
	# list, element is string
	list_machine_names = [] 
	
	# dict, element is machine string:list(material string)
	dict_machine_material_names = {} 
	
	# dict, element is machine string:dict(key string:value string)
	dict_machine_common_params = {} 
	
	# dict, element is machine string:dict( precision string:dict(key string:value string) )
	dict_machine_precision_params = {} 
	
	# dict, element is machine string:dict( material string:dict(key string:value string) )
	dict_machine_material_params = {} 
	
	# test tag
	disp = True
	
	
	def __init__(self, file):
		db_file = file
		sqliteobj = sqlite_helper.SqliteHelper(file)
		
		row_machine_names = sqliteobj.select_cmd_data\
		('select valuestr from t_paramsData where groupstr = ?', ['list_machines'])
		self.__fill_list_machine_names(row_machine_names)
		
		row_machine_material_names = sqliteobj.select_cmd_data\
		('select valuestr, machinestr from t_paramsData where groupstr = ?', ['list_materials'])
		self.__fill_dict_machine_material_names(row_machine_material_names)
		
		row_machine_common_params = sqliteobj.select_cmd_data\
		('select keystr, valuestr, machinestr from t_paramsData where groupstr = ?', ['common'])
		self.__fill_dict_machine_common_params(row_machine_common_params)
		
		row_machine_precision_params = sqliteobj.select_cmd_data\
		('select keystr, valuestr, linkitem, machinestr from t_paramsData where groupstr = ?', ['precision'])
		self.__fill_dict_machine_precision_params(row_machine_precision_params)
		
		row_machine_material_params = sqliteobj.select_cmd_data\
		('select keystr, valuestr, linkitem, machinestr from t_paramsData where groupstr = ?', ['material'])
		self.__fill_dict_machine_material_params(row_machine_material_params)
		
	def __fill_list_machine_names(self, rows):
		for line in rows:
			if line['valuestr'] != None: # in fact, we assume that this must be non-None
				self.list_machine_names.append(line['valuestr'])
	
	def __fill_dict_machine_material_names(self, rows):
		dict = {}
		for line in rows:
			if dict.has_key( line['machinestr'] ): # has key, append to list
				dict[ line['machinestr'] ].append( line['valuestr'] )
			else: # create a key-value
				dict[ line['machinestr'] ] = [ line['valuestr'] ]
		self.dict_machine_material_names = dict
	
	
	def __fill_dict_machine_common_params(self, rows):
		dict = {}
		for line in rows:
			if not dict.has_key( line['machinestr'] ): 
			# if this machine is non-existed, initialize first
				dict[ line['machinestr'] ] = {}
				
			dict[ line['machinestr'] ] [ line['keystr'] ] = line['valuestr']
		self.dict_machine_common_params = dict
		
	def __fill_dict_machine_precision_params(self, rows):
		dict = {}
		for line in rows:
			if not dict.has_key( line['machinestr'] ): 
			# if this machine is non-existed, initialize first
				dict[ line['machinestr'] ] = {}
				
			if not dict[ line['machinestr'] ].has_key( line['linkitem'] ): 
			# if this precision is non-existed, initialize first
				dict[ line['machinestr'] ] [ line['linkitem'] ] = {}
			
			dict[ line['machinestr'] ] [ line['linkitem'] ] [ line['keystr'] ] = line['valuestr']
		self.dict_machine_precision_params = dict
			
	def __fill_dict_machine_material_params(self, rows):
		# in fact, this method is totally the same with __fill_dict_machine_precision_params
		dict = {}
		for line in rows:
			if not dict.has_key( line['machinestr'] ): 
			# if this machine is non-existed, initialize first
				dict[ line['machinestr'] ] = {}
				
			if not dict[ line['machinestr'] ].has_key( line['linkitem'] ): 
			# if this precision is non-existed, initialize first
				dict[ line['machinestr'] ] [ line['linkitem'] ] = {}
			
			dict[ line['machinestr'] ] [ line['linkitem'] ] [ line['keystr'] ] = line['valuestr']
		self.dict_machine_material_params = dict
		
		
		
		
		
		
	# ***************************** public methods *****************************
	def getMachineList(self):
		return self.list_machine_names
	
	def getMaterialsListByMachine(self, machine):
		if self.dict_machine_material_names.has_key(machine):
			return self.dict_machine_material_names[machine]
		else:
			return None
	
	
	# common params *****************************
	def getCommonParamsDictByMachine(self, machine):
		if self.dict_machine_common_params.has_key(machine):
			return self.dict_machine_common_params[machine]
		else:
			return None
	
	def getCommonParamValueByMachineKey(self, machine, key):
		if self.dict_machine_common_params.has_key(machine):
			if self.dict_machine_common_params[machine].has_key(key):
				return self.dict_machine_common_params[machine][key]
		return None
		
	# precision params ************************
	def getPrecisionParamsDictByMachinePrecision(self, machine, precision):
		if self.dict_machine_precision_params.has_key(machine):
			if self.dict_machine_precision_params[machine].has_key(precision):
				return self.dict_machine_precision_params[machine][precision]
		return None
			
	def getPrecisionParamValueByMachinePrecisionKey(self, machine, precision, key):
		if self.dict_machine_precision_params.has_key(machine):
			if self.dict_machine_precision_params[machine].has_key(precision):
				if self.dict_machine_precision_params[machine][precision].has_key(key):
					return self.dict_machine_precision_params[machine][precision][key]
		return None	
	
	# material params
	def getMaterialParamsDictByMachineMaterial(self, machine, material):
		if self.dict_machine_material_params.has_key(machine):
			if self.dict_machine_material_params[machine].has_key(material):
				return self.dict_machine_material_params[machine][material]
		return None
	
	def getMaterialParamValueByMachineMaterialKey(self, machine, material, key):
		if self.dict_machine_material_params.has_key(machine):
			if self.dict_machine_material_params[machine].has_key(material):
				if self.dict_machine_material_params[machine][material].has_key(key):
					return self.dict_machine_material_params[machine][material][key]
		return None
		
imd = ImdData(resources.getPathForImd('params.imd'))
		
		
		
		
		
		
		
		
		
		
	
	