from android_phone import AndroidPhone
from apple_phone import ApplePhone


def applePhoneTest():
    iPhone = ApplePhone('Black', '11 Pro', 64, 'Verizon')
    iPhone.set_airdrop_status('On')
    print(iPhone)
    iPhone.get_storage()
    iPhone.upgrade_storage(128)
    iPhone.connect_cloud()
    iPhone.download_app('FaceTime')
    iPhone.get_time()
    iPhone.get_date()
    iPhone.place_call('1234567890')
    iPhone.send_sms('Hello', '1234567890')
    iPhone.launch_siri()


def androidPhoneTest():
    android = AndroidPhone('Black', 'Pixel 3', 128, 'Verizon')
    android.set_split_screen_mode('On')
    print(android)
    android.get_storage()
    android.upgrade_storage(256)
    android.connect_cloud()
    android.download_app('Zoom')
    android.get_time()
    android.get_date()
    android.place_call('1234567890')
    android.send_sms('Hello', '1234567890')
    android.launch_google_assistant()


if __name__ == "__main__":
    androidPhoneTest()
    print("\n")
    applePhoneTest()
