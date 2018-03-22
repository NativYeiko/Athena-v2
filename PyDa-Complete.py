import wx
from espeak import espeak
import wikipedia
import wolframalpha
from espeak import espeak
import wolframalpha

app_id = "2WH72K-U3U8K9HY3Q"
client = wolframalpha.Client(app_id)

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None,
            pos=wx.DefaultPosition, size=wx.Size(450, 100),
            style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION |
             wx.CLOSE_BOX | wx.CLIP_CHILDREN,
            title="Athena")
        panel = wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        lbl = wx.StaticText(panel,
        label="Bonjours a toi, je suis Athena, une ia Assistante sous Python, en quoi puije d'aider?")
        my_sizer.Add(lbl, 0, wx.ALL, 5)
        self.txt = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER,size=(400,30))
        self.txt.SetFocus()
        self.txt.Bind(wx.EVT_TEXT_ENTER, self.OnEnter)
        my_sizer.Add(self.txt, 0, wx.ALL, 5)
        panel.SetSizer(my_sizer)
        self.Show()

    def OnEnter(self, event):

        input = self.txt.GetValue()
        input = input.lower()
        try:
        	res = client.query(input)
        	answer = next(res.results).text
        	print answer
                espeak.synth("Voici la réponce "+str(answer))
       	except:
       		try:
       			input = input.split(' ')
       			input = ' '.join(input[2:])
       			print wikipedia.summary(input)
       		except:
       			print "Désolé je ne c'est pas"


if __name__ == "__main__":
    app = wx.App(True)
    frame = MyFrame()
    app.MainLoop()
