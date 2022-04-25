from cell_phone import CellPhone


class AndroidPhone(CellPhone):
    """
    AndroidPhone class
    """

    def __init__(self, color, model, storage, carrier):
        """
        Initialize class
        """
        super().__init__(color, model, storage, carrier)
        self.split_screen_mode = "Off"

    def __str__(self):
        """
        String representation
        """
        return "This is a {} {} Android Phone.\nCapacity is {}. Carrier is {}\nSplit Screen Mode is {}".format(
            self.color, self.model, self.storage, self.carrier, self.split_screen_mode)

    def get_split_screen_mode(self):
        """
        Split screen mode
        """
        return self.split_screen_mode

    def set_split_screen_mode(self, split_screen_mode):
        """
        Split screen mode
        """
        self.split_screen_mode = split_screen_mode

    def connect_cloud(self):
        """
        Connect to cloud
        """
        print("Connecting to Google drive")

    def download_app(self, app):
        """
        Download app
        """
        print("Opening Google play to download {} app".format(app))

    def upgrade_storage(self, storage):
        """
        Upgrade storage
        """
        if storage > self.storage:
            print("Old storage: {}".format(self.storage))
            print("New storage: {}".format(storage))
            self.storage = storage
        else:
            print("You can't rollback memory!")

    def launch_google_assistant(self):
        """
        Launch Google assistant
        """
        print("Launching Google assistant...")
