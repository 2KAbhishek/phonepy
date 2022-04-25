import time


class CellPhone:
    """
    CellPhone class
    """

    def __init__(self, color, model, storage, carrier):
        """
        Initialize class
        """
        self.color = color
        self.model = model
        self.storage = storage
        self.carrier = carrier

    def __str__(self):
        """
        String representation
        """
        return
        "This is a {} {} Phone.\nCapacity is {}. Carrier is {}".format(
            self.color, self.model, self.storage, self.carrier)

    def get_color(self):
        """
        Color
        """
        return self.color

    def set_color(self, color):
        """
        Color
        """
        self.color = color

    def get_model(self):
        """
        Model
        """
        return self.model

    def set_model(self, model):
        """
        Model
        """
        self.model = model

    def get_storage(self):
        """
        Storage
        """
        return self.storage

    def set_storage(self, storage):
        """
        Storage
        """
        self.storage = storage

    def get_carrier(self):
        """
        Carrier
        """
        return self.carrier

    def set_carrier(self, carrier):
        """
        Carrier
        """
        self.carrier = carrier

    def upgrade_storage(self, storage):
        """
        Upgrade storage
        """
        pass

    def connect_cloud(self):
        """
        Connect to cloud
        """
        pass

    def download_app(self, app):
        """
        Download app
        """
        pass

    def get_time(self):
        """
        Get time
        """
        print("Time is {}".format(time.strftime("%hh:%mm %p")))

    def get_date(self):
        """
        Get date
        """
        print("Date is {}".format(time.strftime("%m/%d/%Y")))

    def place_call(self, number):
        """
        Place call
        """
        print("Calling number {}".format(number))

    def send_sms(self, msg, number):
        """
        Send sms
        """
        print("Sending message '{}' to {}".format(number, msg))
