#define BAUDRATE 115200
#define N_DIGITAL_PINS 14
#define N_ANALOG_PINS 6

#define digitalStateBufferSize (N_DIGITAL_PINS-8)/8+2

void setup() {
    Serial.begin(BAUDRATE);
    while (!Serial) {;}

    // All digital pins as inputs
    for (int i=0; i<=13; i++)
        pinMode(i, INPUT);

    // All analog pins as inputs
    for (int i=A0; i<=A5; i++)
        pinMode(i, INPUT);

    // Sending number of pins to read
    Serial.write(N_DIGITAL_PINS);
    Serial.write(N_ANALOG_PINS);
}

void loop() {
  
    byte digitalBuffer;
    char* analogBuffer = "0000";

    // Dumping digital pins
    for (int i=0; i<digitalStateBufferSize; i++){
        digitalBuffer = 0;
        for (int j=i*8; j<8*(i+1); j++){
            digitalBuffer << 1;
            digitalBuffer |= digitalRead(j);
        }
        Serial.write(digitalBuffer);
    }
    // Dumping analog pins as strings(comma-separated values)
    Serial.write(',');
    for (int i=0; i<N_ANALOG_PINS; i++){
        sprintf(analogBuffer, "%04d\0", analogRead(i));
        Serial.write(analogBuffer); Serial.write(',');
    }
}
