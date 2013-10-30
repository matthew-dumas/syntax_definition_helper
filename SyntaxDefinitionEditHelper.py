import sublime, sublime_plugin, plistlib, pprint, re, os

class syntax_definition_edit_helper(sublime_plugin.TextCommand):
	def run(self, edit):
		self.syntaxDefFile = sublime.packages_path() + "\\" + self.view.settings().get('syntax')
		self.syntaxDefFile = re.sub("Packages\\\\","", self.syntaxDefFile)
		self.syntaxDefFile = re.sub("/","\\\\", self.syntaxDefFile)
		
		self.plistObject = plistlib.readPlist(self.syntaxDefFile)
		self.patterns = self.plistObject.patterns
		self.view.window().show_input_panel("Would you like to add a new pattern to the language definition? (yes/no)","yes",self.generate_file,None,None)		
        #self.view.window().show_input_panel("Would you like to add a new pattern to the language definition? (yes/no)" , 'yes', self.generate_file, None, None)

	def generate_file(self, input):
		if (input.strip() == "yes"):
		        self.view.window().show_input_panel("Please select a group of related tokens that comprise the first scope, then press enter. Enter 'no' to finish." , "" , self.generate_regex, None, None)                
		else: 
		        return

	def generate_regex(self, input):
		regex = "("
		if (input.strip() == 'no'):
		        self.write_file(self)
		        return
		else: 
		        self.patterns.extend([dict(match = "", comment = "" , name = "")])
		        for region in self.view.sel():  
		                regex += "\\b"+self.view.substr(region)+"\\b|"
		        regex = regex[:-1]
		        regex += ")"

		tokens = self.view.find_all(regex)
		for region in tokens:
		        self.view.sel().add(region)

		self.view.window().show_input_panel("Modify regex as needed (all affected tokens should be highlighted):" , regex , self.name_regex, None, None)

	def name_regex(self, input):
		self.patterns[-1]["match"] = input
		self.view.window().show_input_panel("What is contained in this regex? " , "" , self.set_regex_scope, None, None)

	def set_regex_scope(self,input): 
		self.patterns[-1]["comment"] = input
		self.view.window().show_input_panel("Enter the scope classifier: " , "" , self.get_more_tokens, None, None)

	def get_more_tokens(self, input):
		self.patterns[-1]["name"] = input
		self.view.window().show_input_panel("Please select a group of related tokens that comprise the first scope, then press enter. Enter 'no' to finish." , "" , self.generate_regex, None, None)

	def write_file(self, input): 

		#This is where we output to plist
		self.plistObject.patterns = self.patterns

		plistlib.writePlist(self.plistObject, self.syntaxDefFile)
		return



