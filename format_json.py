import sublime, sublime_plugin, json

class FormatJsonCommand(sublime_plugin.TextCommand):
    
    def run(self, edit):
        selection = self.view.sel()[0]

        if selection.empty():
            # Use the whole view if they don't have anything selected
            region = sublime.Region(0, self.view.size())
        else:
            # Only use the selected text if they have a selection
            region = selection

        source = self.view.substr(region)
        result = json.dumps(json.loads(source), sort_keys = True, indent = 4)

        # Replace the buffer
        self.view.replace(edit, region, result)


    def description(self):
        return "Format Json"
