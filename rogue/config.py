from ConfigParser import RawConfigParser, NoSectionError, NoOptionError, DuplicateSectionError


class Config(object):

    def __init__(self, filename):
        self.filename = filename
        
        self.config = RawConfigParser()
        self.config.read(filename)
        
        self.local_config = {}
        
    def title(self):
        """ Convenience method for retrieving window title """
        return "%s - v%s" % (self.get("__metadata__", "name"), 
                             self.get("__metadata__", "version"))
        
    def frontend_name(self):
        """ Convenience method for retrieving the desired frontend name """
        return self.get("Game", "frontend")
        
    def resolution(self):
        """ Convenience method for retrieving the requested resolution """
        res = self.get("Video", "resolution")
        res = res.split("x")
        return [int(x) for x in res]
        
    def merge_file(self, filename):
        """ Appends data from given file """
        self.config.read(filename)
    
    def get(self, section, key, default = None):
        try:
            res = self.local_config[section][key]
        except KeyError:
            try:
                res = self.config.get(section, key)
            except (NoSectionError, NoOptionError):
                res = default
        return res
        
    def set(self, section, key, value, store = False):
        if not store:
            try:
                target_dict = self.local_config[section]
            except KeyError:
                self.local_config[section] = {}
            self.local_config[section][key] = value
        else:
            try:
                self.config.add_section(section)
            except DuplicateSectionError:
                pass
            self.config.set(section, key, value)
            self.config.write(open(self.filename, "w"))
            