# PiGRRL Switch
An emulation console based off of [Adafruit's PiGRRL](https://learn.adafruit.com/pigrrl-2/overview) and styled after the Nintendo Switch

## Hardware
Below is the BOM for a single controller and console:
1. FauxCon Controller
..* Arduino Pro Minis (x1)
..* HM-10 Bluetooth 4.0 Modules (x1)
..* 6mm Tactile Switch (x8)
..* 12mm Tactile Switch (x2)
..* LiPo Battery (x1)
..* 3D Printed Case (x1)
2. PiGRRL Body
..* 7-inch Electrow Screen (x1)
..* Raspberry Pi 3 (x1)
..* HDMI Splitter (x1)
..* HDMI Cable (x2)
..* LiPo Battery (x1)
..* PowerBoost 1000 (x1)
..* 3D Printed Case (x1)
3. Dock
..* HDMI Cable (x1)
..* USB Charger with micro connector (x1)
..* 3D printed Holder (x1)

## Firmware
The firmware for the FauxCon controllers executes the following steps:
1. Connect and set up the HM-10 module
2. Rename the HM-10 to a unique identifier
3. Read the state of all of the connected buttons
4. Transmit the button states to the Raspberry Pi

## Software
The software runs on the Raspberry Pi in the background on startup.  The FauxCons need to be manually connected to the console.  It executes the following steps:
1. Determines the number of separate FauxCons connected to the console
2. Creates a separate uinput device for each controller
3. Reads the button states from each controller and converts presses into uinput events
