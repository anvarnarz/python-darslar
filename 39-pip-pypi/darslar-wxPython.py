"""
11/03/2021

Dasturlash asoslari

#39-DARS. PYTHON TASHQI KUTUBXONASI

Muallif: Anvar Narzullaev

Web sahifa: https://python.sariq.dev
"""
# wxPython
import wx
from googletrans import Translator

tarjimon = Translator()
class MyFrame(wx.Frame):    
    def __init__(self):
        super().__init__(parent=None, title='Oʻzbek-Ingliz Lugʻat')
        panel = wx.Panel(self)        
        my_sizer = wx.BoxSizer(wx.VERTICAL)        
        self.text_ctrl = wx.TextCtrl(panel)
        my_sizer.Add(self.text_ctrl, 0, wx.ALL | wx.EXPAND, 5)        
        
        my_btn = wx.Button(panel, label='TARJIMA')
        my_btn.Bind(wx.EVT_BUTTON, self.on_press)
        my_sizer.Add(my_btn, 0, wx.ALL | wx.CENTER, 5)        
        
        self.text_out = wx.TextCtrl(panel,style = wx.TE_READONLY)        
        my_sizer.Add(self.text_out, 0, wx.ALL | wx.EXPAND, 5)         
        panel.SetSizer(my_sizer)        
        self.Show()

    def on_press(self, event):
        value = self.text_ctrl.GetValue()
        if not value:                       
            self.text_out.SetValue("Soʻz kiritmadingiz")
        else:
            tarjima = tarjimon.translate(value, src='uz', dest='en')
            self.text_out.SetValue(tarjima.text.capitalize()) 
    

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()