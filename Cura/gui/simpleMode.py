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

		productTypeItems = [u'导入标准', u'导入非标准']
		productTypePanel = wx.Panel(self)
		sb = wx.StaticBox(productTypePanel, label='产品类型')
		boxsizer = wx.StaticBoxSizer(sb, wx.HORIZONTAL)
		for item in productTypeItems:
			button = wx.Button(productTypePanel, -1, item)
			boxsizer.Add(button)
		productTypePanel.SetSizer(wx.BoxSizer(wx.VERTICAL))
		productTypePanel.GetSizer().Add(boxsizer)
		sizer.Add(productTypePanel, (0, 0), flag=wx.EXPAND)

		#print model
		printModelPanel = wx.Panel(self)
		sb = wx.StaticBox(printModelPanel, label='打印模式')
		boxsizer = wx.StaticBoxSizer(sb, wx.VERTICAL)
		##add panel
		nb = wx.Notebook(printModelPanel)
		expertModelPanel = wx.Panel(nb)
		###add components to expert model panel
		radioNames = '高精度 中精度 低精度'.split()
		# subsb = wx.StaticBox(expertModelPanel, label='精度设置')
		subboxsizer = wx.BoxSizer(wx.VERTICAL)
		subboxsizer.Add(wx.RadioBox(expertModelPanel, -1, '精度设置', choices=radioNames, majorDimension=3))
		###支撑设置
		subsb = wx.StaticBox(expertModelPanel, label='支撑设置')
		subboxsizer2 = wx.StaticBoxSizer(subsb, wx.HORIZONTAL)
		subst = wx.StaticText(expertModelPanel, -1, '支撑类型')
		subboxsizer2.Add(subst, flag=wx.ALIGN_BOTTOM)
		subboxsizer2.Add(wx.RadioBox(expertModelPanel, -1, '', choices='有 无'.split(), majorDimension=2))
		subboxsizer.Add(subboxsizer2)

		###填充设置
		subboxsizer2 = wx.BoxSizer(wx.VERTICAL)
		subsb = wx.StaticBox(expertModelPanel, label='填充设置')
		subboxsizer3 = wx.StaticBoxSizer(subsb, wx.HORIZONTAL)
		subst = wx.StaticText(expertModelPanel, -1, '填充密度(%)')
		subboxsizer3.Add(subst)
		tc = wx.TextCtrl(expertModelPanel, -1, '')
		subboxsizer3.Add(tc)
		subboxsizer2.Add(subboxsizer3)
		self.density = 0
		slider = wx.Slider(expertModelPanel, -1, 50, 1, 100, size=(150,-1), style=wx.SL_HORIZONTAL | wx.SL_AUTOTICKS | wx.SL_LABELS)
		subboxsizer2.Add(slider)

		subboxsizer.Add(subboxsizer2)
		expertModelPanel.SetSizer(subboxsizer)

		simpleModelPanel = wx.Panel(nb)
		nb.AddPage(expertModelPanel, '专家模式')
		nb.AddPage(simpleModelPanel, '简单模式')
		boxsizer.Add(nb)

		printModelPanel.SetSizer(wx.BoxSizer(wx.VERTICAL))
		printModelPanel.GetSizer().Add(boxsizer)
		sizer.Add(printModelPanel, (1, 0), flag=wx.EXPAND)

		consumptiveMaterialSettingPanel = wx.Panel(self)
		sb = wx.StaticBox(consumptiveMaterialSettingPanel, label='耗材设置')
		boxsizer = wx.StaticBoxSizer(sb, wx.HORIZONTAL)
		st = wx.StaticText(consumptiveMaterialSettingPanel, label='耗材类型')
		boxsizer.Add(st)
		#change normal button to list button
		materialList = ['PLA', 'A', 'B', 'C']
		cbb = wx.ComboBox(consumptiveMaterialSettingPanel, -1, 'PLA', size=(100, 25), choices=materialList, style=wx.CB_DROPDOWN)
		boxsizer.Add(cbb)
		consumptiveMaterialSettingPanel.SetSizer(wx.BoxSizer(wx.VERTICAL))
		consumptiveMaterialSettingPanel.GetSizer().Add(boxsizer)
		sizer.Add(consumptiveMaterialSettingPanel, (2, 0), flag=wx.EXPAND)

		sliceSettingPanel = wx.Panel(self)
		sb = wx.StaticBox(sliceSettingPanel, label='切片')
		boxsizer = wx.StaticBoxSizer(sb, wx.HORIZONTAL)
		st = wx.StaticText(sliceSettingPanel, label='切片开始')
		boxsizer.Add(st)
		button = wx.Button(sliceSettingPanel, -1, '开始')
		boxsizer.Add(button)
		sliceSettingPanel.SetSizer(wx.BoxSizer(wx.VERTICAL))
		sliceSettingPanel.GetSizer().Add(boxsizer)
		sizer.Add(sliceSettingPanel, (3, 0), flag=wx.EXPAND)

		printerControlPanel = wx.Panel(self)
		sb = wx.StaticBox(printerControlPanel, label='打印机控制')
		boxsizer = wx.StaticBoxSizer(sb, wx.HORIZONTAL)
		st = wx.StaticText(printerControlPanel, -1, '打开打印机控制')
		boxsizer.Add(st)
		button = wx.Button(printerControlPanel, -1, '打开')
		boxsizer.Add(button)
		printerControlPanel.SetSizer(wx.BoxSizer(wx.VERTICAL))
		printerControlPanel.GetSizer().Add(boxsizer)
		sizer.Add(printerControlPanel, (4, 0), flag=wx.EXPAND)
		#additional panel
		# testPanel = wx.Panel(self)
		# sb = wx.StaticBox(testPanel, label='test')
		# boxsizer = wx.StaticBoxSizer(sb, wx.HORIZONTAL)
		# button = wx.Button(testPanel, -1, 'Hello')
		# boxsizer.Add(button, 0, wx.ALL, 2)
		# button = wx.Button(testPanel, -1, 'World')
		# boxsizer.Add(button, 0, wx.ALL, 2)
		# button = wx.Button(testPanel, -1, 'aha')
		# boxsizer.Add(button, 0, wx.ALL, 2)
		# testPanel.SetSizer(wx.BoxSizer(wx.VERTICAL))
		# testPanel.GetSizer().Add(boxsizer, flag=wx.EXPAND)
		# sizer.Add(testPanel, (4, 0), flag=wx.EXPAND)

		# sb = wx.StaticBox(printTypePanel, label=_("Select a quickprint profile:"))
		# boxsizer = wx.StaticBoxSizer(sb, wx.VERTICAL)
		# for button in self._print_profile_options:
		# 	boxsizer.Add(button)
		# printTypePanel.SetSizer(wx.BoxSizer(wx.VERTICAL))
		# printTypePanel.GetSizer().Add(boxsizer, flag=wx.EXPAND)
		# sizer.Add(printTypePanel, (0,0), flag=wx.EXPAND)

		# sb = wx.StaticBox(printMaterialPanel, label=_("Material:"))
		# boxsizer = wx.StaticBoxSizer(sb, wx.VERTICAL)
		# for button in self._print_material_options:
		# 	boxsizer.Add(button)
		# printMaterialPanel.SetSizer(wx.BoxSizer(wx.VERTICAL))
		# printMaterialPanel.GetSizer().Add(boxsizer, flag=wx.EXPAND)
		# sizer.Add(printMaterialPanel, (1,0), flag=wx.EXPAND)

		# sb = wx.StaticBox(printNozzlePanel, label=_("Nozzle:"))
		# boxsizer = wx.StaticBoxSizer(sb, wx.VERTICAL)
		# for button in self._print_nozzle_options:
		# 	boxsizer.Add(button)
		# printNozzlePanel.SetSizer(wx.BoxSizer(wx.VERTICAL))
		# printNozzlePanel.GetSizer().Add(boxsizer, flag=wx.EXPAND)
		# sizer.Add(printNozzlePanel, (2,0), flag=wx.EXPAND)

		# sb = wx.StaticBox(self, label=_("Other:"))
		# boxsizer = wx.StaticBoxSizer(sb, wx.VERTICAL)
		# boxsizer.Add(self.printSupport)
		# sizer.Add(boxsizer, (3,0), flag=wx.EXPAND)

		# for button in self._print_profile_options:
		# 	button.Bind(wx.EVT_RADIOBUTTON, self._update)
		# for button in self._print_material_options:
		# 	button.Bind(wx.EVT_RADIOBUTTON, self._update)
		# for button in self._print_nozzle_options:
		# 	button.Bind(wx.EVT_RADIOBUTTON, self._update)

		# self.printSupport.Bind(wx.EVT_CHECKBOX, self._update)

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
