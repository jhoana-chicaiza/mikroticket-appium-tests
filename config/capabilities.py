
def get_android_capabilities():
    
    capabilities = {
	"platformName": "android",
	"appium:automationName": "UIAutomator2",
	"appium:deviceName": "emulator-5554",
	"appium:appPackage": "com.mikroisp.apps.android.mikrotik.hotspot.voucher.ticket.mikroticket",
	"appium:appActivity": "com.loogika.mikroticket.MainActivity",
	"appium:newCommandTimeout": 3600,
	"appium:connectHardwareKeyboard": "true"
    }
    return capabilities