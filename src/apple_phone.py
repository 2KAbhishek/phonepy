from cell_phone import CellPhone


class ApplePhone(CellPhone):
    """
    ApplePhone class
    """

    def __init__(self, color, model, storage, carrier):
        """
        Initialize class
        """
        super().__init__(color, model, storage, carrier)
        self.airdrop_status = "Off"

    def __str__(self):
        """
        String representation
        """
        return "This is a {} {} Apple Phone.\nCapacity is {}. Carrier is {}\nAirDrop Status is {}".format(
            self.color, self.model, self.storage, self.carrier, self.airdrop_status)

    def get_airdrop_status(self):
        """
        Split screen mode
        """
        return self.airdrop_status

    def set_airdrop_status(self, airdrop_status):
        """
        Split screen mode
        """
        self.airdrop_status = airdrop_status

    def connect_cloud(self):
        """
        Connect to cloud
        """
        print("Connecting to iCloud")

    def download_app(self, app):
        """
        Download app
        """
        print("Opening Apple store to download {} app".format(app))

    def upgrade_storage(self, storage):
        """
        Upgrade storage
        """
        print("Updating storage is not allowed on Apple phones")

    def launch_siri(self):
        """
        Launch Siri
        """
        print("Launching Siri...")
