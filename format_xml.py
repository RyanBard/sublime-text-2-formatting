import sublime, sublime_plugin, subprocess
import xml.dom.minidom
from xml.etree import ElementTree

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
        parsed = xml.dom.minidom.parseString(source)
        lines  = parsed.toprettyxml(indent = ' ' * 4).split('\n')
        return '\n'.join([line for line in lines if line.strip()])


    def description(self):
        return "Format Xml"
