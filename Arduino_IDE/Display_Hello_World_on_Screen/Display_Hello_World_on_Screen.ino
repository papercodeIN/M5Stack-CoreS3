
#include <M5CoreS3.h>

void setup() {
    M5.begin();  // Init M5CoreS3
    M5.Lcd.setCursor(20, 119);
    M5.Lcd.setTextColor(WHITE);
    M5.Lcd.setTextSize(3);
    M5.Lcd.printf("Fusion Automate");  // Print text on the screen (string)

}

void loop() {
}