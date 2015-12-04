#coding=utf-8
__copyright__ = "Copyright (C) 2013 David Braam - Released under terms of the AGPLv3 License"

import wx
import ConfigParser as configparser
import os.path

from Cura.util import profile
from Cura.util import resources

class simpleModePanel(wx.Panel):
	"Main user interface window for Quickprint mode"
	def __init__(self, parent, callback):
		super(simpleModePanel, self).__init__(parent)

		# self._callback = callback

		# self._print_profile_options = []
		# self._print_material_options = []
		# self._print_nozzle_options = []

		# nozzle_options = []
		# printTypePanel = wx.Panel(self)
		# for filename in resources.getSimpleModeProfiles(profile.getMachineSetting('machine_type')):
			# cp = configparser.ConfigParser()
			# cp.read(filename)
			# base_filename = os.path.splitext(os.path.basename(filename))[0]
			# name = base_filename
			# if cp.has_option('info', 'name'):
			# 	name = cp.get('info', 'name')
			# nozzle = profile.getProfileSetting('nozzle_size')
			# if cp.has_option('profile', 'nozzle_size'):
			# 	nozzle = cp.get('profile', 'nozzle_size')
			# 	if nozzle not in nozzle_options:
			# 		nozzle_options.append(nozzle)
			# for button in self._print_profile_options:
			# 	if button.GetLabel() == name:
			# 		button.filename[nozzle] = filename
			# 		nozzle = None

			# if nozzle is not None:
			# 	button = wx.RadioButton(printTypePanel, -1, name, style=wx.RB_GROUP if len(self._print_profile_options) == 0 else 0)
			# 	button.base_filename = base_filename
			# 	button.filename = {nozzle: filename}
			# 	self._print_profile_options.append(button)
			# 	if profile.getPreference('simpleModeProfile') == base_filename:
			# 		button.SetValue(True)

		

		# printMaterialPanel = wx.Panel(self)
		# for filename in resources.getSimpleModeMaterials():
		# 	cp = configparser.ConfigParser()
		# 	cp.read(filename)
		# 	base_filename = os.path.splitext(os.path.basename(filename))[0]
		# 	name = base_filename
		# 	if cp.has_option('info', 'name'):
		# 		name = cp.get('info', 'name')
		# 	button = wx.RadioButton(printMaterialPanel, -1, name, style=wx.RB_GROUP if len(self._print_material_options) == 0 else 0)
		# 	button.base_filename = base_filename
		# 	button.filename = filename
		# 	self._print_material_options.append(button)
		# 	if profile.getPreference('simpleModeMaterial') == base_filename:
		# 		button.SetValue(True)

		# printNozzlePanel = wx.Panel(self)
		# for nozzle_size in nozzle_options:
			# name = str(nozzle_size) + "mm"
			# button = wx.RadioButton(printNozzlePanel, -1, name, style=wx.RB_GROUP if len(self._print_nozzle_options) == 0 else 0)
			# button.nozzle_size = nozzle_size
			# button.nozzle_name = name
			# self._print_nozzle_options.append(button)
			# if profile.getPreference('simpleModeNozzle') == name:
			# 	button.SetValue(True)

		# if profile.getMachineSetting('gcode_flavor') == 'UltiGCode':
		# 	printMaterialPanel.Show(False)
		# if len(nozzle_options) < 1:
		# 	printNozzlePanel.Show(False)

		# self.printSupport = wx.CheckBox(self, -1, _("Print support structure"))

		sizer = wx.GridBagSizer()
		self.SetSizer(sizer)

		#print type panel
		productTypeItems = [u'导入标准', u'导入非标准']
		callbackList = [None, None]
		productTypePanel = wx.Panel(self)
		boxsizer = self.createProductTypeSizer(productTypePanel, productTypeItems, callbackList)
		productTypePanel.SetSizer(wx.BoxSizer(wx.VERTICAL))
		productTypePanel.GetSizer().Add(boxsizer, flag=wx.EXPAND)
		sizer.Add(productTypePanel, (0, 0), flag=wx.EXPAND)

		#print model
		printModelPanel = wx.Panel(self)
		boxsizer = self.createPrintModelSizer(printModelPanel)
		# sb = wx.StaticBox(printModelPanel, label='打印模式')
		# boxsizer = wx.StaticBoxSizer(sb, wx.VERTICAL)
		# ##add panel
		# nb = wx.Notebook(printModelPanel)
		# expertModelPanel = wx.Panel(nb)
		# ###add components to expert model panel
		# radioNames = '高精度 中精度 低精度'.split()
		# # subsb = wx.StaticBox(expertModelPanel, label='精度设置')
		# subboxsizer = wx.BoxSizer(wx.VERTICAL)
		# subboxsizer.Add(wx.RadioBox(expertModelPanel, -1, '精度设置', choices=radioNames, majorDimension=3))
		# ###支撑设置
		# subsb = wx.StaticBox(expertModelPanel, label='支撑设置')
		# subboxsizer2 = wx.StaticBoxSizer(subsb, wx.HORIZONTAL)
		# subst = wx.StaticText(expertModelPanel, -1, '支撑类型')
		# subboxsizer2.Add(subst, flag=wx.ALIGN_BOTTOM)
		# subboxsizer2.Add(wx.RadioBox(expertModelPanel, -1, '', choices='有 无'.split(), majorDimension=2))
		# subboxsizer.Add(subboxsizer2)

		# ###填充设置
		# subboxsizer2 = wx.BoxSizer(wx.VERTICAL)
		# subsb = wx.StaticBox(expertModelPanel, label='填充设置')
		# subboxsizer3 = wx.StaticBoxSizer(subsb, wx.HORIZONTAL)
		# subst = wx.StaticText(expertModelPanel, -1, '填充密度(%)')
		# subboxsizer3.Add(subst)
		# tc = wx.TextCtrl(expertModelPanel, -1, '')
		# subboxsizer3.Add(tc)
		# subboxsizer2.Add(subboxsizer3)
		# self.density = 0
		# slider = wx.Slider(expertModelPanel, -1, 50, 1, 100, size=(150,-1), style=wx.SL_HORIZONTAL | wx.SL_AUTOTICKS | wx.SL_LABELS)
		# subboxsizer2.Add(slider)

		# subboxsizer.Add(subboxsizer2)
		# expertModelPanel.SetSizer(subboxsizer)

		# simpleModelPanel = wx.Panel(nb)
		# nb.AddPage(expertModelPanel, '专家模式')
		# nb.AddPage(simpleModelPanel, '简单模式')
		# boxsizer.Add(nb)

		printModelPanel.SetSizer(wx.BoxSizer(wx.VERTICAL))
		printModelPanel.GetSizer().Add(boxsizer)
		sizer.Add(printModelPanel, (1, 0), flag=wx.EXPAND)


		#consumptive material setting panel 
		consumptiveMaterialSettingPanel = wx.Panel(self)
		sb = wx.StaticBox(consumptiveMaterialSettingPanel, label='耗材设置')
		boxsizer = wx.StaticBoxSizer(sb, wx.HORIZONTAL)
		st = wx.StaticText(consumptiveMaterialSettingPanel, label='耗材类型')
		boxsizer.Add(st, 1, flag=wx.EXPAND)
		materialList = ['PLA', 'A', 'B', 'C']
		cbb = wx.ComboBox(consumptiveMaterialSettingPanel, -1, 'PLA', size=(100, 25), choices=materialList, style=wx.CB_DROPDOWN)
		boxsizer.Add(cbb, 1, flag=wx.EXPAND)
		consumptiveMaterialSettingPanel.SetSizer(wx.BoxSizer(wx.VERTICAL))
		consumptiveMaterialSettingPanel.GetSizer().Add(boxsizer, flag=wx.EXPAND)
		sizer.Add(consumptiveMaterialSettingPanel, (2, 0), flag=wx.EXPAND)

		#slice setting panel
		sliceSettingPanel = wx.Panel(self)
		sb = wx.StaticBox(sliceSettingPanel, label='切片')
		boxsizer = wx.StaticBoxSizer(sb, wx.HORIZONTAL)
		st = wx.StaticText(sliceSettingPanel, label='切片开始')
		boxsizer.Add(st, 1, flag=wx.EXPAND)
		button = wx.Button(sliceSettingPanel, -1, '开始')
		boxsizer.Add(button, 1, flag=wx.EXPAND)
		sliceSettingPanel.SetSizer(wx.BoxSizer(wx.VERTICAL))
		sliceSettingPanel.GetSizer().Add(boxsizer, flag=wx.EXPAND)
		sizer.Add(sliceSettingPanel, (3, 0), flag=wx.EXPAND)

		#printer control panel
		printerControlPanel = wx.Panel(self)
		sb = wx.StaticBox(printerControlPanel, label='打印机控制')
		boxsizer = wx.StaticBoxSizer(sb, wx.HORIZONTAL)
		st = wx.StaticText(printerControlPanel, -1, '打开打印机控制')
		boxsizer.Add(st, 1, flag=wx.EXPAND)
		button = wx.Button(printerControlPanel, -1, '打开')
		boxsizer.Add(button, 1, flag=wx.EXPAND)
		printerControlPanel.SetSizer(wx.BoxSizer(wx.VERTICAL))
		printerControlPanel.GetSizer().Add(boxsizer, flag=wx.EXPAND)
		sizer.Add(printerControlPanel, (4, 0), flag=wx.EXPAND)

	def createProductTypeSizer(self, parent, buttonNameList, callbackList):
		sb = wx.StaticBox(parent, label='产品类型')
		boxsizer = wx.StaticBoxSizer(sb, wx.HORIZONTAL)
		for buttonName in buttonNameList:
			button = wx.Button(parent, -1, buttonName)
			boxsizer.Add(button, 1, flag=wx.EXPAND)
		return boxsizer

	def createPrintModelSizer(self, parent):
		sb = wx.StaticBox(parent, label='打印模式')
		boxsizer = wx.StaticBoxSizer(sb, wx.VERTICAL)

		nb = wx.Notebook(parent)
		expertModelPanel = self.createExpertModelPanel(nb)
		simpleModelPanel = self.createSimpleModelPanel(nb)

		nb.AddPage(expertModelPanel, '专家模式')
		nb.AddPage(simpleModelPanel, '简单模式')

		boxsizer.Add(nb, flag=wx.EXPAND)
		return boxsizer

	def createExpertModelPanel(self, notebook):
		panel = wx.Panel(notebook)
		boxsizer = wx.BoxSizer(wx.VERTICAL)

		#精度设置
		sb = wx.StaticBox(panel, label='精度设置')
		sbsizer = wx.StaticBoxSizer(sb, wx.VERTICAL)
		radioNames = '高精度 中精度 低精度'.split()
		sbsizer.Add(wx.RadioBox(panel, -1, '精度设置', choices=radioNames, majorDimension=3), flag=wx.EXPAND)
		boxsizer.Add(sbsizer, flag=wx.EXPAND)

		#支撑设置
		sb = wx.StaticBox(panel, label='支撑设置')
		sbsizer = wx.StaticBoxSizer(sb, wx.VERTICAL)

		sbboxsizer = wx.BoxSizer(wx.HORIZONTAL)

		st = wx.StaticText(panel, -1, '支撑类型')
		sbboxsizer.Add(st, 1, flag=wx.EXPAND)

		for buttonName in '有 无'.split():
			radioButton = wx.RadioButton(panel, -1, buttonName, style=wx.RB_GROUP if buttonName == '有' else 0)
			sbboxsizer.Add(radioButton, 1, flag=wx.EXPAND)
		sbsizer.Add(sbboxsizer, flag=wx.EXPAND)
		boxsizer.Add(sbsizer, flag=wx.EXPAND)

		#填充设置
		sb = wx.StaticBox(panel, label='填充设置')
		sbsizer = wx.StaticBoxSizer(sb, wx.VERTICAL)

		sbboxsizer = wx.BoxSizer(wx.HORIZONTAL)
		st = wx.StaticText(panel, -1, '填充密度（%）')
		sbboxsizer.Add(st, 1, flag=wx.EXPAND)
		initDensityValue = 50
		tc = wx.TextCtrl(panel, -1, '', style=wx.TE_PROCESS_ENTER)
		tc.SetValue(str(initDensityValue))
		self.densityTextCtrl = tc
		self.density = initDensityValue
		sbboxsizer.Add(tc, 1, flag=wx.EXPAND)
		sbsizer.Add(sbboxsizer, flag=wx.EXPAND)

		slider = wx.Slider(panel, -1, initDensityValue, 1, 100, size=(-1,-1), style=wx.SL_HORIZONTAL | wx.SL_AUTOTICKS | wx.SL_LABELS)		
		self.densitySlider = slider
		sbsizer.Add(slider, flag=wx.EXPAND)
		boxsizer.Add(sbsizer, flag=wx.EXPAND)

		self.Bind(wx.EVT_SLIDER, self.OnDensitySlide, self.densitySlider)
		self.Bind(wx.EVT_TEXT_ENTER, self.OnDensityEnter, self.densityTextCtrl)
		panel.SetSizer(boxsizer)

		return panel

	def OnDensityEnter(self, event):
		try:
			value = self.densityTextCtrl.GetValue()
			value = int(value)
			self.densitySlider.SetValue(value)
			self.density = value
		except:
			self.OnDensitySlide(event)

	def OnDensitySlide(self, event):
		value = self.densitySlider.GetValue()
		self.densityTextCtrl.SetValue(str(value))
		self.density = value

	def createSimpleModelPanel(self, notebook):
		panel = wx.Panel(notebook)

		return panel

	def _update(self, e):
		pass
		# for button in self._print_profile_options:
		# 	if button.GetValue():
		# 		profile.putPreference('simpleModeProfile', button.base_filename)
		# for button in self._print_material_options:
		# 	if button.GetValue():
		# 		profile.putPreference('simpleModeMaterial', button.base_filename)
		# for button in self._print_nozzle_options:
		# 	if button.GetValue():
		# 		profile.putPreference('simpleModeNozzle', button.nozzle_name)
		# self._callback()

	def getSettingOverrides(self):
		pass
		# settings = {}
		# for setting in profile.settingsList:
		# 	if not setting.isProfile():
		# 		continue
		# 	settings[setting.getName()] = setting.getDefault()

		# nozzle = profile.getProfileSetting('nozzle_size')
		# for button in self._print_nozzle_options:
		# 	if button.GetValue():
		# 		nozzle = button.nozzle_size
		# for button in self._print_profile_options:
		# 	if button.GetValue():
		# 		cp = configparser.ConfigParser()
		# 		cp.read(button.filename[nozzle])
		# 		for setting in profile.settingsList:
		# 			if setting.isProfile():
		# 				if cp.has_option('profile', setting.getName()):
		# 					settings[setting.getName()] = cp.get('profile', setting.getName())
		# if profile.getMachineSetting('gcode_flavor') != 'UltiGCode':
		# 	for button in self._print_material_options:
		# 		if button.GetValue():
		# 			cp = configparser.ConfigParser()
		# 			cp.read(button.filename)
		# 			for setting in profile.settingsList:
		# 				if setting.isProfile():
		# 					if cp.has_option('profile', setting.getName()):
		# 						settings[setting.getName()] = cp.get('profile', setting.getName())

		# if self.printSupport.GetValue():
		# 	settings['support'] = "Exterior Only"
		# return settings

	def updateProfileToControls(self):
		pass
