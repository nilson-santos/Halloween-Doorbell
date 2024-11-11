# Halloween Doorbell

This project turns a Raspberry Pi into a spooky doorbell system that plays random Halloween sounds when a button is pressed. It’s ideal for adding a fun and eerie touch to Halloween decorations!

## Setup Instructions

### 1. Python Environment Setup

To get started, you’ll need to set up a virtual environment and install the required libraries.

1. **Create and activate the virtual environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
    Make sure to have a `requirements.txt` file listing the libraries needed for this project (e.g., `pygame`, `gpiozero`, `pigpio`).

### 2. Crontab Configuration for Boot Startup

To ensure the application runs automatically when the Raspberry Pi boots up, you can add a cron job:

1. Open your crontab editor:
    ```bash
    crontab -e
    ```

2. Add the following line to run the application at startup:
    ```cron
    @reboot /path/to/venv/bin/python /path/to/main.py
    ```

   Replace `/path/to/venv/bin/python` with the path to the Python executable in your virtual environment and `/path/to/main.py` with the path to your main script.

### 3. Bluetooth Speaker Setup (Optional)

If you want to use a Bluetooth speaker instead of an auxiliary speaker connected via the 3.5mm jack, follow these steps:

1. **Pair and trust the Bluetooth speaker**:
   - Run `bluetoothctl` and enter the following commands:
        ```bash
        agent on
        default-agent
        scan on
        pair [SPEAKER_MAC_ADDRESS]
        trust [SPEAKER_MAC_ADDRESS]
        connect [SPEAKER_MAC_ADDRESS]
        ```
   - Replace `[SPEAKER_MAC_ADDRESS]` with the actual MAC address of your Bluetooth speaker.

2. **Auto-connect Bluetooth speaker on boot**:
   - Add the following command to `/etc/rc.local` before `exit 0` to reconnect the Bluetooth speaker at each boot:
        ```bash
        bluetoothctl connect [SPEAKER_MAC_ADDRESS] &
        ```

3. **Alternatively**, you can use a speaker with a 3.5mm audio cable by plugging it directly into the Raspberry Pi.

## Usage

1. Make sure the Raspberry Pi is connected to the speaker.
2. Press the button connected to GPIO pin 10 (or modify the code to the correct pin as per your setup).
3. When the button is pressed, a random Halloween sound from the `sounds` directory will play.

Happy Halloween!