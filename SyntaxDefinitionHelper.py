import sublime, sublime_plugin, pprint, plistlib, StringIO, os, re, uuid

class syntax_definition_patterns():
    begin = "" 
    end = ""
    name = ""
    begincaptures = {}
    endcaptures = {}
    captures = {}
    comment = ""
    match = ""
    include = ""

class syntax_definition_helper(sublime_plugin.TextCommand):
    def run(self, edit):
        self.extensions = []
        self.name = "My Custom Language"
        self.scope = "custom.mcl"
        self.this_uuid = str(uuid.uuid1())
        self.patterns = []
        self.patterns_index = -1

        window = sublime.active_window()

        langFile = "../../"+self.view.settings().get('syntax')

        self.view.window().show_input_panel("Would you like to create a language definition? (yes/no)" , 'yes', self.generate_file, None, None)

    def generate_file(self, input):
        fn = self.view.file_name()
        if (input.strip() == "yes"):
                fileName, fileExtension = os.path.splitext(fn)
                self.view.window().show_input_panel("Enter file extensions this applies to (ex: .txt .asm .def)" , fileExtension , self.set_extensions, None, None)
        else: 
                return

    def set_extensions(self, input):                
        input = re.sub("\s+","", input)
        input = re.sub("^\.","", input)
        extensions = input.split(".")
        self.extensions = extensions
        self.view.window().show_input_panel("What is the name of this language? (ex: XML)" , self.name , self.set_name, None, None)

    def set_name(self, input):
        self.name = input
        self.view.window().show_input_panel("Enter a UUID for this language, or keep the randomly generated one: " , self.this_uuid , self.set_uuid, None, None)

    def set_uuid(self, input):
        self.this_uuid = input
        self.view.window().show_input_panel("Enter a root-scope for this language (ex: text.xml): " , self.scope , self.set_scope, None, None)

    def set_scope(self, input):
        self.scope = input
        self.view.window().show_input_panel("Please select a group of related tokens that comprise the first scope, then press enter. Enter 'no' to finish." , "" , self.generate_regex, None, None)                

    def generate_regex(self, input): 
        regex = "("
        if (input.strip() == 'no'):
                self.write_file(self)
                return
        else: 
                self.patterns_index = self.patterns_index + 1
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
        self.patterns[self.patterns_index]["match"] = input
        self.view.window().show_input_panel("What is contained in this regex? " , "" , self.set_regex_scope, None, None)

    def set_regex_scope(self,input): 
        self.patterns[self.patterns_index]["comment"] = input
        self.view.window().show_input_panel("Enter the scope classifier: " , "" , self.get_more_tokens, None, None)

    def get_more_tokens(self, input):
        self.patterns[self.patterns_index]["name"] = input
        self.view.window().show_input_panel("Please select a group of related tokens that comprise the first scope, then press enter. Enter 'no' to finish." , "" , self.generate_regex, None, None)

    def write_file(self, input): 

        #This is where we output to plist
        plObject = {
            "name": self.name,
            "scopeName": self.scope,
            "fileTypes": self.extensions,
            "uuid": self.this_uuid,
            "patterns" : self.patterns
            }
        os.chdir("..")
        directory = sublime.packages_path() + "\\" + self.name
        os.makedirs(directory)

        plistlib.writePlist(plObject, directory+"\\"+ self.scope+".tmLanguage")
        return



