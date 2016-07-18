int voltage_pin1 = A0;
int voltage_pin2 = A1;
double voltage1 = 0.0;
double voltage2 = 0.0;

// Code reads two analog in pins every 0.5 seconds
// Converts raw int to float representing voltage
// Sends data over USB serial connection to computer

void setup() {
  // Start serial connection, with baudrate=9600Hz
  Serial.begin(9600);
  Serial.flush();
  pinMode(voltage_pin1, INPUT);
  pinMode(voltage_pin2, INPUT);
}

void loop() {
  // Read both analog in pins to be read
  voltage1 = analogRead(A0)*5.0/1024.;
  voltage2 = analogRead(A1)*5.0/1024.;

  Serial.print(voltage1);
  Serial.print(",");
  Serial.println(voltage2);

  // Wait 0.5 sec before repeating
  delay(500);
}
