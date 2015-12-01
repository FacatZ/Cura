
import wx
from Cura.util import profile
from Cura.util import resources

class customSettingPanel(wx.Panel):
	def __init__(self, parent, callback=None):

		super(wx.Panel, self).__init__(parent)
		self._machine_type = ['standard', 'nonstandard']
		# self._print_type = ['expert', 'simple']
		# self._consumptive_material_setting = []
		
		sizer = wx.GridBagSizer()
		self.SetSizer(sizer)

		#create machine type panel
		machineTypePanel = wx.Panel(self)
		sb = wx.StaticBox(machineTypePanel, label=_("Machine Type"))
		boxsizer = wx.StaticBoxSizer(sb, wx.HORIZONTAL)
		for buttonName in self._machine_type:
			button = wx.Button(machineTypePanel, -1, buttonName)
			boxsizer.Add(button)
		machineTypePanel.SetSizer(boxsizer)#(wx.BoxSizer(wx.HORIZONTAL))
		# machineTypePanel.GetSizer().Add(boxsizer, flag=wx.EXPAND)
		sizer.Add(machineTypePanel, (0, 0), flag=wx.EXPAND)
		