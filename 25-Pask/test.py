from autotest_lib.client.common_lib.cros import chromedriver

with chromedriver.chromedriver() as chromedriver_instance:

   driver = chromedriver_instance.driver

   # Here you can make standard Chrome Driver calls through the driver instance.

   driver.get(nturl2)

