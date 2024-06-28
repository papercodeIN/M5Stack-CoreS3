#include <M5CoreS3.h>

void setup() {
    M5.begin();  // Init M5CoreS3
    M5.Lcd.qrcode(
        "https://youtube.com/@fusion_automate", 40, 0, 240, 6);  
        // Create a QR code with a width of 150 QR code with version 6 at (0, 0).  
        // Please select the appropriate QR code version according to the number of characters.  
}

void loop() {
}
