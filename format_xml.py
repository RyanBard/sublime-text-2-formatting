import sublime, sublime_plugin, subprocess
#from xml.etree import ElementTree as ET

class FormatXmlCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        selection = self.view.sel()[0]

        if selection.empty():
            # Use the whole view if they don't have anything selected
            region = sublime.Region(0, self.view.size())
        else:
            # Only use the selected text if they have a selection
            region = selection

        source = self.view.substr(region)
        result = self.pretty_print(source)

        # Replace the buffer
        self.view.replace(edit, region, result)


    def pretty_print(self, source):
        #element = ET.fromstring(source)
        #lines  = ET.tostringlist(element)
        lines = [
            "XML parsing seems to be a mess in Python right now, so I'm not bothering with this!",
            "I tried examples of ElementTree from python.org",
            "I tried the example from twigstechtips using xml.dom.minidom",
            "In both cases, it would appear my install of python has a mix of conflicting versions of things",
            "ImportErrors coming from the xml modules -- not my code",
            "My best guess is that I have a mix of 2.6/2.7 python or something, however...",
            "I don't know enough to proceed without wasting a lot of time for something I don't need right now",
            "It's not clear to me how stable xml parsing is in Python -- does it change and break every minor version?"
        ]
        return '\n'.join([line for line in lines if line.strip()])


    def description(self):
        return "Format Xml"
